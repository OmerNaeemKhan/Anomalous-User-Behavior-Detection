import os
import re
import textwrap

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Authentication Anomaly Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PATH CONFIGURATION
# ============================================================

DATA_FILE = "data/processed/anomaly_detection_results.csv"


# ============================================================
# HTML / CSS RENDERING GUARDS
#
# Streamlit renders markdown, and markdown ENDS a raw HTML block at the
# first blank line -- after which any line indented 4+ spaces becomes a
# code block. That is why hand-indented HTML (and blank lines between CSS
# rule groups) leak onto the page as literal source text. Both helpers
# strip blank lines and indentation so the browser always receives one
# clean, uninterrupted block.
# ============================================================

def render_html(html):
    cleaned = textwrap.dedent(html).strip()
    cleaned = "\n".join(l.strip() for l in cleaned.splitlines() if l.strip())
    cleaned = re.sub(r">\s+<", "><", cleaned)
    st.markdown(cleaned, unsafe_allow_html=True)


def inject_css(css):
    body = "\n".join(l.strip() for l in css.splitlines() if l.strip())
    st.markdown(body, unsafe_allow_html=True)


# Streamlit renamed use_container_width -> width="stretch" in 1.49.
try:
    _MAJ, _MIN = (int(x) for x in st.__version__.split(".")[:2])
    _NEW_API = (_MAJ, _MIN) >= (1, 49)
except Exception:
    _NEW_API = False

WIDTH_KW = {"width": "stretch"} if _NEW_API else {"use_container_width": True}


# ============================================================
# THEME
# All colours below were checked for WCAG contrast against their
# own background, so secondary text stays readable in dark mode.
# ============================================================

THEMES = {
    "Dark": {
        "scheme": "dark",
        "bg": "#0a1120",
        "surface": "#131f33",
        "surface_2": "#1a293f",
        "sidebar": "#0d1626",
        "border": "#2b4260",
        "text": "#f2f7fd",
        "muted": "#b3c6dd",
        "primary": "#9aa5ff",
        "secondary": "#c4a9ff",
        "success": "#4ade80",
        "warning": "#fcd34d",
        "danger": "#fb8b8b",
        "info": "#67e8f9",
        "grid": "#243a56",
        "plot_bg": "rgba(0,0,0,0)",
        "shadow": "0 4px 22px rgba(0,0,0,.45)",
        "shadow_hover": "0 10px 30px rgba(154,165,255,.20)",
        "card": "linear-gradient(160deg,#131f33 0%,#17263d 100%)",
        "hero": "linear-gradient(135deg,#16233b 0%,#131f33 55%,#1b1a35 100%)",
        "glow": "radial-gradient(1000px 340px at 8% -35%,rgba(154,165,255,.14),transparent 60%)",
    },
    "Light": {
        "scheme": "light",
        "bg": "#f4f7fb",
        "surface": "#ffffff",
        "surface_2": "#f7fafd",
        "sidebar": "#ffffff",
        "border": "#dbe4ef",
        "text": "#0f172a",
        "muted": "#54657d",
        "primary": "#4f46e5",
        "secondary": "#9333ea",
        "success": "#047857",
        "warning": "#b45309",
        "danger": "#be1d1d",
        "info": "#0e7490",
        "grid": "#eef2f7",
        "plot_bg": "#ffffff",
        "shadow": "0 2px 14px rgba(15,23,42,.06)",
        "shadow_hover": "0 10px 28px rgba(79,70,229,.16)",
        "card": "linear-gradient(160deg,#ffffff 0%,#fafbfe 100%)",
        "hero": "linear-gradient(135deg,#eef2ff 0%,#ffffff 52%,#faf5ff 100%)",
        "glow": "radial-gradient(1000px 340px at 8% -35%,rgba(79,70,229,.08),transparent 60%)",
    },
}

if "theme_choice" not in st.session_state:
    st.session_state.theme_choice = "Dark"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


