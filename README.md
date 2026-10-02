# 🔐 Anomalous User Behavior in Authentication Logs

## 📌 Project Overview

This project is a cybersecurity and behavioral analytics solution designed to detect anomalous user activity in authentication logs.

The system simulates authentication events, stores and analyzes data using SQL, performs feature engineering with Python, applies machine learning for anomaly detection, and presents the results through an interactive Streamlit dashboard.

The project demonstrates an end-to-end cybersecurity data analytics workflow combining:

- 🐍 Python
- 🗄️ SQL / SQLite
- 🤖 Artificial Intelligence and Machine Learning
- 📊 Interactive Dashboard Development
- 🔐 Cybersecurity Analytics
- 📈 Data Visualization

---

# 🎯 Project Objective

The objective of this project is to identify unusual authentication behavior that may indicate potential security risks.

Examples of suspicious behavior include:

- Unusual login times
- Abnormal login frequency
- Login activity from unexpected locations
- Multiple devices used by the same user
- Failed authentication attempts
- Behavioral patterns that differ from normal user activity

The project uses machine learning to analyze multiple behavioral features together and identify potentially anomalous events.

---

# 🏗️ Project Architecture

```text
Authentication Logs
        │
        ▼
Python Dataset Generation
        │
        ▼
Raw Authentication Dataset
        │
        ▼
SQL / SQLite Database Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Anomaly Detection
        │
        ▼
Anomaly Detection Results
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🛠️ Technologies Used

## Python

Python is used for:

- Data generation
- Data processing
- Database interaction
- Feature engineering
- Machine learning
- Anomaly detection
- Dashboard development

## SQL / SQLite

SQLite is used to:

- Store authentication log data
- Perform SQL-based analysis
- Analyze user behavior
- Identify patterns in authentication activity

## Artificial Intelligence / Machine Learning

The project uses machine learning for anomaly detection.

### Isolation Forest

Isolation Forest is used to identify unusual authentication events based on behavioral features.

The model isolates observations that differ significantly from normal activity.

Outputs include:

- Normal events
- Anomalous events
- Anomaly predictions
- Anomaly scores
- High-risk activity indicators

## Streamlit Dashboard

Streamlit is used to create an interactive cybersecurity dashboard.

The dashboard provides:

- Security overview metrics
- Total authentication events
- AI-detected anomalies
- Normal events
- Anomaly rate
- High-risk events
- User filtering
- Risk-level filtering
- Location filtering
- Date filtering
- Interactive visualizations

---

# 📂 Project Structure

```text
Anomalous_User_Behavior/
│
├── data/
│   ├── raw/
│   │   └── authentication_logs.csv
│   │
│   └── processed/
│       ├── authentication_features.csv
│       └── anomaly_detection_results.csv
│
├── database/
│   └── authentication.db
│
├── documentation/
│   ├── 01_project_overview.md
│   ├── 02_project_architecture.md
│   ├── 03_sql_database_analysis.md
│   ├── 04_feature_engineering.md
│   ├── 05_ai_ml_anomaly_detection.md
│   ├── 06_dashboard.md
│   ├── 07_project_findings.md
│   └── project_documentation.md
│
├── outputs/
│   ├── charts/
│   └── models/
│       ├── isolation_forest_model.pkl
│       └── feature_scaler.pkl
│
├── src/
│   ├── 01_create_dataset.py
│   ├── 02_database_analysis.py
│   ├── 03_feature_engineering.py
│   ├── 04_anomaly_detection.py
│   └── 05_dashboard.py
│
├── README.md
└── requirements.txt
```

---

# 🔄 Project Workflow

## Step 1: Create Authentication Dataset

The first stage creates a simulated authentication dataset containing user login activity.

The dataset includes information such as:

- Event ID
- Timestamp
- Username
- IP address
- Location
- Device
- Login hour
- Authentication success status
- Anomaly indicators

Run:

```powershell
python src/01_create_dataset.py
```

---

## Step 2: SQL Database Analysis

The authentication dataset is loaded into SQLite for structured database analysis.

SQL queries are used to analyze:

- Authentication activity
- User login frequency
- Successful and failed logins
- Location activity
- User-based anomalies
- Behavioral patterns

Run:

```powershell
python src/02_database_analysis.py
```

---

## Step 3: Feature Engineering

Raw authentication data is transformed into machine-learning features.

Feature engineering creates behavioral signals that help the machine learning model identify unusual activity.

Examples include:

- Login time patterns
- User activity frequency
- Device-related behavior
- Location-related behavior
- Authentication behavior
- Encoded categorical features

Run:

```powershell
python src/03_feature_engineering.py
```

---

## Step 4: AI / ML Anomaly Detection

The engineered features are analyzed using an Isolation Forest machine learning model.

The model identifies authentication events that differ from normal behavioral patterns.

The script produces:

- Anomaly predictions
- Anomaly scores
- Processed anomaly results
- Trained Isolation Forest model
- Feature scaler

Run:

```powershell
python src/04_anomaly_detection.py
```

The trained model is saved to:

```text
outputs/models/isolation_forest_model.pkl
```

The feature scaler is saved to:

```text
outputs/models/feature_scaler.pkl
```

---

## Step 5: Interactive Dashboard

The final results are displayed through an interactive Streamlit cybersecurity dashboard.

Run:

```powershell
streamlit run src/05_dashboard.py
```

The dashboard includes interactive filters for:

- User
- Risk level
- Location
- Date range

It also displays security metrics and visualizations based on the anomaly detection results.

---

# 📊 Key Results

The completed pipeline processes authentication events and separates them into normal and potentially anomalous behavior.

In the current project dataset:

- Total Events: 1,000
- AI Anomalies Detected: 50
- Normal Events: 950
- Anomaly Rate: 5%
- High-Risk Events: 50

These results demonstrate how behavioral analytics and machine learning can be used to identify potentially suspicious authentication activity.

---

# 🤖 AI Components

This project incorporates multiple AI and analytical concepts:

### 1. Machine Learning Anomaly Detection

Isolation Forest is used as an unsupervised machine learning algorithm to identify unusual authentication events.

### 2. Behavioral Analytics

Authentication events are analyzed using multiple behavioral features rather than relying on a single security rule.

### 3. Risk Classification

Anomaly results are used to identify potentially high-risk authentication events.

### 4. Feature-Based Intelligence

Raw authentication logs are transformed into structured behavioral features for machine learning analysis.

---

# 🗄️ SQL Components

The SQL/database portion of the project demonstrates:

- Database creation
- Data storage
- SQL queries
- Aggregation
- User activity analysis
- Authentication analysis
- Behavioral pattern analysis

This ensures that the project includes both database analytics and machine learning workflows.

---

# 🚀 How to Run the Complete Project

## 1. Clone or download the project

Navigate to the project directory:

```powershell
cd Anomalous-User-Behavior-Detection
```

## 2. Create and activate a virtual environment

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate
```

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 4. Run the pipeline

