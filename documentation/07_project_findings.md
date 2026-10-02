# Project Findings and Conclusions

## Anomalous User Behavior in Authentication Logs

---

# 1. Project Overview

This project analyzed authentication log data to identify unusual user behavior and potentially suspicious authentication events.

The project was designed as an end-to-end cybersecurity analytics workflow using:

- Python
- SQL
- Feature Engineering
- Artificial Intelligence
- Machine Learning
- Interactive Dashboards

The complete workflow transformed raw authentication records into behavioral features, analyzed the data using SQL, applied an AI/ML anomaly detection model, assigned risk levels, and presented the results through an interactive dashboard.

The complete architecture is:

```text
Raw Authentication Logs
        │
        ▼
Python Data Processing
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
Anomaly Detection
        │
        ▼
Risk Classification
        │
        ▼
Interactive Dashboard
        │
        ▼
Security Investigation
2. Dataset Findings

The final project used a manageable authentication dataset containing:

Total Authentication Records: 1,000

The smaller dataset allowed the complete project pipeline to run efficiently while still demonstrating the cybersecurity analytics workflow.

The authentication records contained information such as:

Event ID
Timestamp
Username
IP address
Location
Device
Authentication status
Anomaly-related information

The dataset was processed successfully through the complete pipeline.

3. SQL Analysis Findings

The authentication data was loaded into a SQLite database for structured analysis.

SQL was used to investigate authentication behavior before applying machine learning.

The database analysis supported questions involving:

Total authentication activity
Successful logins
Failed logins
User activity
IP address activity
Location activity
Device activity
Authentication patterns

SQL demonstrated how authentication data can be queried and summarized using a relational database.

The database layer provided an important structured analysis component within the project.

4. Feature Engineering Findings

Raw authentication records were transformed into additional behavioral features.

The feature engineering process successfully created indicators related to:

Login hour
Day of week
Weekend activity
Night authentication
Failed login behavior
Successful login behavior
User login frequency
User failed login counts
User failed login rates
IP address activity
Device activity
Location activity
User/IP relationships
User/device relationships
User/location relationships

The final feature engineering stage produced:

Original Records: 1,000
Processed Records: 1,000
Total Columns: 27

The increase in available behavioral information created a stronger foundation for anomaly detection.

5. Time-Based Behavior Findings

The project created time-related features to support behavioral analysis.

These included:

Login hour
Day of week
Weekend indicator
Night login indicator

Time is important in authentication analysis because activity may become more suspicious when it occurs outside a user's expected behavioral pattern.

For example, a night login alone may not be suspicious.

However, a night login combined with:

A rare IP address
A new device
An unusual location
Failed authentication attempts

may represent a stronger investigation signal.

This demonstrates the importance of combining multiple behavioral features.

6. Failed Login Behavior Findings

The project created features related to authentication failures.

These included:

failed_login
user_failed_login_count
user_failed_login_rate

Failed logins are important because repeated failures may indicate:

Password guessing
Brute-force attempts
Credential stuffing
Unauthorized access attempts
Legitimate user mistakes

The project therefore did not rely only on the presence of a failed login.

Instead, the behavioral features provided additional context regarding the frequency and rate of failures.

7. User Behavior Findings

The project analyzed authentication behavior at the user level.

Features included:

user_login_count
user_failed_login_count
user_failed_login_rate

These features allowed the project to compare authentication activity across users.

Potentially unusual user behavior can include:

Very high authentication frequency
Unusually high failed login counts
High failed login rates
Rare combinations of users with IP addresses
Rare combinations of users with devices
Rare combinations of users with locations

The project used these features as inputs to the anomaly detection process.

8. IP Address Findings

The project created IP-related behavioral features including:

ip_login_count
ip_unique_users
user_ip_count

These features helped provide context about:

Overall IP activity
Number of users associated with an IP
Frequency of specific user/IP combinations

A high-activity IP address is not automatically malicious.

For example, corporate networks, VPN gateways, and shared infrastructure may be associated with many authentication events.

The project therefore treated IP information as one part of a larger behavioral analysis.

9. Device Behavior Findings

Device-related features included:

device_login_count
device_unique_users
user_device_count

These features provided information about:

Device authentication frequency
Number of users associated with devices
Frequency of specific user/device combinations

This supports the investigation of behavioral changes such as:

Unusual device usage
Rare user/device combinations
Shared device activity

Again, unusual behavior does not automatically confirm malicious activity.

The results require contextual investigation.

10. Location Behavior Findings

Location-related features included:

location_login_count
location_unique_users
user_location_count

These features helped measure:

Authentication frequency by location
Number of users associated with locations
Frequency of specific user/location combinations

Rare location activity can be useful for identifying changes in behavior.

However, location information alone should not be treated as proof of a security incident.

Users may legitimately travel or work from multiple locations.

11. AI/ML Findings

The project used an unsupervised machine learning approach based on:

Isolation Forest

The model analyzed engineered numerical features and identified authentication events that appeared unusual compared with the overall dataset.

The completed model run produced:

Total Authentication Events: 1,000
AI-Detected Anomalies: 50
Normal Events: 950
AI Anomaly Rate: 5.00%
High-Risk Events: 50

The results demonstrate that the anomaly detection pipeline successfully identified a subset of authentication events for additional investigation.

12. Anomaly Detection Finding

The AI model classified:

50 events as anomalies

out of:

1,000 total authentication events

This produced an anomaly rate of:

5.00%

These events were identified because their combined behavioral characteristics differed from the broader authentication dataset.

The anomaly detection process evaluated multiple behavioral features together rather than using a single static rule.

This is an important advantage of machine learning-based anomaly detection.

13. High-Risk Event Finding

The project assigned risk classifications to make the AI output easier to use during investigation.

The completed results included:

High-Risk Events: 50

High-risk events represent authentication records prioritized for additional review.

The risk layer helps translate technical machine learning output into a cybersecurity investigation workflow.

The process is:

Authentication Event
        │
        ▼
Behavioral Features
        │
        ▼
AI Anomaly Detection
        │
        ▼
Anomaly Score
        │
        ▼
Risk Classification
        │
        ▼
Investigation Priority
14. Key Finding: Multiple Signals Are More Valuable

One of the most important findings of the project is that authentication events should not be evaluated using only one factor.

For example:

Failed Login

alone may not indicate an attack.

Similarly:

Night Login

alone may not indicate malicious behavior.

A stronger investigation signal can occur when multiple unusual characteristics appear together.

Example:

Night Login
      +
High Failed Login Activity
      +
Rare User/IP Combination
      +
Rare User/Device Combination
      +
AI Anomaly Detection
      =
Higher Investigation Priority

This is the central concept behind behavioral anomaly detection.

15. Dashboard Findings

The interactive dashboard successfully integrated the output of the project pipeline.

The dashboard displayed key results including:

Total Events: 1,000
AI Anomalies: 50
Normal Events: 950
Anomaly Rate: 5.00%
High-Risk Events: 50

The dashboard also supports investigation through:

Security KPIs
AI anomaly visualization
Risk analysis
Interactive filtering
User analysis
Location analysis
Authentication activity analysis
Suspicious event tables

This made the AI results visible and usable.

16. End-to-End Integration Finding

A major outcome of the project is the successful integration of multiple technologies.

The project did not rely on only one technology.

Instead, the workflow connected:

Python
   │
   ├── Data Processing
   │
SQL
   │
   ├── Structured Analysis
   │
Feature Engineering
   │
   ├── Behavioral Indicators
   │
AI / Machine Learning
   │
   ├── Isolation Forest
   ├── Anomaly Detection
   └── Risk Classification
   │
Dashboard
   │
   └── Interactive Investigation

This demonstrates an end-to-end cybersecurity analytics architecture.

17. Main Project Conclusion

The project successfully demonstrates how authentication logs can be transformed into a behavioral anomaly detection system.

The final solution includes:

Raw authentication data
Python data processing
SQLite database analysis
SQL queries
Feature engineering
Behavioral analytics
AI/ML anomaly detection
Anomaly scoring
Risk classification
Interactive dashboard visualization

The workflow provides a practical example of how multiple technical skills can be combined in a cybersecurity project.

18. Security Interpretation

The AI model identifies events that are unusual.

It does not independently prove that an event is malicious.

This distinction is important.

An event may be anomalous because of legitimate reasons, including:

User travel
Remote work
New devices
Changed work schedules
Shared corporate infrastructure
VPN usage
Legitimate authentication mistakes

Therefore, AI-generated anomalies should be treated as:

Prioritized Investigation Signals

rather than confirmed cybersecurity incidents.

Human investigation remains necessary.

19. Human-in-the-Loop Conclusion

The project supports a human-in-the-loop security model.

Authentication Logs
        │
        ▼
Automated Processing
        │
        ▼
SQL Analysis
        │
        ▼
Feature Engineering
        │
        ▼
AI/ML Detection
        │
        ▼
Suspicious Event Prioritization
        │
        ▼
Security Analyst Investigation
        │
        ▼
Final Decision

The AI system helps reduce the amount of data requiring immediate manual attention.

The security analyst remains responsible for evaluating context and determining whether a real security incident exists.

20. Limitations

The current project is a portfolio-style cybersecurity analytics prototype.

Its limitations include:

Static dataset rather than live authentication logs
No real-time log ingestion
No direct SIEM integration
No threat intelligence enrichment
No IP reputation integration
No automatic alert delivery
One primary machine learning anomaly detection model
No confirmed production incident-response workflow

These limitations provide opportunities for future expansion.

21. Future Improvements

Future versions could introduce additional capabilities.

Data Improvements
Larger datasets
Real enterprise authentication logs
Streaming authentication data
Live database connections
SQL Improvements
Additional security investigation queries
Automated SQL reports
Historical trend analysis
Feature Engineering Improvements
First-seen IP detection
First-seen device detection
First-seen location detection
Authentication velocity
Failed login bursts
Time since previous login
Impossible travel detection
AI Improvements
Local Outlier Factor
One-Class SVM
K-Means clustering
Autoencoders
Deep learning anomaly detection
Rule-based detection
Multi-model AI ensembles
Dashboard Improvements
Real-time updates
Alert notifications
Geographic maps
Authentication timelines
Explainable AI results
Model comparison
Investigation notes
22. Final Conclusion

The Anomalous User Behavior in Authentication Logs project demonstrates a complete cybersecurity analytics workflow.

The project successfully combines:

Python + SQL + Feature Engineering + Artificial Intelligence + Machine Learning + Interactive Dashboard

The AI model identified:

50 anomalous events

from:

1,000 authentication events

resulting in an anomaly rate of:

5.00%

The anomaly detection results were then converted into investigation-friendly risk classifications and displayed through an interactive dashboard.

The project demonstrates an important cybersecurity principle:

Security events become more meaningful when multiple behavioral signals are analyzed together.

The final workflow provides a strong foundation for future development into a more advanced behavioral analytics and authentication monitoring platform.


Save it with **Ctrl + S**. ✅

Next, create:

```text
documentation/08_technical_architecture.md