# ============================================================
# CHECK DATA FILE
# ============================================================

if not os.path.exists(DATA_FILE):
    st.error(f"Data file not found: {DATA_FILE}")
    st.info(
        "Please run the following scripts first:\n"
        "1. 01_create_dataset.py\n"
        "2. 02_database_analysis.py\n"
        "3. 03_feature_engineering.py\n"
        "4. 04_anomaly_detection.py"
    )
    st.stop()


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    render_html(
        """
        <div class="brand">
        <div class="brand-icon">🛡️</div>
        <div>
        <div class="brand-name">AUTH ANOMALY</div>
        <div class="brand-sub">Behavioral Detection Engine</div>
        </div>
        </div>
        """
    )

    render_html("<div class='rule'></div>")
    render_html("<div class='side-label'>Appearance</div>")

    theme_choice = st.selectbox(
        "Theme",
        options=["Dark", "Light"],
        index=0 if st.session_state.theme_choice == "Dark" else 1,
        label_visibility="collapsed",
    )
    st.session_state.theme_choice = theme_choice

    render_html("<div class='rule'></div>")
    render_html("<div class='side-label'>🔍 Dashboard Filters</div>")

    # ---------------- USER FILTER ----------------
    users = ["All Users"] + sorted(df["username"].unique().tolist())
    selected_user = st.selectbox("Select User", users)

    # ---------------- RISK LEVEL FILTER ----------------
    risk_levels = ["All Risk Levels"] + sorted(df["risk_level"].unique().tolist())
    selected_risk = st.selectbox("Select Risk Level", risk_levels)

    # ---------------- LOCATION FILTER ----------------
    locations = ["All Locations"] + sorted(df["location"].unique().tolist())
    selected_location = st.selectbox("Select Location", locations)

    # ---------------- DATE FILTER ----------------
    min_date = df["timestamp"].min().date()
    max_date = df["timestamp"].max().date()

    selected_dates = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    # ---------------- ANOMALIES ONLY ----------------
    anomalies_only = st.toggle("Show anomalies only", value=False)

    if st.button("Reset all filters", **WIDTH_KW):
        for k in list(st.session_state.keys()):
            if k != "theme_choice":
                del st.session_state[k]
        st.rerun()


T = THEMES[st.session_state.theme_choice]


# ============================================================
# STYLING
# ============================================================

