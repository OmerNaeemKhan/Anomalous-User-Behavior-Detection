# AI and Machine Learning Anomaly Detection

## Anomalous User Behavior in Authentication Logs

---

# 1. Overview

The Artificial Intelligence and Machine Learning component is responsible for identifying authentication events that differ from normal behavioral patterns.

Traditional security monitoring often depends on manually created rules. For example:

- More than 5 failed logins
- Login outside business hours
- Login from an unusual location
- Login from a new device

These rules can be useful, but they may miss unusual combinations of behavior.

This project adds an AI and Machine Learning layer that evaluates multiple behavioral features together and identifies events that appear statistically different from the overall authentication activity.

The main AI/ML script is:

```text
src/04_anomaly_detection.py

The workflow uses Python and Scikit-learn to process engineered authentication features, scale numerical data, train an anomaly detection model, generate anomaly predictions, calculate anomaly scores, and assign risk levels.

2. AI/ML Pipeline Overview

The complete anomaly detection workflow is:

Processed Authentication Features
        │
        ▼
Feature Selection
        │
        ▼
Data Validation
        │
        ▼
Feature Scaling
        │
        ▼
Isolation Forest Model
        │
        ▼
Anomaly Prediction
        │
        ▼
Anomaly Scoring
        │
        ▼
Risk Classification
        │
        ▼
Saved Results
        │
        ▼
Interactive Dashboard

This creates a complete machine learning pipeline rather than using only static security rules.

3. Input Dataset

The AI/ML stage reads the processed authentication dataset created during feature engineering.

Input file:

data/processed/authentication_features.csv

The feature engineering process preserves the original authentication information while adding behavioral indicators.

The processed dataset contains:

1,000 authentication records
27 total columns

The AI model uses selected numerical features from this dataset to identify unusual authentication behavior.

4. AI/ML Technologies Used

The anomaly detection pipeline uses:

Python
Pandas
NumPy
Scikit-learn
Joblib

Python is used to automate the entire workflow.

Pandas and NumPy are used for data processing.

Scikit-learn provides the machine learning tools used for feature scaling and anomaly detection.

Joblib is used to save trained machine learning components for future reuse.

5. Machine Learning Problem Type

The project uses unsupervised anomaly detection.

Unlike traditional supervised machine learning, the model does not require a complete set of manually verified malicious and normal authentication examples for every prediction.

Instead, the model analyzes the structure of the available data and identifies events that differ significantly from the majority of authentication activity.

The objective is:

Learn normal behavioral patterns
        │
        ▼
Identify unusual observations
        │
        ▼
Assign anomaly predictions
        │
        ▼
Prioritize suspicious events

This approach is useful for cybersecurity because previously unseen attack patterns may not match existing predefined labels or rules.

6. Behavioral Features Used for Detection

The anomaly detection model evaluates engineered numerical features representing different aspects of authentication behavior.

These include categories such as:

Time-Based Features

Examples:

login_hour
day_of_week
is_weekend
is_night_login

These features provide information about when authentication activity occurred.

Authentication Status Features

Examples:

failed_login
successful_login

These features provide information about whether authentication attempts succeeded or failed.

User Behavior Features

Examples:

user_login_count
user_failed_login_count
user_failed_login_rate

These features describe overall user authentication behavior.

IP Address Features

Examples:

ip_login_count
ip_unique_users

These features provide information about IP activity and the number of users associated with an IP address.

Device Features

Examples:

device_login_count
device_unique_users

These features provide information about device activity and device sharing patterns.

Location Features

Examples:

location_login_count
location_unique_users

These features provide information about authentication activity associated with locations.

Behavioral Relationship Features

Examples:

user_ip_count
user_device_count
user_location_count

These features provide context about how frequently specific combinations occur.

For example, a user/IP combination that occurs only once may be behaviorally different from one observed repeatedly.

7. Feature Selection

Not every column in the dataset should be sent directly to the machine learning model.

For example, raw text values such as usernames or device names may require separate encoding techniques.

The anomaly detection pipeline selects appropriate numerical behavioral features.

The general process is:

Full Processed Dataset
        │
        ▼
Select Numerical Features
        │
        ▼
Remove Non-ML Columns
        │
        ▼
Validate Missing Values
        │
        ▼
Prepare Feature Matrix

The prepared feature matrix becomes the input to the scaling and anomaly detection stages.

8. Data Validation

Before training the model, the dataset must be checked for data quality issues.

Important validation steps include:

Confirming that the input file exists
Confirming that expected feature columns exist
Checking for missing values
Ensuring selected ML features are numerical
Confirming that the dataset contains records
Confirming that the final feature matrix can be processed by the model

Data validation is important because machine learning results are only meaningful when the input data is properly prepared.

9. Feature Scaling

Different features can have different numerical ranges.

For example:

login_hour = 0 to 23

user_login_count = potentially much larger

user_failed_login_rate = 0.0 to 1.0

Without scaling, features with larger numerical ranges may have an unintended influence on the anomaly detection process.

The project uses:

StandardScaler

The scaling process standardizes the selected numerical features.

Conceptually:

Original Features
        │
        ▼
StandardScaler
        │
        ▼
Normalized Feature Values
        │
        ▼
Isolation Forest

The fitted scaler is saved for future use.

Saved file:

outputs/models/feature_scaler.pkl

Saving the scaler is important because future data should be transformed consistently before being evaluated by the trained model.

10. Isolation Forest

The primary machine learning algorithm used in the project is:

Isolation Forest

Isolation Forest is designed for anomaly detection.

Instead of attempting to model every possible malicious behavior, it identifies observations that are easier to isolate from the rest of the dataset.

The general idea is:

Normal Events
Usually require more partitions
to isolate from similar events

Anomalous Events
Can often be isolated more quickly
because they differ from the majority

The model evaluates multiple features together to identify observations that appear unusual.

This makes Isolation Forest appropriate for the authentication anomaly detection use case.

11. Why Isolation Forest Was Selected

Isolation Forest is useful for this project because:

It supports unsupervised anomaly detection
It works well with numerical behavioral features
It does not require complete attack labels
It can identify unusual observations
It can generate anomaly scores
It is suitable for cybersecurity anomaly detection use cases
It is efficient for datasets larger than simple manual analysis

The model is not intended to independently prove that an event is malicious.

Instead, it helps prioritize authentication events for further security investigation.

12. Model Training

The scaled feature matrix is used to train the Isolation Forest model.

The process is:

Engineered Features
        │
        ▼
Feature Selection
        │
        ▼
StandardScaler
        │
        ▼
Scaled Features
        │
        ▼
Isolation Forest Training

During training, the model learns the structure of the authentication dataset and determines which observations appear more isolated from the majority.

13. Anomaly Predictions

After training, the model generates predictions for each authentication event.

The Isolation Forest model internally uses values such as:

1  = Normal
-1 = Anomaly

For easier use in the project, these predictions are converted into a clearer format:

0 = Normal
1 = Anomaly

A readable label is also generated:

Normal
Anomaly

These predictions are added to the final results dataset.

14. AI Anomaly Score

The model also generates an anomaly score for each authentication event.

The anomaly score provides a continuous measure that can be used to rank events.

The purpose of scoring is to move beyond a simple yes/no decision.

For example:

Event A → Slightly unusual
Event B → More unusual
Event C → Highly unusual

The anomaly score can be used to prioritize security investigations.

Analysts can sort events by suspiciousness and focus first on the most unusual authentication activity.

The dashboard uses anomaly-related information to support visual investigation.

15. Risk Classification

The project adds a risk classification layer on top of the machine learning results.

The purpose is to convert technical anomaly information into easier-to-understand investigation categories.

Risk levels include:

Low
Medium
High

The workflow is:

Authentication Event
        │
        ▼
Behavioral Features
        │
        ▼
AI / ML Anomaly Detection
        │
        ▼
Anomaly Prediction and Score
        │
        ▼
Risk Classification
        │
        ▼
Low / Medium / High

AI-detected anomalous events are prioritized as high-risk events in the project workflow.

Risk levels make the final output easier to use in a cybersecurity dashboard and investigation process.

16. Model Persistence

The trained machine learning model is saved after training.

Saved model:

outputs/models/isolation_forest_model.pkl

The feature scaler is also saved:

outputs/models/feature_scaler.pkl

Model persistence provides several benefits.

The model can potentially be:

Reloaded later
Used for future authentication data
Integrated into another application
Evaluated against new datasets
Compared with other anomaly detection models

This demonstrates an important part of a real machine learning workflow.

17. Output Results

The AI/ML pipeline saves the authentication results to:

data/processed/anomaly_detection_results.csv

The results include the original authentication information together with machine learning output.

Important AI-related fields include:

AI anomaly prediction
AI prediction label
Anomaly score
Risk level

This output becomes the primary dataset used by the cybersecurity dashboard.

18. AI Results Summary

The completed project run produced:

Total Authentication Events: 1,000
AI-Detected Anomalies: 50
Normal Events: 950
AI Anomaly Rate: 5.00%
High-Risk Events: 50

These values are displayed through the interactive dashboard.

The results demonstrate that the model successfully completed the end-to-end anomaly detection workflow and generated a prioritized set of unusual authentication events for investigation.

19. AI and Dashboard Integration

The machine learning output is connected directly to the dashboard.

AI / ML Model
      │
      ▼
Anomaly Prediction
      │
      ▼
Anomaly Score
      │
      ▼
Risk Level
      │
      ▼
anomaly_detection_results.csv
      │
      ▼
Streamlit Dashboard
      │
      ├── AI Anomaly Count
      ├── Anomaly Rate
      ├── High-Risk Events
      ├── Risk Distribution
      ├── AI Prediction Distribution
      └── Suspicious Event Analysis

This ensures that the AI component is visible and usable rather than existing only in the backend.

20. Current AI/ML Component

The current project includes the following machine learning capabilities:

AI / ML
│
├── Unsupervised Learning
│
├── Behavioral Feature Analysis
│
├── Feature Scaling
│
├── Isolation Forest
│
├── Anomaly Prediction
│
├── Continuous Anomaly Scoring
│
├── Risk Classification
│
└── Saved Model and Scaler

This provides a complete anomaly detection pipeline.

21. Different AI Approaches for Future Expansion

The current implementation uses Isolation Forest as the primary anomaly detection model.

Future versions can introduce additional AI and machine learning approaches.

Local Outlier Factor

Local Outlier Factor can identify observations that differ from their local neighborhood.

Potential use:

Compare authentication events
with similar nearby behavioral patterns
One-Class SVM

One-Class SVM can model the boundary of expected authentication behavior.

Potential use:

Learn normal authentication behavior
and identify events outside the learned boundary
K-Means Clustering

Clustering can group users or authentication events with similar behavior.

Potential use:

Identify normal behavioral groups
and investigate events far from expected clusters
Autoencoders

A neural-network-based autoencoder can learn to reconstruct normal authentication behavior.

Potential use:

Normal events → low reconstruction error

Unusual events → high reconstruction error

This would add a deep learning approach to the project.

Rule-Based AI Layer

A rule-based detection engine could evaluate known suspicious conditions.

Examples:

Multiple failed logins
Night login
Rare user/IP combination
Rare user/device combination

This could be combined with machine learning.

22. Hybrid AI Detection

A future version of the project could combine multiple AI techniques.

Example:

                 Authentication Event
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Isolation Forest       LOF          Rule Engine
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 Combined Risk Score
                         │
                         ▼
                   AI Risk Level

This would provide a more advanced multi-model detection architecture.

23. AI Limitations

AI anomaly detection should not be considered a replacement for a human security analyst.

An unusual event is not automatically malicious.

For example, a user may legitimately:

Travel to a new location
Use a new device
Work unusual hours
Authenticate through a shared network
Experience legitimate password failures

The AI model identifies behavior that differs from expected patterns.

The final determination of whether an event represents a cybersecurity incident requires additional context and investigation.

24. Human-in-the-Loop Security Analysis

The project follows a practical security analytics concept:

Authentication Data
        │
        ▼
SQL Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI / ML Detection
        │
        ▼
Prioritized Suspicious Events
        │
        ▼
Security Analyst Investigation
        │
        ▼
Final Security Decision

AI helps reduce the number of events requiring manual review.

The human analyst remains responsible for interpreting context and making the final security decision.

25. AI's Role in the Complete Project

The AI/ML layer works together with the other project technologies.

Technology	Role
Python	Automates data processing and the AI/ML pipeline
SQL	Supports structured authentication log analysis
Feature Engineering	Creates behavioral indicators
AI / Machine Learning	Detects unusual authentication behavior
Risk Classification	Prioritizes events for investigation
Dashboard	Visualizes AI results interactively

The complete architecture is:

Python
  │
  ├── Dataset Generation
  │
  ├── SQL Database Analysis
  │
  ├── Feature Engineering
  │
  └── AI / Machine Learning
           │
           ├── Scaling
           ├── Isolation Forest
           ├── Anomaly Detection
           ├── Anomaly Scoring
           └── Risk Classification
                    │
                    ▼
              Interactive Dashboard
26. Future AI Development Plan

A future production-style version could compare multiple models.

Example:

Model	AI Type	Purpose
Isolation Forest	Unsupervised ML	Global anomaly detection
Local Outlier Factor	Unsupervised ML	Local behavioral anomalies
One-Class SVM	Unsupervised ML	Boundary-based anomaly detection
K-Means	Unsupervised ML	Behavioral segmentation
Autoencoder	Deep Learning	Complex anomaly detection
Rule Engine	Explainable AI	Known suspicious patterns
Hybrid Ensemble	Multi-model AI	Combined anomaly scoring

This would expand the project from a single-model system into a multi-AI cybersecurity detection platform.

Conclusion

The AI and Machine Learning component transforms engineered authentication behavior into actionable anomaly detection results.

The current project uses an unsupervised Isolation Forest model to identify unusual authentication events.

The workflow includes:

Feature Selection → Data Validation → Feature Scaling → Isolation Forest → Anomaly Prediction → Anomaly Scoring → Risk Classification

The model output is saved and integrated into the interactive cybersecurity dashboard.

This ensures that Artificial Intelligence is a visible and functional component of the complete project, alongside Python, SQL, feature engineering, and interactive data visualization.


Save it with **Ctrl + S**. ✅

### Next file to create

Create:

```text
documentation/06_dashboard.md