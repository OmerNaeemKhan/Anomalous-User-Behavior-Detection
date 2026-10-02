# Project Architecture

## Anomalous User Behavior in Authentication Logs

---

# 1. Architecture Overview

This project uses an end-to-end cybersecurity analytics architecture that combines:

- Python
- SQL and SQLite
- Feature Engineering
- Artificial Intelligence
- Machine Learning
- Anomaly Detection
- Risk Classification
- Interactive Dashboard
- Data Visualization

The purpose of the architecture is to transform raw authentication events into actionable cybersecurity insights.

The complete workflow moves through multiple stages, beginning with raw authentication data and ending with AI-driven anomaly detection and interactive security monitoring.

---

# 2. High-Level Architecture

```text
┌───────────────────────────────────────┐
│       AUTHENTICATION DATA SOURCE      │
│                                       │
│  Simulated Authentication Log Events  │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│            PYTHON DATA PIPELINE       │
│                                       │
│      01_create_dataset.py             │
│                                       │
│  Generates authentication log data    │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│             RAW DATA LAYER            │
│                                       │
│ authentication_logs.csv               │
│                                       │
│ Event ID                              │
│ Timestamp                             │
│ Username                              │
│ IP Address                            │
│ Location                              │
│ Device                                │
│ Login Success                         │
│ Anomaly Label                         │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│          SQL DATABASE LAYER           │
│                                       │
│        SQLite Authentication DB       │
│                                       │
│ authentication_logs table             │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│           SQL SECURITY ANALYSIS       │
│                                       │
│      02_database_analysis.py          │
│                                       │
│  • User activity analysis             │
│  • Login success analysis             │
│  • Failed login analysis              │
│  • Anomaly summaries                  │
│  • Suspicious user analysis           │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│         FEATURE ENGINEERING           │
│                                       │
│      03_feature_engineering.py        │
│                                       │
│ Converts raw logs into behavioral     │
│ and cybersecurity-focused features    │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│          PROCESSED DATA LAYER         │
│                                       │
│ authentication_features.csv           │
│                                       │
│ 27 Total Data Columns                 │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│        AI / MACHINE LEARNING LAYER    │
│                                       │
│      04_anomaly_detection.py          │
│                                       │
│  Feature Scaling                      │
│          ↓                            │
│  Isolation Forest                     │
│          ↓                            │
│  AI Anomaly Prediction                │
│          ↓                            │
│  Anomaly Scoring                      │
│          ↓                            │
│  Risk Classification                  │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│             OUTPUT LAYER              │
│                                       │
│ anomaly_detection_results.csv         │
│ isolation_forest_model.pkl            │
│ feature_scaler.pkl                    │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│       INTERACTIVE SECURITY DASHBOARD  │
│                                       │
│         Streamlit + Plotly            │
│                                       │
│      05_dashboard.py                  │
│                                       │
│  Security KPIs                        │
│  Risk Analysis                        │
│  AI Anomaly Visualization             │
│  User Analysis                        │
│  IP Analysis                          │
│  Location Analysis                    │
│  Interactive Filters                  │
│  Suspicious Event Investigation       │
└───────────────────────────────────────┘

Python
  │
  ▼
Dataset Generation
  │
  ▼
Raw Authentication Logs
  │
  ▼
SQL / SQLite Database
  │
  ▼
SQL Security Analysis
  │
  ▼
Python Feature Engineering
  │
  ▼
AI / Machine Learning
  │
  ├── Feature Scaling
  │
  ├── Isolation Forest
  │
  ├── Anomaly Prediction
  │
  ├── Anomaly Score
  │
  └── Risk Classification
  │
  ▼
Processed Detection Results
  │
  ▼
Interactive Dashboard
  │
  ▼
Cybersecurity Investigation

4. Python Architecture

Python is the main technology connecting every stage of the project.

The project currently contains the following Python pipeline:

Script	Purpose
01_create_dataset.py	Creates the authentication dataset
02_database_analysis.py	Loads and analyzes authentication data using SQLite and SQL
03_feature_engineering.py	Creates behavioral features from raw authentication events
04_anomaly_detection.py	Performs AI/ML anomaly detection and risk scoring
05_dashboard.py	Displays results in an interactive cybersecurity dashboard

Python is responsible for:

Data generation
Data loading
Data transformation
Database interaction
SQL execution
Feature engineering
Machine learning preparation
Feature scaling
AI anomaly detection
Risk scoring
Model saving
Result saving
Dashboard development
5. SQL Database Architecture

The project uses SQLite as its database layer.

Database file:

database/authentication.db

Main table:

authentication_logs

The authentication data is loaded from the raw CSV file into SQLite.

SQL is then used to investigate authentication behavior.

Current SQL analysis includes:

Total authentication event counts
User activity counts
Login success analysis
Anomaly summaries
Anomalous activity by user

The SQL layer demonstrates how authentication events can be stored and queried in a structured cybersecurity investigation environment.

6. Feature Engineering Architecture

Raw authentication events do not directly contain all the behavioral information required for anomaly detection.

Feature engineering transforms the raw data into additional indicators.

The feature engineering process includes the following categories.

Time-Based Features
login_hour
day_of_week
day_name
is_weekend
is_night_login

These features help identify unusual authentication timing.

Login Status Features
failed_login
successful_login

These features help distinguish successful and failed authentication activity.

User Behavior Features
user_login_count
user_failed_login_count
user_failed_login_rate

These features summarize user authentication behavior.

IP Address Features
ip_login_count
ip_unique_users

These features measure IP address activity and sharing.

Device Features
device_login_count
device_unique_users

These features identify device usage patterns.

Location Features
location_login_count
location_unique_users

These features support geographic and location-based analysis.

Behavioral Combination Features
user_ip_count
user_device_count
user_location_count

These features analyze repeated relationships between users and authentication contexts.

7. AI and Machine Learning Architecture

The current AI/ML pipeline uses multiple stages.

Stage 1: Feature Selection

The anomaly detection model receives engineered numerical features representing authentication behavior.

These include time, login, user, IP, device, location, and behavioral frequency features.

Stage 2: Feature Scaling

A StandardScaler is used to normalize numerical feature values before training the anomaly detection model.

The scaler is saved as:

outputs/models/feature_scaler.pkl
Stage 3: Isolation Forest

The project uses the Isolation Forest machine learning algorithm.

Isolation Forest is an unsupervised anomaly detection algorithm.

It works by identifying records that are easier to isolate from the overall dataset.

The model produces:

Normal predictions
Anomalous predictions
Anomaly scores

The trained model is saved as:

outputs/models/isolation_forest_model.pkl
Stage 4: AI Prediction

The model generates a prediction for each authentication event.

The raw Isolation Forest prediction is converted into:

0 = Normal
1 = Anomaly

A readable label is also created:

Normal
Anomaly
Stage 5: Anomaly Scoring

Each event receives an anomaly score.

Lower scores indicate more unusual behavior.

These scores allow events to be ranked from most suspicious to least suspicious.

Stage 6: Risk Classification

Authentication events are classified into risk levels:

Low
Medium
High

AI-detected anomalies are classified as high risk.

This provides an additional security investigation layer between raw machine learning output and dashboard visualization.

8. AI Component Structure

The current project contains the following AI/ML components:

AI / ML Pipeline
│
├── Behavioral Feature Engineering
│
├── Feature Scaling
│
├── Unsupervised Machine Learning
│     │
│     └── Isolation Forest
│
├── AI Anomaly Prediction
│
├── Continuous Anomaly Scoring
│
├── Risk Classification
│
└── Model Persistence
      │
      ├── Saved ML Model
      └── Saved Feature Scaler

This gives the project a complete machine learning workflow rather than only displaying predefined anomaly rules.

9. Dashboard Architecture

The interactive dashboard is built with:

Streamlit
Plotly
Pandas
Python

The dashboard reads:

data/processed/anomaly_detection_results.csv

The dashboard provides an investigation interface for authentication events and AI results.

Dashboard Filters

Users can filter the dashboard by:

Username
Risk level
Location
Date range

The filters update the visible metrics, charts, and event data.

Dashboard KPIs

The dashboard displays:

Total authentication events
AI-detected anomalies
Normal events
Anomaly rate
High-risk events
Dashboard Visualizations

The dashboard includes analysis for:

Risk level distribution
AI prediction distribution
Login activity by hour
Anomaly score distribution
Most suspicious users
Most suspicious IP addresses
Anomalies by location
Login success versus failure
Most suspicious authentication events
10. End-to-End Data Flow
01_create_dataset.py
        │
        ▼
authentication_logs.csv
        │
        ├───────────────────────────────┐
        ▼                               │
02_database_analysis.py                 │
        │                               │
        ▼                               │
authentication.db                       │
                                        │
03_feature_engineering.py ◄─────────────┘
        │
        ▼
authentication_features.csv
        │
        ▼
04_anomaly_detection.py
        │
        ├──────────────┬───────────────┐
        ▼              ▼               ▼
AI Results        ML Model          Scaler
        │
        ▼
anomaly_detection_results.csv
        │
        ▼
05_dashboard.py
        │
        ▼
Interactive Cybersecurity Dashboard
11. Technology Integration

The architecture intentionally integrates multiple technologies.

Python

Python provides the automation and analytics layer.

SQL

SQL provides structured authentication log storage and investigation capabilities.

Feature Engineering

Feature engineering converts raw authentication logs into measurable behavioral indicators.

Artificial Intelligence

AI analyzes authentication behavior to identify unusual patterns.

Machine Learning

Isolation Forest performs unsupervised anomaly detection.

Dashboard

The dashboard presents security information in an interactive format.

Together, these components create an end-to-end cybersecurity analytics workflow.

12. Current Architecture Summary

The project currently demonstrates:

                 ┌──────────────┐
                 │    PYTHON    │
                 │ Main Pipeline│
                 └──────┬───────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
      RAW DATA         SQL         FEATURES
         │              │              │
         └──────────────┼──────────────┘
                        ▼
                 AI / MACHINE LEARNING
                        │
               ┌────────┼────────┐
               ▼        ▼        ▼
           Scaling   Detection  Scoring
                        │
                        ▼
                   Risk Levels
                        │
                        ▼
                    DASHBOARD
                        │
                        ▼
              CYBERSECURITY INSIGHTS
13. Future Architecture Enhancements

Future versions of the project can expand the AI layer with additional models and analysis techniques.

Potential enhancements include:

Local Outlier Factor (LOF)
One-Class SVM
K-Means clustering for behavioral segmentation
Autoencoder-based anomaly detection
Rule-based detection engine
Hybrid AI risk scoring
Ensemble anomaly detection
Explainable AI for anomaly decisions
Natural language AI summaries for security analysts

These future additions would allow multiple AI techniques to be compared and combined into a more advanced hybrid detection system.

Conclusion

The project architecture demonstrates an integrated cybersecurity analytics system.

The workflow combines:

Python → SQL → Feature Engineering → AI/ML → Risk Scoring → Dashboard

This architecture ensures that the project visibly demonstrates Python development, SQL analysis, AI and machine learning, and interactive dashboard development as connected components of one end-to-end cybersecurity solution.


Save it with **Ctrl + S**.

After that, create the next file:

```text
documentation/03_sql_database_analysis.md