inject_css(
    f"""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"] {{
    font-family: Inter, "Segoe UI", Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
}}
.stApp {{ background: {T["bg"]}; color: {T["text"]}; color-scheme: {T["scheme"]}; }}
[data-testid="stAppViewContainer"] {{ background: {T["glow"]}, {T["bg"]}; }}
[data-testid="stHeader"] {{ background: transparent; }}
.block-container {{ padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1560px; }}
::-webkit-scrollbar {{ width: 10px; height: 10px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: {T["border"]}; border-radius: 10px; }}
::-webkit-scrollbar-thumb:hover {{ background: {T["muted"]}; }}
section[data-testid="stSidebar"] {{ background: {T["sidebar"]}; border-right: 1px solid {T["border"]}; }}
section[data-testid="stSidebar"] .block-container {{ padding-top: 1.6rem; }}
.brand {{ display: flex; align-items: center; gap: .8rem; padding: .2rem 0 1.1rem 0; }}
.brand-icon {{ font-size: 1.7rem; line-height: 1; filter: drop-shadow(0 0 10px {T["primary"]}66); }}
.brand-name {{ font-size: 1rem; font-weight: 900; letter-spacing: .07em; color: {T["text"]}; }}
.brand-sub {{ font-size: .77rem; color: {T["muted"]}; margin-top: .18rem; }}
.rule {{ height: 1px; background: linear-gradient(90deg,{T["border"]},transparent); margin: .9rem 0 1rem; }}
.side-label {{
    color: {T["muted"]}; font-size: .68rem; font-weight: 800;
    letter-spacing: .13em; text-transform: uppercase; margin: .9rem 0 .5rem;
}}
.hero {{
    background: {T["hero"]}; border: 1px solid {T["border"]}; border-radius: 20px;
    padding: 1.5rem 1.9rem; margin-bottom: 1.4rem; box-shadow: {T["shadow"]};
}}
.hero-title {{
    display: flex; align-items: center; gap: .6rem;
    font-size: clamp(1.35rem, 2.45vw, 2.25rem); font-weight: 800;
    letter-spacing: -.035em; color: {T["text"]}; margin: 0;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.hero-icon {{ font-size: .95em; flex-shrink: 0; filter: drop-shadow(0 0 12px {T["primary"]}55); }}
.hero-sub {{ font-size: .96rem; color: {T["muted"]}; margin-top: .5rem; line-height: 1.6; max-width: 950px; }}
.section-title {{
    display: flex; align-items: center; gap: .6rem; font-size: 1.24rem;
    font-weight: 800; color: {T["text"]}; letter-spacing: -.015em; margin: 1.7rem 0 .9rem;
}}
.section-title::before {{
    content: ""; width: 3px; height: 1.05em; border-radius: 3px; flex-shrink: 0;
    background: linear-gradient(180deg,{T["primary"]},{T["secondary"]});
}}
div[data-testid="stMetric"] {{
    background: {T["card"]}; border: 1px solid {T["border"]}; padding: 1rem 1.15rem;
    border-radius: 15px; box-shadow: {T["shadow"]}; min-height: 108px;
    position: relative; overflow: hidden;
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}}
div[data-testid="stMetric"]::before {{
    content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg,{T["primary"]},{T["secondary"]});
}}
div[data-testid="stMetric"]:hover {{
    transform: translateY(-3px); border-color: {T["primary"]}66; box-shadow: {T["shadow_hover"]};
}}
div[data-testid="stDataFrame"] {{
    border: 1px solid {T["border"]}; border-radius: 12px; overflow: hidden; box-shadow: {T["shadow"]};
}}
.js-plotly-plot {{
    border: 1px solid {T["border"]}; border-radius: 15px; overflow: hidden;
    box-shadow: {T["shadow"]}; background: {T["surface"]};
}}
div.stButton > button, div.stDownloadButton > button {{
    border-radius: 10px; font-weight: 600; border: 1px solid {T["border"]};
    background: {T["surface_2"]}; color: {T["text"]}; padding: .5rem 1.1rem; transition: all .18s ease;
}}
div.stButton > button:hover, div.stDownloadButton > button:hover {{
    border-color: {T["primary"]}; color: {T["primary"]};
    transform: translateY(-1px); box-shadow: {T["shadow_hover"]};
}}
div[data-baseweb="select"] > div, .stTextInput input, .stDateInput input {{
    background: {T["surface"]}; border-color: {T["border"]}; border-radius: 10px; color: {T["text"]};
}}
hr, [data-testid="stDivider"] {{ border-color: {T["border"]} !important; }}
.footer-box {{
    margin-top: 2rem; padding: 1rem 1.3rem; background: {T["card"]};
    border: 1px solid {T["border"]}; border-radius: 14px;
    color: {T["muted"]}; text-align: center; font-size: .85rem;
}}
/* ============================================================
   STREAMLIT INTERNAL TEXT OVERRIDES
   Streamlit colours its own widget labels, captions, tick marks
   and metric labels from config.toml. Those elements out-specify
   ordinary CSS, so under a runtime-switched dark theme they stay
   near-black and unreadable. Force them here.
   ============================================================ */
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label, [data-testid="stWidgetLabel"] div,
.stSelectbox label, .stDateInput label, .stTextInput label, .stSlider label {{
    color: {T["muted"]} !important; font-weight: 600 !important;
}}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li,
.stMarkdown p, .stMarkdown li {{ color: {T["text"]}; }}
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {{ color: {T["muted"]} !important; }}
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p, [data-testid="stMetricLabel"] div {{
    color: {T["muted"]} !important; font-size: .7rem !important; font-weight: 800 !important;
    letter-spacing: .1em; text-transform: uppercase;
}}
[data-testid="stMetricValue"], [data-testid="stMetricValue"] div {{
    color: {T["text"]} !important; font-size: 1.85rem !important; font-weight: 800 !important;
    letter-spacing: -.03em; font-variant-numeric: tabular-nums;
}}
[data-testid="stMetricDelta"], [data-testid="stMetricDelta"] div {{ color: {T["muted"]} !important; }}
[data-testid="stTickBarMin"], [data-testid="stTickBarMax"], [data-testid="stThumbValue"] {{
    color: {T["muted"]} !important;
}}
.stTextInput input::placeholder {{ color: {T["muted"]} !important; opacity: .8; }}
div[data-baseweb="select"] *, div[data-baseweb="select"] div {{ color: {T["text"]} !important; }}
div[data-baseweb="popover"] li, div[data-baseweb="menu"] li {{
    background: {T["surface"]} !important; color: {T["text"]} !important;
}}
div[data-baseweb="popover"] li:hover, div[data-baseweb="menu"] li:hover {{ background: {T["surface_2"]} !important; }}
div[data-baseweb="calendar"], div[data-baseweb="calendar"] * {{ color: {T["text"]} !important; }}
[data-testid="stAlert"] {{
    background: {T["surface_2"]} !important; border: 1px solid {T["border"]};
    border-radius: 12px; color: {T["text"]} !important;
}}
[data-testid="stAlert"] p, [data-testid="stAlert"] div {{ color: {T["text"]} !important; }}
[data-testid="stHeader"] button, [data-testid="stHeader"] svg,
[data-testid="stSidebarCollapseButton"] svg, [data-testid="stSidebarCollapsedControl"] svg {{
    color: {T["text"]} !important; fill: {T["text"]} !important;
}}
h1, h2, h3, h4, h5, h6 {{ color: {T["text"]} !important; }}
label[data-baseweb="checkbox"] div, label[data-baseweb="checkbox"] span {{ color: {T["text"]} !important; }}
@media (max-width: 1150px) {{
    .hero-title {{ white-space: normal; font-size: clamp(1.25rem, 4vw, 1.8rem); }}
}}
</style>
"""
)


