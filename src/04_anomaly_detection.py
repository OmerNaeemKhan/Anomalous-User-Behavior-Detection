import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


# ============================================================
# PATH CONFIGURATION
# ============================================================

INPUT_FILE = "data/processed/authentication_features.csv"

OUTPUT_FILE = "data/processed/anomaly_detection_results.csv"

MODEL_FILE = "outputs/models/isolation_forest_model.pkl"

SCALER_FILE = "outputs/models/feature_scaler.pkl"


# ============================================================
# SELECT FEATURES FOR MACHINE LEARNING
# ============================================================

FEATURE_COLUMNS = [
    "login_hour",
    "day_of_week",
    "is_weekend",
    "is_night_login",
    "failed_login",
    "successful_login",
    "user_login_count",
    "user_failed_login_count",
    "user_failed_login_rate",
    "ip_login_count",
    "ip_unique_users",
    "device_login_count",
    "device_unique_users",
    "location_login_count",
    "location_unique_users",
    "user_ip_count",
    "user_device_count",
    "user_location_count",
]


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print("=" * 60)
    print("AI-BASED ANOMALY DETECTION")
    print("=" * 60)

    # --------------------------------------------------------
    # CHECK INPUT FILE
    # --------------------------------------------------------

    if not os.path.exists(INPUT_FILE):
        print(f"\nERROR: Input file not found: {INPUT_FILE}")
        return

    # --------------------------------------------------------
    # LOAD PROCESSED DATA
    # --------------------------------------------------------

    print(f"\nLoading processed data from: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print(f"Records loaded: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    # --------------------------------------------------------
    # CHECK REQUIRED FEATURES
    # --------------------------------------------------------

    missing_features = [
        feature
        for feature in FEATURE_COLUMNS
        if feature not in df.columns
    ]

    if missing_features:
        print("\nERROR: The following required features are missing:")
        for feature in missing_features:
            print(f"- {feature}")
        return

    # --------------------------------------------------------
    # PREPARE MACHINE LEARNING DATA
    # --------------------------------------------------------

    print("\nPreparing features for the AI model...")

    X = df[FEATURE_COLUMNS].copy()

    # Replace missing values if any exist
    X = X.fillna(0)

    print(f"Number of AI features: {len(FEATURE_COLUMNS)}")

    # --------------------------------------------------------
    # SCALE FEATURES
    # --------------------------------------------------------

    print("\nScaling features...")

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    # --------------------------------------------------------
    # CREATE ISOLATION FOREST MODEL
    # --------------------------------------------------------

    print("\nTraining Isolation Forest anomaly detection model...")

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    )

    model.fit(X_scaled)

    # --------------------------------------------------------
    # GENERATE PREDICTIONS
    # --------------------------------------------------------

    print("\nGenerating anomaly predictions...")

    predictions = model.predict(X_scaled)

    anomaly_scores = model.decision_function(X_scaled)

    # Isolation Forest:
    #  1  = Normal
    # -1  = Anomaly

    df["ai_prediction_raw"] = predictions

    df["ai_is_anomaly"] = (
        df["ai_prediction_raw"] == -1
    ).astype(int)

    # Lower score = more suspicious
    df["anomaly_score"] = anomaly_scores

    # Create a readable prediction label
    df["ai_prediction"] = df["ai_is_anomaly"].map({
        0: "Normal",
        1: "Anomaly"
    })

    # --------------------------------------------------------
    # CREATE RISK LEVEL
    # --------------------------------------------------------

    df["risk_level"] = "Low"

    # Medium risk for suspicious scores
    df.loc[
        df["anomaly_score"] < 0.05,
        "risk_level"
    ] = "Medium"

    # High risk for AI-detected anomalies
    df.loc[
        df["ai_is_anomaly"] == 1,
        "risk_level"
    ] = "High"

    # --------------------------------------------------------
    # COMPARE WITH ORIGINAL LABEL
    # --------------------------------------------------------

    if "is_anomaly" in df.columns:

        print("\nComparing AI predictions with original anomaly labels...")

        comparison = pd.crosstab(
            df["is_anomaly"],
            df["ai_is_anomaly"],
            rownames=["Actual"],
            colnames=["AI Prediction"]
        )

        print("\nComparison Table:")
        print(comparison)

        matches = (
            df["is_anomaly"] == df["ai_is_anomaly"]
        ).sum()

        accuracy = matches / len(df) * 100

        print(f"\nPrediction agreement: {accuracy:.2f}%")

    # --------------------------------------------------------
    # SHOW RESULTS
    # --------------------------------------------------------

    total_anomalies = df["ai_is_anomaly"].sum()

    total_normal = (
        len(df) - total_anomalies
    )

    print("\n" + "-" * 60)
    print("AI ANOMALY DETECTION RESULTS")
    print("-" * 60)

    print(f"\nTotal records: {len(df)}")
    print(f"Normal events: {total_normal}")
    print(f"AI detected anomalies: {total_anomalies}")
    print(
        f"Anomaly percentage: "
        f"{(total_anomalies / len(df) * 100):.2f}%"
    )

    # --------------------------------------------------------
    # DISPLAY MOST SUSPICIOUS EVENTS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("TOP 10 MOST SUSPICIOUS EVENTS")
    print("-" * 60)

    suspicious_columns = [
        "event_id",
        "timestamp",
        "username",
        "ip_address",
        "location",
        "device",
        "success",
        "is_anomaly",
        "ai_is_anomaly",
        "anomaly_score",
        "risk_level",
    ]

    available_columns = [
        column
        for column in suspicious_columns
        if column in df.columns
    ]

    most_suspicious = df.sort_values(
        "anomaly_score",
        ascending=True
    ).head(10)

    print(
        most_suspicious[available_columns].to_string(
            index=False
        )
    )

    # --------------------------------------------------------
    # CREATE OUTPUT DIRECTORIES
    # --------------------------------------------------------

    os.makedirs(
        os.path.dirname(OUTPUT_FILE),
        exist_ok=True
    )

    os.makedirs(
        os.path.dirname(MODEL_FILE),
        exist_ok=True
    )

    # --------------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------------

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"\nResults saved to: {OUTPUT_FILE}")

    # --------------------------------------------------------
    # SAVE AI MODEL
    # --------------------------------------------------------

    joblib.dump(
        model,
        MODEL_FILE
    )

    print(f"Model saved to: {MODEL_FILE}")

    # --------------------------------------------------------
    # SAVE FEATURE SCALER
    # --------------------------------------------------------

    joblib.dump(
        scaler,
        SCALER_FILE
    )

    print(f"Feature scaler saved to: {SCALER_FILE}")

    # --------------------------------------------------------
    # COMPLETION MESSAGE
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("AI ANOMALY DETECTION COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()