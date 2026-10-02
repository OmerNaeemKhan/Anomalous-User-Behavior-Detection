# Interactive Cybersecurity Dashboard

## Anomalous User Behavior in Authentication Logs

---

# 1. Overview

The interactive dashboard is the final visualization and investigation layer of the project.

It transforms the processed authentication data and AI/ML anomaly detection results into an interactive cybersecurity monitoring interface.

The dashboard allows users to:

- Monitor authentication activity
- View key security metrics
- Analyze AI-detected anomalies
- Review high-risk events
- Filter events by user
- Filter events by risk level
- Filter events by location
- Filter events by date range
- Investigate suspicious authentication behavior

The dashboard ensures that the results of the Python, SQL, feature engineering, and AI/ML pipeline are presented in a format that is useful for security analysis.

---

# 2. Dashboard Technology

The dashboard is built using:

- Python
- Streamlit
- Pandas
- Plotly

The dashboard application is located at:

```text
src/05_dashboard.py

The dashboard reads the AI/ML output file:

data/processed/anomaly_detection_results.csv
3. Dashboard Position in the Project Architecture

The dashboard is the final layer of the complete cybersecurity analytics workflow.

Authentication Dataset
        │
        ▼
Python Data Processing
        │
        ▼
SQL Database Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI / Machine Learning
        │
        ▼
Anomaly Detection Results
        │
        ▼
Risk Classification
        │
        ▼
Interactive Dashboard
        │
        ▼
Cybersecurity Investigation

This integration ensures that the dashboard is connected to the actual analytical pipeline rather than displaying manually created or disconnected information.

4. Dashboard Purpose

Authentication systems can generate large numbers of events.

Reviewing raw CSV files or database records can make it difficult to quickly identify important patterns.

The dashboard provides a visual interface that helps answer questions such as:

How many authentication events occurred?
How many events were identified as anomalous by AI?
What percentage of events are anomalous?
How many high-risk events require attention?
Which users are associated with suspicious activity?
Which IP addresses are associated with anomalies?
Which locations contain unusual activity?
When does authentication activity occur?
Which events should be investigated first?

The dashboard helps transform technical results into actionable security insights.

5. Input Data

The dashboard uses the final output from the AI/ML anomaly detection stage.

Input file:

data/processed/anomaly_detection_results.csv

The dataset includes original authentication information together with engineered features and AI-generated results.

Examples of available information include:

Event ID
Timestamp
Username
IP address
Location
Device
Authentication success status
Behavioral features
AI anomaly prediction
AI prediction label
Anomaly score
Risk level

This allows the dashboard to display information from multiple stages of the project.

6. Security Key Performance Indicators

The dashboard displays high-level cybersecurity metrics.

These KPIs provide an immediate summary of the selected authentication data.

Total Events

This metric displays the total number of authentication events currently included after filters are applied.

Example:

Total Events: 1,000

This provides the overall size of the authentication activity being analyzed.

AI Anomalies

This metric displays the number of events identified as anomalous by the AI/ML model.

Example:

AI Anomalies: 50

These events represent authentication activity that differs from the overall behavioral patterns identified by the anomaly detection model.

Normal Events

This metric displays the number of events classified as normal by the AI/ML model.

Example:

Normal Events: 950

These events were not identified as anomalies by the current model.

Anomaly Rate

The anomaly rate shows the percentage of analyzed events identified as anomalous.

The calculation is:

AI-Detected Anomalies
---------------------
Total Authentication Events

For the completed project dataset:

50 / 1,000 = 5.00%

The dashboard displays:

Anomaly Rate: 5.00%

This metric provides a quick view of how much unusual behavior exists within the current filtered dataset.

High-Risk Events

This metric displays the number of events classified as high risk.

Example:

High-Risk Events: 50

Risk classification helps convert machine learning output into an investigation-friendly security category.

High-risk events should be prioritized for additional review.

7. Interactive Filters

The dashboard includes interactive filters that allow the user to focus on specific authentication activity.

The filters update the displayed data and visualizations.

User Filter

The user filter allows authentication activity to be reviewed for a specific username.

Example investigation:

Select User A
        │
        ▼
View only User A authentication events
        │
        ▼
Review anomalies, risk levels, locations,
devices, and behavioral patterns

This can support account-focused investigations.

Risk Level Filter

The risk level filter allows events to be filtered by categories such as:

Low
Medium
High

This allows a security analyst to focus specifically on high-priority events.

Example:

Select High Risk
        │
        ▼
Display only high-risk authentication events
Location Filter

The location filter allows authentication activity to be analyzed by location.

This can help investigate:

Locations associated with anomalies
High-volume authentication locations
Unusual geographic activity
Date Range Filter

The date range filter allows the dashboard to focus on authentication activity during a selected period.

This supports time-based investigations and trend analysis.

Example:

Select Date Range
        │
        ▼
Filter authentication events
        │
        ▼
Recalculate KPIs and update visualizations
8. AI Anomaly Visualization

One of the main purposes of the dashboard is to make AI/ML results visible.

The dashboard displays information related to:

AI-detected anomalies
Normal events
Anomaly rates
Anomaly scores
Risk levels
High-risk authentication events

This is important because the machine learning model should produce results that can be understood and investigated.

The dashboard connects the backend AI pipeline with the security analyst.

9. Risk Level Analysis

Risk levels provide an additional layer of interpretation.

The dashboard visualizes authentication events by risk category.

The categories include:

Low
Medium
High

Risk analysis allows users to quickly identify the distribution of authentication events across investigation priorities.

Example:

Authentication Events
        │
        ├── Low Risk
        │
        ├── Medium Risk
        │
        └── High Risk

This makes it easier to prioritize security investigations.

10. AI Prediction Distribution

The dashboard displays the distribution of:

Normal Events
Anomalous Events

This provides a visual summary of the machine learning output.

For the completed project:

Normal: 950 events
Anomaly: 50 events

The anomaly distribution helps users understand the overall output of the AI detection model.

11. Authentication Activity by Hour

The dashboard can visualize authentication activity based on login hour.

The login_hour feature was created during feature engineering.

This visualization can help identify:

High-activity periods
Low-activity periods
Night authentication
Changes in authentication patterns

Time-based activity can become particularly useful when combined with AI anomalies.

For example:

High Anomaly Activity
        +
Unusual Login Hour
        +
Failed Authentication
        =
Higher Investigation Priority
12. Anomaly Score Analysis

The anomaly score provides a continuous measure of how unusual an event appears to the machine learning model.

The dashboard can use anomaly scores to:

Rank suspicious events
Identify highly unusual activity
Compare anomalies
Support investigation prioritization

This provides more detail than only displaying:

Normal
or
Anomaly

Anomaly scoring allows events to be ordered based on relative unusualness.

13. User Analysis

The dashboard supports user-focused security analysis.

Possible questions include:

Which users have the most authentication activity?
Which users have the most anomalies?
Which users are associated with high-risk events?
Which users have high failed login activity?

User analysis can help security teams prioritize account investigations.

14. IP Address Analysis

IP address information is an important part of authentication investigations.

The dashboard can display suspicious activity associated with IP addresses.

Potential analysis includes:

IP addresses with high activity
IP addresses associated with anomalies
IP addresses used by multiple users
IP addresses associated with high-risk events

IP information should be analyzed together with other behavioral features because shared corporate networks or VPNs may legitimately produce high activity.

15. Location Analysis

Location analysis helps visualize where authentication activity occurs.

The dashboard can identify:

Locations with high authentication volume
Locations associated with anomalous events
Locations associated with high-risk activity

Location alone should not be treated as proof of malicious behavior.

The project uses location as one behavioral signal among multiple factors.

16. Login Success and Failure Analysis

Authentication success and failure status provide important context.

The dashboard can visualize:

Successful Authentication
vs.
Failed Authentication

This can support investigation into:

Repeated failures
Failed login patterns
Users with unusual failure rates
Failed events associated with anomalies

Combining authentication failures with AI detection can provide stronger investigation signals.

17. Suspicious Event Investigation Table

The dashboard includes a detailed view of authentication events.

This allows users to move from high-level KPIs into individual records.

Potential event details include:

Timestamp
Username
IP address
Location
Device
Login success status
AI prediction
Anomaly score
Risk level

This creates an investigation workflow:

Dashboard KPI
      │
      ▼
Visualization
      │
      ▼
Identify Pattern
      │
      ▼
Filter Data
      │
      ▼
Review Suspicious Events
      │
      ▼
Investigate Individual Records
18. Dashboard and AI Integration

The dashboard directly uses results generated by the AI/ML pipeline.

Feature Engineering
        │
        ▼
Authentication Features
        │
        ▼
Isolation Forest
        │
        ├── AI Prediction
        ├── Anomaly Score
        └── Risk Level
        │
        ▼
anomaly_detection_results.csv
        │
        ▼
Interactive Dashboard

This ensures that the AI component is visible to users and contributes directly to cybersecurity analysis.

19. Dashboard and SQL Integration

The project architecture also connects the dashboard to the earlier database analysis stage.

Authentication Data
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI / Machine Learning
        │
        ▼
Dashboard

SQL provides structured analysis, while the dashboard provides visual analysis.

Together, they support different stages of the cybersecurity investigation process.

20. Dashboard and Python Integration

Python is responsible for building and operating the dashboard.

Python is used to:

Load the processed AI results
Process dashboard data
Apply user filters
Calculate KPIs
Generate charts
Display tables
Handle dashboard interactions

The dashboard therefore represents another visible use of Python within the project.

21. Complete Dashboard Investigation Workflow

The dashboard supports the following investigation process:

Open Dashboard
        │
        ▼
Review Security KPIs
        │
        ▼
Identify Anomaly Rate
        │
        ▼
Review High-Risk Events
        │
        ▼
Analyze Risk Distribution
        │
        ▼
Review AI Predictions
        │
        ▼
Apply User / Location / Risk Filters
        │
        ▼
Analyze Patterns
        │
        ▼
Review Suspicious Event Records
        │
        ▼
Prioritize Security Investigation

This represents a simplified security monitoring workflow.

22. Current Dashboard Results

The completed dashboard displays the following results from the current dataset:

Total Events: 1,000
AI Anomalies: 50
Normal Events: 950
Anomaly Rate: 5.00%
High-Risk Events: 50

These values confirm that the AI anomaly detection results are successfully integrated into the dashboard.

23. Dashboard Technology Summary
Technology	Role
Python	Dashboard application logic
Streamlit	Interactive web application framework
Pandas	Data loading and processing
Plotly	Interactive visualizations
AI/ML Results	Anomaly predictions and scoring
Risk Classification	Investigation prioritization
24. Cybersecurity Value

The dashboard helps convert large amounts of authentication data into a more usable security monitoring interface.

It supports:

Faster data exploration
AI result visibility
Security metric monitoring
Risk prioritization
Interactive investigation
Pattern identification
Event-level review

The dashboard does not replace a full SIEM or Security Operations Center platform.

Instead, it demonstrates how Python, data analytics, AI, and visualization can be combined to create a cybersecurity monitoring prototype.

25. Future Dashboard Enhancements

Future versions of the dashboard could include:

Real-time log ingestion
Live database connections
Automatic dashboard refresh
Alert notifications
Email or Slack alerts
User behavior profiles
Investigation notes
Analyst feedback buttons
Model comparison views
Multiple AI model results
Explainable AI indicators
Geographic login maps
Impossible travel visualization
Authentication timelines
Alert severity scoring

A future version could also connect the dashboard directly to a production database or SIEM platform.

Conclusion

The interactive cybersecurity dashboard is the final investigation and visualization layer of the project.

It combines the results of:

Python → SQL → Feature Engineering → AI/ML → Risk Classification

into an interactive interface.

The dashboard provides:

Security KPIs
AI anomaly monitoring
Risk analysis
Interactive filtering
Authentication behavior visualization
Suspicious event investigation

This ensures that dashboards are a visible and functional part of the complete cybersecurity project and that the Python, SQL, and AI/ML components are connected in one end-to-end workflow.


Press **Ctrl + S**. ✅

### Next step

Create this next file:

```text
documentation/07_project_findings.md