# ============================================================
# CHART HELPERS
# ============================================================

# Severity keeps a fixed meaning everywhere: red is always worse than green.
RISK_COLORS = {
    "Critical": T["danger"],
    "High": T["danger"],
    "Medium": T["warning"],
    "Low": T["success"],
    "Minimal": T["info"],
}

CATEGORICAL = [
    T["primary"], T["secondary"], T["info"], T["warning"],
    T["success"], T["danger"], "#f472b6", "#2dd4bf",
]


def _supports(fn):
    try:
        fn()
        return True
    except Exception:
        return False


_ROUNDED = _supports(lambda: go.Bar(x=["a"], y=[1], marker=dict(cornerradius=6)))
BAR_MARKER = dict(cornerradius=6) if _ROUNDED else {}


def style_chart(fig, height=400, title=None, x_title=None, y_title=None, legend=False):
    fig.update_layout(
        height=height,
        title=dict(text=title, font=dict(size=15, color=T["text"]), x=0.015, y=0.96),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor=T["plot_bg"],
        font=dict(
            family='Inter, "Segoe UI", Arial, sans-serif',
            color=T["muted"],
            size=12,
        ),
        margin=dict(l=30, r=30, t=62, b=50),
        showlegend=legend,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.22, xanchor="center", x=0.5,
            bgcolor="rgba(0,0,0,0)", font=dict(color=T["muted"], size=11),
        ),
        hoverlabel=dict(
            bgcolor=T["surface_2"], bordercolor=T["border"],
            font=dict(color=T["text"], size=12),
        ),
        coloraxis_showscale=False,
        xaxis=dict(
            title=x_title, showgrid=False, linecolor=T["border"],
            tickfont=dict(color=T["muted"], size=11),
        ),
        yaxis=dict(
            title=y_title, showgrid=True, gridcolor=T["grid"], zeroline=False,
            linecolor=T["border"], tickfont=dict(color=T["muted"], size=11),
        ),
    )
    return fig


