# Feature Engineering

## Anomalous User Behavior in Authentication Logs

---

# 1. Overview

Feature engineering is the process of transforming raw authentication log data into meaningful variables that can be used for cybersecurity analysis and machine learning.

Raw authentication events contain information such as:

- Timestamp
- Username
- IP address
- Location
- Device
- Login success or failure

However, raw values alone do not always describe user behavior clearly.

For example, a timestamp does not directly indicate whether a login occurred during unusual hours. Similarly, a single IP address does not directly indicate how frequently that IP has been used.

The feature engineering stage creates additional behavioral indicators that help identify unusual authentication patterns.

This stage is implemented using:

```text
Python
Pandas

The feature engineering script is:

src/03_feature_engineering.py
2. Role of Feature Engineering

Feature engineering connects the raw data layer with the AI and Machine Learning layer.

The project workflow is:

Raw Authentication Logs
        │
        ▼
Feature Engineering
        │
        ├── Time Features
        ├── Login Status Features
        ├── User Behavior Features
        ├── IP Features
        ├── Device Features
        ├── Location Features
        └── Behavioral Combination Features
        │
        ▼
Processed Authentication Features
        │
        ▼
AI / Machine Learning

The purpose is to provide the anomaly detection model with measurable behavioral patterns instead of only raw authentication fields.

3. Input Dataset

The feature engineering process reads the raw authentication dataset:

data/raw/authentication_logs.csv

The dataset contains authentication event information.

Examples of important fields include:

Field	Description
event_id	Unique identifier for each authentication event
timestamp	Date and time of the authentication event
username	User associated with the authentication event
ip_address	IP address used during authentication
location	Location associated with the event
device	Device used for authentication
success	Indicates whether authentication was successful
is_anomaly	Original anomaly indicator in the dataset
4. Timestamp Processing

The first major transformation is converting the timestamp into a datetime format.

The timestamp is processed so that additional time-based information can be extracted.

These additional features include:

Login hour
Day of the week
Day name
Weekend indicator
Night login indicator

Time-based features are important because unusual authentication activity may occur outside normal behavioral patterns.

5. Login Hour Feature

Feature:

login_hour

The login hour extracts the hour of the day from the timestamp.

Example:

Timestamp: 2026-08-27 23:45:00

login_hour: 23

This allows authentication activity to be analyzed by hour.

Potential security value:

Identifying unusual late-night logins
Identifying unusual early-morning logins
Comparing login times across users
Detecting activity outside expected working patterns

The dashboard also uses this feature to visualize authentication activity by hour.

6. Day of Week Feature

Feature:

day_of_week

This feature identifies the numerical day of the week.

It supports the analysis of whether authentication behavior differs between weekdays and weekends.

Potential uses include:

Detecting unusual weekend activity
Comparing weekday and weekend login patterns
Identifying changes in user behavior over time
7. Day Name Feature

Feature:

day_name

This provides a readable name for the day associated with each authentication event.

Examples include:

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

This feature improves human-readable analysis and can support future dashboard enhancements.

8. Weekend Indicator

Feature:

is_weekend

This is a binary feature.

0 = Weekday
1 = Weekend

Weekend authentication can be useful for anomaly detection because some users may normally authenticate only during business days.

However, weekend activity is not automatically suspicious.

The feature is used as one behavioral signal among many.

9. Night Login Indicator

Feature:

is_night_login

The project defines night authentication activity as:

10 PM through 6 AM

The binary output is:

0 = Normal Time Window
1 = Night Login

This feature helps the model identify authentication events occurring during potentially unusual hours.

Potential investigation questions include:

Does the user normally log in at night?
Is the night login associated with a new device?
Is the login from a new location?
Did the authentication fail?
Did the AI model identify the event as anomalous?

The night indicator should therefore be evaluated together with other features.

10. Login Status Features

The original authentication status is transformed into two machine learning-friendly indicators.

Features:

failed_login
successful_login
Failed Login

Feature:

failed_login

Values:

0 = Authentication was not a failure
1 = Authentication failed

Failed authentication attempts are important cybersecurity indicators.

Repeated failures may indicate:

Password guessing
Brute-force activity
Credential stuffing
Unauthorized access attempts
User credential mistakes
Successful Login

Feature:

successful_login

Values:

0 = Authentication was not successful
1 = Authentication succeeded

This feature provides a separate indicator for successful authentication behavior.

11. User Login Count

Feature:

user_login_count

This feature calculates the total number of authentication events associated with each user.

Example:

User A → 25 authentication events
User B → 8 authentication events
User C → 42 authentication events

This allows the AI model to consider the overall activity frequency of each user.

A user with unusually high or low activity may differ from normal behavioral patterns.

12. User Failed Login Count

Feature:

user_failed_login_count

This calculates the total number of failed authentication events for each user.

Example:

User A → 2 failed logins
User B → 0 failed logins
User C → 9 failed logins

This feature helps identify users with repeated authentication failures.

Repeated failures can be an important behavioral signal when combined with:

Login frequency
IP activity
Device activity
Location behavior
Time of authentication
13. User Failed Login Rate

Feature:

user_failed_login_rate

The failure rate is calculated as:

User Failed Login Count
-----------------------
Total User Login Count

For example:

10 total logins
4 failed logins

Failure Rate = 4 / 10 = 0.40

This feature provides a normalized measure of failed authentication behavior.

This is useful because a user with five failed logins out of ten events behaves differently from a user with five failed logins out of one hundred events.

14. IP Login Count

Feature:

ip_login_count

This feature calculates how many times each IP address appears in the authentication dataset.

Example:

192.168.1.10 → 40 events
10.0.0.25    → 3 events
172.16.5.8   → 22 events

The feature helps measure IP address activity.

High IP activity may be normal in some environments, such as shared corporate networks.

Therefore, this feature is combined with other indicators rather than being treated as automatically suspicious.

15. IP Unique Users

Feature:

ip_unique_users

This calculates the number of different users associated with an IP address.

Example:

IP A → Used by 1 user
IP B → Used by 5 users
IP C → Used by 20 users

This can help identify shared IP addresses and unusual authentication relationships.

A high number of users associated with an IP may be normal for:

Corporate networks
VPN gateways
Shared network infrastructure

It may also be useful for identifying unexpected account access patterns.

16. Device Login Count

Feature:

device_login_count

This feature measures how frequently each device appears in authentication activity.

Example:

Laptop-A → 50 logins
Desktop-B → 17 logins
Mobile-C → 8 logins

Device frequency provides another behavioral context for the anomaly detection model.

17. Device Unique Users

Feature:

device_unique_users

This calculates the number of different users associated with a device.

Example:

Device A → 1 user
Device B → 3 users
Device C → 10 users

This feature can help identify devices that are shared across multiple accounts.

In some environments this is expected.

In others, unusual device sharing may require investigation.

18. Location Login Count

Feature:

location_login_count

This feature counts the number of authentication events associated with each location.

Example:

New York → 200 events
Chicago → 75 events
Dallas → 40 events

This provides information about the overall authentication activity associated with each location.

19. Location Unique Users

Feature:

location_unique_users

This calculates the number of unique users authenticating from each location.

This can support the identification of:

Highly shared locations
Low-frequency locations
Locations associated with many users
Locations that may require additional investigation
20. User and IP Combination Feature

Feature:

user_ip_count

This feature measures how frequently a specific user and IP address combination occurs.

Example:

User A + IP 192.168.1.10 → 15 events
User A + IP 10.0.0.25     → 1 event

A rare user/IP combination may be behaviorally different from a frequently observed combination.

This type of relationship-based feature is useful for anomaly detection because it analyzes context rather than only individual values.

21. User and Device Combination Feature

Feature:

user_device_count

This measures how frequently a specific user authenticates using a particular device.

Example:

User A + Laptop-A → 30 events
User A + Mobile-C → 1 event

Rare user/device combinations can help identify changes in authentication behavior.

Potential investigation scenarios include:

First-time device usage
Unusual device changes
Account access from unexpected systems
22. User and Location Combination Feature

Feature:

user_location_count

This measures how frequently a user authenticates from a particular location.

Example:

User A + New York → 20 events
User A + Dallas   → 1 event

Rare location combinations may indicate a deviation from expected user behavior.

This does not automatically mean the activity is malicious.

The AI model considers this information together with other features.

23. Feature Categories Summary

The engineered features can be grouped into the following categories:

Category	Features
Time	login_hour, day_of_week, day_name, is_weekend, is_night_login
Login Status	failed_login, successful_login
User Behavior	user_login_count, user_failed_login_count, user_failed_login_rate
IP Behavior	ip_login_count, ip_unique_users
Device Behavior	device_login_count, device_unique_users
Location Behavior	location_login_count, location_unique_users
User/IP Relationship	user_ip_count
User/Device Relationship	user_device_count
User/Location Relationship	user_location_count

These features provide multiple perspectives on authentication behavior.

24. Feature Engineering and AI

The engineered features are used by the AI and Machine Learning pipeline.

The workflow is:

Raw Authentication Event
        │
        ▼
Feature Extraction
        │
        ├── Time
        ├── Login Status
        ├── User Behavior
        ├── IP Behavior
        ├── Device Behavior
        ├── Location Behavior
        └── Behavioral Relationships
        │
        ▼
Numerical Feature Dataset
        │
        ▼
Feature Scaling
        │
        ▼
Isolation Forest
        │
        ▼
Anomaly Prediction

Feature engineering is therefore one of the most important stages of the machine learning pipeline.

25. Output Dataset

After feature engineering, the processed dataset is saved to:

data/processed/authentication_features.csv

The processed dataset contains the original authentication fields together with the newly created behavioral features.

The completed processing stage produced:

Original Records: 1,000
Processed Records: 1,000
Total Columns: 27

This dataset is used as the input for the AI and Machine Learning anomaly detection stage.

26. Role in Cybersecurity Detection

Feature engineering allows the project to move beyond simple rule-based checks.

Instead of asking only:

Did the login fail?

The system can analyze multiple factors:

Did the login occur at night?

How frequently does the user log in?

How many failures does the user have?

What is the user's failure rate?

How often is this IP used?

How many users use this IP?

How often is this device used?

How many users use this device?

How frequently has this user used this IP?

How frequently has this user used this device?

How frequently has this user authenticated from this location?

Combining multiple signals provides richer behavioral context for anomaly detection.

27. Future Feature Engineering Enhancements

Future versions of the project could include additional behavioral features such as:

First-seen IP address indicator
First-seen device indicator
First-seen location indicator
Time since previous login
Authentication velocity
Failed login burst detection
Geographic distance between consecutive logins
Impossible travel detection
User-specific baseline login hours
User-specific baseline locations
User-specific baseline devices
Rolling failed login counts
Rolling authentication counts
IP reputation scores

These features could support more advanced AI models and hybrid anomaly detection.

Conclusion

Feature engineering is the bridge between raw authentication logs and intelligent anomaly detection.

Using Python and Pandas, the project transforms authentication events into meaningful behavioral indicators involving:

Time
Authentication status
User activity
IP behavior
Device behavior
Location behavior
Behavioral relationships

The processed feature dataset provides the foundation for the project's AI and Machine Learning layer.

The complete flow is:

Raw Logs → Feature Engineering → Behavioral Features → AI/ML → Anomaly Detection → Risk Classification → Dashboard


Save it with **Ctrl + S**. ✅

### Next file to create

```text
documentation/05_ai_ml_anomaly_detection.md