```powershell
python src/01_create_dataset.py
python src/02_database_analysis.py
python src/03_feature_engineering.py
python src/04_anomaly_detection.py
```

## 5. Start the dashboard

```powershell
streamlit run src/05_dashboard.py
```

---

# 🔮 Future Improvements

Potential future enhancements include:

- Real-time authentication log ingestion
- Integration with SIEM platforms
- Live API-based data collection
- Additional anomaly detection models
- Deep learning-based behavioral analysis
- User behavior baselines
- Alert notifications
- Email or Slack security alerts
- Role-based dashboard access
- Threat intelligence integration
- Model comparison and performance monitoring

---

# 🧠 Skills Demonstrated

This project demonstrates practical skills in:

- Python programming
- Pandas and NumPy
- SQL and SQLite
- Data engineering
- Feature engineering
- Machine learning
- Isolation Forest
- Cybersecurity analytics
- Behavioral analysis
- Anomaly detection
- Data visualization
- Streamlit dashboard development
- Model persistence
- End-to-end project development

---

# ✅ Project Status

**Core project pipeline completed successfully.**

The project includes:

- ✅ Python
- ✅ SQL / Database Analysis
- ✅ Feature Engineering
- ✅ Artificial Intelligence / Machine Learning
- ✅ Isolation Forest Anomaly Detection
- ✅ Saved ML Model
- ✅ Processed Results
- ✅ Interactive Dashboard
- ✅ Cybersecurity Analytics
- ✅ Project Documentation

---

## 🔐 Final Summary

This project demonstrates an end-to-end approach to detecting anomalous user behavior in authentication logs.

By combining Python, SQL, feature engineering, machine learning, and an interactive dashboard, the system transforms raw authentication events into meaningful security insights.

The solution provides a foundation for future development into a more advanced authentication monitoring and behavioral analytics platform.