def hbar(data, label_col, value_col, title, color, x_title="Count", height=400):
    """Horizontal bars: usernames and IP addresses are too long for rotated labels."""
    d = data.sort_values(value_col, ascending=True).tail(10)
    fig = px.bar(
        d, x=value_col, y=label_col, orientation="h", text=value_col,
        color=value_col, color_continuous_scale=[[0, color + "66"], [1, color]],
    )
    fig.update_traces(
        marker_line_width=0, marker=BAR_MARKER,
        texttemplate="%{text:,}", textposition="outside",
        textfont=dict(size=11, color=T["muted"]), cliponaxis=False,
        hovertemplate="<b>%{y}</b><br>" + x_title + ": %{x:,}<extra></extra>",
    )
    style_chart(fig, height=height, title=title, x_title=x_title)
    fig.update_layout(
        yaxis=dict(showgrid=False, linecolor=T["border"],
                   tickfont=dict(color=T["text"], size=11), title=None),
        xaxis=dict(showgrid=True, gridcolor=T["grid"], zeroline=False,
                   linecolor=T["border"], tickfont=dict(color=T["muted"], size=11),
                   title=x_title),
        margin=dict(l=10, r=55, t=62, b=45),
    )
    return fig


def section(title):
    render_html(f'<div class="section-title">{title}</div>')


# ============================================================
# HEADER
# ============================================================