Then tell me created, and I’ll give you the complete findings and conclusions document to paste.

06\_dashboard.md

Start writing

Sure — here is the same content as a clean writing block, ready to copy and paste into:

documentation/06_dashboard.md

# Interactive Cybersecurity Dashboard

## Anomalous User Behavior in Authentication Logs

---

# 1. Overview

The interactive dashboard is the final visualization and investigation layer of the project.

It transforms the processed authentication data and AI/ML anomaly detection results into an interactive cybersecurity monitoring interface.

The dashboard allows users to:

- Monitor authentication activity
- View key security metrics
- Analyze AI-detected anomalies
- Review high-risk events
- Filter events by user
- Filter events by risk level
- Filter events by location
- Filter events by date range
- Investigate suspicious authentication behavior

The dashboard ensures that the results of the Python, SQL, feature engineering, and AI/ML pipeline are presented in a format that is useful for security analysis.

---

# 2. Dashboard Technology

The dashboard is built using:

- Python
- Streamlit
- Pandas
- Plotly

The dashboard application is located at:

```text
src/05_dashboard.py

The dashboard reads the AI/ML output file:

data/processed/anomaly_detection_results.csv
3. Dashboard Position in the Project Architecture

The dashboard is the final layer of the complete cybersecurity analytics workflow.

Authentication Dataset
        │
        ▼
Python Data Processing
        │
        ▼
SQL Database Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI / Machine Learning
        │
        ▼
Anomaly Detection Results
        │
        ▼
Risk Classification
        │
        ▼
Interactive Dashboard
        │
        ▼
Cybersecurity Investigation

This integration ensures that the dashboard is connected to the actual analytical pipeline rather than displaying manually created or disconnected information.

4. Dashboard Purpose

Authentication systems can generate large numbers of events.

Reviewing raw CSV files or database records can make it difficult to quickly identify important patterns.

The dashboard provides a visual interface that helps answer questions such as:

How many authentication events occurred?
How many events were identified as anomalous by AI?
What percentage of events are anomalous?
How many high-risk events require attention?
Which users are associated with suspicious activity?
Which IP addresses are associated with anomalies?
Which locations contain unusual activity?
When does authentication activity occur?
Which events should be investigated first?

The dashboard helps transform technical results into actionable security insights.

5. Input Data

The dashboard uses the final output from the AI/ML anomaly detection stage.

Input file:

data/processed/anomaly_detection_results.csv

The dataset includes original authentication information together with engineered features and AI-generated results.

Examples of available information include:

Event ID
Timestamp
Username
IP address
Location
Device
Authentication success status
Behavioral features
AI anomaly prediction
AI prediction label
Anomaly score
Risk level

This allows the dashboard to display information from multiple stages of the project.

6. Security Key Performance Indicators

The dashboard displays high-level cybersecurity metrics.

These KPIs provide an immediate summary of the selected authentication data.

Total Events

This metric displays the total number of authentication events currently included after filters are applied.

Example:

Total Events: 1,000

This provides the overall size of the authentication activity being analyzed.

AI Anomalies

This metric displays the number of events identified as anomalous by the AI/ML model.

Example:

AI Anomalies: 50

These events represent authentication activity that differs from the overall behavioral patterns identified by the anomaly detection model.

Normal Events

This metric displays the number of events classified as normal by the AI/ML model.

Example:

Normal Events: 950

These events were not identified as anomalies by the current model.

Anomaly Rate

The anomaly rate shows the percentage of analyzed events identified as anomalous.

The calculation is:

AI-Detected Anomalies
---------------------
Total Authentication Events

For the completed project dataset:

50 / 1,000 = 5.00%

The dashboard displays:

Anomaly Rate: 5.00%
High-Risk Events

This metric displays the number of events classified as high risk.

Example:

High-Risk Events: 50

High-risk events should be prioritized for additional review.

7. Interactive Filters

The dashboard includes interactive filters that allow the user to focus on specific authentication activity.

The filters update the displayed data and visualizations.

User Filter

The user filter allows authentication activity to be reviewed for a specific username.

This can support account-focused investigations.

Risk Level Filter

The risk level filter allows events to be filtered by categories such as:

Low
Medium
High

This allows a security analyst to focus specifically on high-priority events.

Location Filter

The location filter allows authentication activity to be analyzed by location.

This can help investigate:

Locations associated with anomalies
High-volume authentication locations
Unusual geographic activity
Date Range Filter

The date range filter allows the dashboard to focus on authentication activity during a selected period.

This supports time-based investigations and trend analysis.

8. AI Anomaly Visualization

One of the main purposes of the dashboard is to make AI/ML results visible.

The dashboard displays information related to:

AI-detected anomalies
Normal events
Anomaly rates
Anomaly scores
Risk levels
High-risk authentication events

This is important because the machine learning model should produce results that can be understood and investigated.

The dashboard connects the backend AI pipeline with the security analyst.

9. Risk Level Analysis

Risk levels provide an additional layer of interpretation.

The dashboard visualizes authentication events by risk category:

Low
Medium
High

Risk analysis allows users to quickly identify the distribution of authentication events across investigation priorities.

10. AI Prediction Distribution

The dashboard displays the distribution of:

Normal Events
Anomalous Events

For the completed project:

Normal: 950 events
Anomaly: 50 events

The anomaly distribution helps users understand the overall output of the AI detection model.

11. Authentication Activity by Hour

The dashboard visualizes authentication activity based on the login_hour feature created during feature engineering.

This visualization can help identify:

High-activity periods
Low-activity periods
Night authentication
Changes in authentication patterns

Time-based activity can become particularly useful when combined with AI anomalies.

For example:

High Anomaly Activity
        +
Unusual Login Hour
        +
Failed Authentication
        =
Higher Investigation Priority
12. Anomaly Score Analysis

The anomaly score provides a continuous measure of how unusual an event appears to the machine learning model.

The dashboard can use anomaly scores to:

Rank suspicious events
Identify highly unusual activity
Compare anomalies
Support investigation prioritization

This provides more detail than only displaying:

Normal
or
Anomaly
13. User Analysis

The dashboard supports user-focused security analysis.

Possible questions include:

Which users have the most authentication activity?
Which users have the most anomalies?
Which users are associated with high-risk events?
Which users have high failed login activity?
14. IP Address Analysis

IP address information is an important part of authentication investigations.

The dashboard can display suspicious activity associated with IP addresses.

Potential analysis includes:

IP addresses with high activity
IP addresses associated with anomalies
IP addresses used by multiple users
IP addresses associated with high-risk events

IP information should be analyzed together with other behavioral features because shared corporate networks or VPNs may legitimately produce high activity.

15. Location Analysis

Location analysis helps visualize where authentication activity occurs.

The dashboard can identify:

Locations with high authentication volume
Locations associated with anomalous events
Locations associated with high-risk activity

Location alone should not be treated as proof of malicious behavior.

16. Login Success and Failure Analysis

Authentication success and failure status provide important context.

The dashboard can visualize:

Successful Authentication
vs.
Failed Authentication

This can support investigation into:

Repeated failures
Failed login patterns
Users with unusual failure rates
Failed events associated with anomalies
17. Suspicious Event Investigation Table

The dashboard includes a detailed view of authentication events.

Potential event details include:

Timestamp
Username
IP address
Location
Device
Login success status
AI prediction
Anomaly score
Risk level

This creates an investigation workflow:

Dashboard KPI
      │
      ▼
Visualization
      │
      ▼
Identify Pattern
      │
      ▼
Filter Data
      │
      ▼
Review Suspicious Events
      │
      ▼
Investigate Individual Records
18. Dashboard and AI Integration

The dashboard directly uses results generated by the AI/ML pipeline.

Feature Engineering
        │
        ▼
Authentication Features
        │
        ▼
Isolation Forest
        │
        ├── AI Prediction
        ├── Anomaly Score
        └── Risk Level
        │
        ▼
anomaly_detection_results.csv
        │
        ▼
Interactive Dashboard

This ensures that the AI component is visible to users and contributes directly to cybersecurity analysis.

19. Dashboard and SQL Integration

The project architecture also connects the dashboard to the earlier database analysis stage.

Authentication Data
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI / Machine Learning
        │
        ▼
Dashboard

SQL provides structured analysis, while the dashboard provides visual analysis.

20. Dashboard and Python Integration

Python is responsible for building and operating the dashboard.

Python is used to:

Load the processed AI results
Process dashboard data
Apply user filters
Calculate KPIs
Generate charts
Display tables
Handle dashboard interactions

The dashboard therefore represents another visible use of Python within the project.

21. Complete Dashboard Investigation Workflow
Open Dashboard
        │
        ▼
Review Security KPIs
        │
        ▼
Identify Anomaly Rate
        │
        ▼
Review High-Risk Events
        │
        ▼
Analyze Risk Distribution
        │
        ▼
Review AI Predictions
        │
        ▼
Apply User / Location / Risk Filters
        │
        ▼
Analyze Patterns
        │
        ▼
Review Suspicious Event Records
        │
        ▼
Prioritize Security Investigation

This represents a simplified security monitoring workflow.

22. Current Dashboard Results

The completed dashboard displays the following results from the current dataset:

Total Events: 1,000
AI Anomalies: 50
Normal Events: 950
Anomaly Rate: 5.00%
High-Risk Events: 50

These values confirm that the AI anomaly detection results are successfully integrated into the dashboard.

23. Dashboard Technology Summary
Technology	Role
Python	Dashboard application logic
Streamlit	Interactive web application framework
Pandas	Data loading and processing
Plotly	Interactive visualizations
AI/ML Results	Anomaly predictions and scoring
Risk Classification	Investigation prioritization
24. Cybersecurity Value

The dashboard helps convert large amounts of authentication data into a more usable security monitoring interface.

It supports:

Faster data exploration
AI result visibility
Security metric monitoring
Risk prioritization
Interactive investigation
Pattern identification
Event-level review

The dashboard does not replace a full SIEM or Security Operations Center platform.

Instead, it demonstrates how Python, data analytics, AI, and visualization can be combined to create a cybersecurity monitoring prototype.

25. Future Dashboard Enhancements

Future versions of the dashboard could include:

Real-time log ingestion
Live database connections
Automatic dashboard refresh
Alert notifications
Email or Slack alerts
User behavior profiles
Investigation notes
Analyst feedback buttons
Model comparison views
Multiple AI model results
Explainable AI indicators
Geographic login maps
Impossible travel visualization
Authentication timelines
Alert severity scoring

A future version could also connect the dashboard directly to a production database or SIEM platform.

Conclusion

The interactive cybersecurity dashboard is the final investigation and visualization layer of the project.

It combines the results of:

Python → SQL → Feature Engineering → AI/ML → Risk Classification

into an interactive interface.

The dashboard provides:

Security KPIs
AI anomaly monitoring
Risk analysis
Interactive filtering
Authentication behavior visualization
Suspicious event investigation

This ensures that dashboards are a visible and functional part of the complete cybersecurity project and that the Python, SQL, and AI/ML components are connected in one end-to-end workflow.


Save it with **Ctrl + S**.

Next, create:

```text
documentation/07_project_findings.md