render_html(
    """
    <div class="hero">
    <div class="hero-title"><span class="hero-icon">🛡️</span><span>Authentication Anomaly Detection</span></div>
    <div class="hero-sub">Interactive cybersecurity dashboard for detecting and analyzing anomalous user behavior in authentication logs using AI and machine learning.</div>
    </div>
    """
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

if selected_user != "All Users":
    filtered_df = filtered_df[filtered_df["username"] == selected_user]

if selected_risk != "All Risk Levels":
    filtered_df = filtered_df[filtered_df["risk_level"] == selected_risk]

if selected_location != "All Locations":
    filtered_df = filtered_df[filtered_df["location"] == selected_location]

if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date = pd.to_datetime(selected_dates[0])
    end_date = (
        pd.to_datetime(selected_dates[1])
        + pd.Timedelta(days=1)
        - pd.Timedelta(seconds=1)
    )
    filtered_df = filtered_df[
        (filtered_df["timestamp"] >= start_date)
        & (filtered_df["timestamp"] <= end_date)
    ]

if anomalies_only:
    filtered_df = filtered_df[filtered_df["ai_is_anomaly"] == 1]


# ============================================================
# CHECK FILTERED DATA
# ============================================================

if filtered_df.empty:
    st.warning(
        "No records match the selected filters. Please change the filters."
    )
    st.stop()


# ============================================================
# KPI METRICS
# ============================================================

total_events = len(filtered_df)
total_anomalies = int(filtered_df["ai_is_anomaly"].sum())
normal_events = total_events - total_anomalies
anomaly_percentage = total_anomalies / total_events * 100
high_risk_events = len(filtered_df[filtered_df["risk_level"] == "High"])

baseline_rate = df["ai_is_anomaly"].sum() / len(df) * 100
rate_delta = anomaly_percentage - baseline_rate

failed_logins = (
    int((filtered_df["success"] == 0).sum())
    if "success" in filtered_df.columns
    else 0
)


section("📊 Security Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Events", f"{total_events:,}")

with col2:
    st.metric(
        "AI Anomalies",
        f"{total_anomalies:,}",
        delta=f"{total_anomalies / total_events * 100:.1f}% of view",
        delta_color="off",
    )

with col3:
    st.metric("Normal Events", f"{normal_events:,}")

with col4:
    st.metric(
        "Anomaly Rate",
        f"{anomaly_percentage:.2f}%",
        delta=f"{rate_delta:+.2f} pts vs all data",
        delta_color="inverse",
    )

with col5:
    st.metric("High Risk Events", f"{high_risk_events:,}")


# ============================================================
# ROW 1 - RISK LEVEL + AI PREDICTION
# ============================================================

section("🚨 Risk & Prediction Breakdown")

col1, col2 = st.columns(2)

with col1:
    risk_counts = filtered_df["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["risk_level", "count"]

    order = ["Critical", "High", "Medium", "Low", "Minimal"]
    risk_counts["_o"] = risk_counts["risk_level"].apply(
        lambda x: order.index(x) if x in order else 99
    )
    risk_counts = risk_counts.sort_values("_o")

    fig_risk = px.bar(
        risk_counts, x="risk_level", y="count", text="count",
        color="risk_level", color_discrete_map=RISK_COLORS,
    )
    fig_risk.update_traces(
        marker_line_width=0, marker=BAR_MARKER, width=0.55,
        texttemplate="%{text:,}", textposition="outside",
        textfont=dict(size=12, color=T["text"]), cliponaxis=False,
        hovertemplate="<b>%{x}</b><br>%{y:,} events<extra></extra>",
    )
    style_chart(
        fig_risk, height=400,
        title="Authentication Events by Risk Level",
        x_title="Risk Level", y_title="Number of Events",
    )
    fig_risk.update_layout(bargap=0.42)
    st.plotly_chart(fig_risk, **WIDTH_KW)

with col2:
    prediction_counts = filtered_df["ai_prediction"].value_counts().reset_index()
    prediction_counts.columns = ["prediction", "count"]

    pred_colors = {}
    for name in prediction_counts["prediction"]:
        low = str(name).lower()
        if any(k in low for k in ["anomal", "attack", "malic", "suspic"]):
            pred_colors[name] = T["danger"]
        else:
            pred_colors[name] = T["success"]

    fig_prediction = px.pie(
        prediction_counts, names="prediction", values="count",
        hole=0.66, color="prediction", color_discrete_map=pred_colors,
    )
    fig_prediction.update_traces(
        textinfo="percent", textfont=dict(size=13, color="#ffffff"),
        marker=dict(line=dict(color=T["surface"], width=3)),
        hovertemplate="<b>%{label}</b><br>%{value:,} events<br>%{percent}<extra></extra>",
    )
    fig_prediction.add_annotation(
        text=f"<b>{anomaly_percentage:.1f}%</b><br>"
        "<span style='font-size:11px'>anomalous</span>",
        x=0.5, y=0.5, font=dict(size=23, color=T["text"]), showarrow=False,
    )
    style_chart(fig_prediction, height=400, title="AI Normal vs Anomalous Events", legend=True)
    st.plotly_chart(fig_prediction, **WIDTH_KW)


# ============================================================
# ROW 2 - HOURLY ACTIVITY + ANOMALY SCORES
# ============================================================

section("🕒 Temporal Patterns")

col1, col2 = st.columns(2)

with col1:
    hourly = (
        filtered_df.groupby("login_hour")
        .agg(total=("login_hour", "size"), anomalies=("ai_is_anomaly", "sum"))
        .reset_index()
    )

    fig_hourly = go.Figure()
    fig_hourly.add_trace(
        go.Scatter(
            x=hourly["login_hour"], y=hourly["total"],
            mode="lines+markers", name="All events",
            line=dict(color=T["primary"], width=3, shape="spline"),
            marker=dict(size=7, color=T["primary"]),
            fill="tozeroy", fillcolor=T["primary"] + "26",
            hovertemplate="%{x}:00<br>%{y:,} events<extra></extra>",
        )
    )
    fig_hourly.add_trace(
        go.Scatter(
            x=hourly["login_hour"], y=hourly["anomalies"],
            mode="lines+markers", name="Anomalies",
            line=dict(color=T["danger"], width=3, shape="spline"),
            marker=dict(size=7, color=T["danger"]),
            fill="tozeroy", fillcolor=T["danger"] + "26",
            hovertemplate="%{x}:00<br>%{y:,} anomalies<extra></extra>",
        )
    )
    # Off-hours shading: 00:00-06:00 and 19:00-23:00 are where
    # unusual authentication activity most often shows up.
    for x0, x1 in [(-0.5, 6), (19, 23.5)]:
        fig_hourly.add_vrect(
            x0=x0, x1=x1, fillcolor=T["warning"], opacity=0.07,
            layer="below", line_width=0,
        )
    style_chart(
        fig_hourly, height=400, title="Authentication Activity by Hour",
        x_title="Hour of Day (shaded = off-hours)", y_title="Number of Events",
        legend=True,
    )
    st.plotly_chart(fig_hourly, **WIDTH_KW)

with col2:
    fig_scores = px.histogram(
        filtered_df, x="anomaly_score", nbins=34,
        color="ai_is_anomaly",
        color_discrete_map={0: T["success"], 1: T["danger"]},
    )
    fig_scores.update_traces(
        marker_line_width=0, marker=BAR_MARKER, opacity=0.85,
        hovertemplate="Score %{x:.3f}<br>%{y:,} events<extra></extra>",
    )
    style_chart(
        fig_scores, height=400, title="Distribution of AI Anomaly Scores",
        x_title="Anomaly Score (lower = more anomalous)",
        y_title="Number of Events", legend=True,
    )
    fig_scores.update_layout(barmode="overlay", bargap=0.05)
    for tr, name in zip(fig_scores.data, ["Normal", "Anomaly"]):
        tr.name = name
    st.plotly_chart(fig_scores, **WIDTH_KW)


# ============================================================
# ROW 2b - WEEKDAY x HOUR HEATMAP
# ============================================================

heat = filtered_df.copy()
heat["day_name"] = heat["timestamp"].dt.day_name().str[:3]
heat_pivot = (
    heat.pivot_table(
        index="day_name", columns="login_hour",
        values="ai_is_anomaly", aggfunc="sum", fill_value=0,
    )
    .reindex([d for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
              if d in heat["day_name"].unique()])
)

if not heat_pivot.empty and heat_pivot.to_numpy().sum() > 0:
    fig_heat = px.imshow(
        heat_pivot, aspect="auto",
        color_continuous_scale=[
            [0.0, T["surface_2"]], [0.35, T["info"]],
            [0.7, T["warning"]], [1.0, T["danger"]],
        ],
        labels=dict(x="Hour of Day", y="Day", color="Anomalies"),
    )
    fig_heat.update_traces(
        hovertemplate="%{y} at %{x}:00<br>%{z:,} anomalies<extra></extra>"
    )
    style_chart(
        fig_heat, height=290,
        title="Anomaly Concentration — Day of Week vs Hour",
        x_title="Hour of Day", y_title=None,
    )
    fig_heat.update_layout(coloraxis_showscale=True, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_heat, **WIDTH_KW)


# ============================================================
# ROW 3 - SUSPICIOUS USERS + IP ADDRESSES
# ============================================================

anomalies_df = filtered_df[filtered_df["ai_is_anomaly"] == 1].copy()

section("🎯 Top Risk Entities")

col1, col2 = st.columns(2)

with col1:
    if not anomalies_df.empty:
        suspicious_users = (
            anomalies_df.groupby("username").size()
            .reset_index(name="anomaly_count")
            .sort_values("anomaly_count", ascending=False).head(10)
        )
        st.plotly_chart(
            hbar(suspicious_users, "username", "anomaly_count",
                 "👤 Top Users with AI-Detected Anomalies",
                 T["secondary"], "Anomalies"),
            **WIDTH_KW,
        )
    else:
        st.info("No AI-detected anomalies found for the selected filters.")

with col2:
    if not anomalies_df.empty:
        suspicious_ips = (
            anomalies_df.groupby("ip_address").size()
            .reset_index(name="anomaly_count")
            .sort_values("anomaly_count", ascending=False).head(10)
        )
        st.plotly_chart(
            hbar(suspicious_ips, "ip_address", "anomaly_count",
                 "🌐 Top IP Addresses with Anomalies",
                 T["info"], "Anomalies"),
            **WIDTH_KW,
        )
    else:
        st.info("No suspicious IP addresses found for the selected filters.")


# ============================================================
# ROW 4 - LOCATIONS + LOGIN OUTCOME
# ============================================================

col1, col2 = st.columns(2)

with col1:
    if not anomalies_df.empty:
        suspicious_locations = (
            anomalies_df.groupby("location").size()
            .reset_index(name="anomaly_count")
            .sort_values("anomaly_count", ascending=False)
        )
        st.plotly_chart(
            hbar(suspicious_locations, "location", "anomaly_count",
                 "📍 Anomalies by Location", T["warning"], "Anomalies"),
            **WIDTH_KW,
        )
    else:
        st.info("No anomalous locations found for the selected filters.")

with col2:
    login_status = filtered_df.groupby("success").size().reset_index(name="count")
    login_status["login_status"] = login_status["success"].map(
        {1: "Successful Login", 0: "Failed Login"}
    )

    fig_status = px.bar(
        login_status, x="login_status", y="count", text="count",
        color="login_status",
        color_discrete_map={
            "Successful Login": T["success"],
            "Failed Login": T["danger"],
        },
    )
    fig_status.update_traces(
        marker_line_width=0, marker=BAR_MARKER, width=0.45,
        texttemplate="%{text:,}", textposition="outside",
        textfont=dict(size=12, color=T["text"]), cliponaxis=False,
        hovertemplate="<b>%{x}</b><br>%{y:,} events<extra></extra>",
    )
    style_chart(
        fig_status, height=400,
        title="🔐 Authentication Success and Failure",
        x_title="Login Status", y_title="Number of Events",
    )
    fig_status.update_layout(bargap=0.5)
    st.plotly_chart(fig_status, **WIDTH_KW)


# ============================================================
# SUSPICIOUS EVENTS TABLE
# ============================================================

section("🚨 Most Suspicious Authentication Events")

# Isolation Forest returns lower scores for more anomalous points,
# so ascending order puts the highest-risk events first.
row_count = st.slider("Number of events to display", 10, 100, 25, 5)

suspicious_events = filtered_df.sort_values("anomaly_score", ascending=True).head(row_count)

display_columns = [
    "event_id", "timestamp", "username", "ip_address", "location",
    "device", "success", "is_anomaly", "ai_is_anomaly",
    "anomaly_score", "risk_level",
]
available_columns = [c for c in display_columns if c in suspicious_events.columns]

st.dataframe(suspicious_events[available_columns], height=430, **WIDTH_KW)

st.caption(
    f"Showing the {row_count} lowest-scoring events out of "
    f"{total_events:,} in the current filter."
)


# ============================================================
# DOWNLOAD FILTERED RESULTS
# ============================================================

section("📥 Download Filtered Results")

dl1, dl2 = st.columns(2)

with dl1:
    st.download_button(
        label="⬇️ Download all filtered results (CSV)",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_authentication_results.csv",
        mime="text/csv",
        **WIDTH_KW,
    )

with dl2:
    if not anomalies_df.empty:
        st.download_button(
            label="⬇️ Download anomalies only (CSV)",
            data=anomalies_df.to_csv(index=False).encode("utf-8"),
            file_name="detected_anomalies.csv",
            mime="text/csv",
            **WIDTH_KW,
        )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="footer-box">
    🛡️ <b>Anomalous User Behavior in Authentication Logs</b>
    &nbsp;|&nbsp; AI + Machine Learning + SQL + Python + Streamlit
    </div>
    """
)
