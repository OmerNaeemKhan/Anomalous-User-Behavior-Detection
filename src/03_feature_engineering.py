import os
import pandas as pd


# ============================================================
# PATH CONFIGURATION
# ============================================================

INPUT_FILE = "data/raw/authentication_logs.csv"
OUTPUT_FILE = "data/processed/authentication_features.csv"


# ============================================================
# FEATURE ENGINEERING FUNCTION
# ============================================================

def create_features(df):
    """
    Create features from authentication logs for anomaly detection.
    """

    # Make a copy so the original dataframe is unchanged
    df = df.copy()

    # --------------------------------------------------------
    # CONVERT TIMESTAMP
    # --------------------------------------------------------

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # --------------------------------------------------------
    # TIME-BASED FEATURES
    # --------------------------------------------------------

    df["login_hour"] = df["timestamp"].dt.hour

    df["day_of_week"] = df["timestamp"].dt.dayofweek

    df["day_name"] = df["timestamp"].dt.day_name()

    df["is_weekend"] = (
        df["day_of_week"] >= 5
    ).astype(int)

    # Night login: between 10 PM and 6 AM
    df["is_night_login"] = (
        (df["login_hour"] >= 22)
        | (df["login_hour"] <= 6)
    ).astype(int)

    # --------------------------------------------------------
    # LOGIN STATUS FEATURES
    # --------------------------------------------------------

    # Convert success column to integer
    df["success"] = df["success"].astype(int)

    # Failed login indicator
    df["failed_login"] = (
        df["success"] == 0
    ).astype(int)

    # Successful login indicator
    df["successful_login"] = (
        df["success"] == 1
    ).astype(int)

    # --------------------------------------------------------
    # USER ACTIVITY FEATURES
    # --------------------------------------------------------

    # Total number of authentication events per user
    df["user_login_count"] = (
        df.groupby("username")["event_id"]
        .transform("count")
    )

    # Total failed login attempts per user
    df["user_failed_login_count"] = (
        df.groupby("username")["failed_login"]
        .transform("sum")
    )

    # Failed login rate per user
    df["user_failed_login_rate"] = (
        df["user_failed_login_count"]
        / df["user_login_count"]
    )

    # --------------------------------------------------------
    # IP ADDRESS FEATURES
    # --------------------------------------------------------

    # Number of times each IP address appears
    df["ip_login_count"] = (
        df.groupby("ip_address")["event_id"]
        .transform("count")
    )

    # Number of unique users per IP address
    df["ip_unique_users"] = (
        df.groupby("ip_address")["username"]
        .transform("transform")
        if False
        else df.groupby("ip_address")["username"]
        .transform("nunique")
    )

    # --------------------------------------------------------
    # DEVICE FEATURES
    # --------------------------------------------------------

    # Number of times each device appears
    df["device_login_count"] = (
        df.groupby("device")["event_id"]
        .transform("count")
    )

    # Number of unique users using each device
    df["device_unique_users"] = (
        df.groupby("device")["username"]
        .transform("nunique")
    )

    # --------------------------------------------------------
    # LOCATION FEATURES
    # --------------------------------------------------------

    # Number of logins from each location
    df["location_login_count"] = (
        df.groupby("location")["event_id"]
        .transform("count")
    )

    # Number of unique users per location
    df["location_unique_users"] = (
        df.groupby("location")["username"]
        .transform("nunique")
    )

    # --------------------------------------------------------
    # USER + IP COMBINATION
    # --------------------------------------------------------

    # How many times a user has used the same IP address
    df["user_ip_count"] = (
        df.groupby(["username", "ip_address"])["event_id"]
        .transform("count")
    )

    # --------------------------------------------------------
    # USER + DEVICE COMBINATION
    # --------------------------------------------------------

    # How many times a user has used the same device
    df["user_device_count"] = (
        df.groupby(["username", "device"])["event_id"]
        .transform("count")
    )

    # --------------------------------------------------------
    # USER + LOCATION COMBINATION
    # --------------------------------------------------------

    # How many times a user has logged in from same location
    df["user_location_count"] = (
        df.groupby(["username", "location"])["event_id"]
        .transform("count")
    )

    return df


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print("=" * 60)
    print("AUTHENTICATION LOG FEATURE ENGINEERING")
    print("=" * 60)

    # --------------------------------------------------------
    # CHECK INPUT FILE
    # --------------------------------------------------------

    if not os.path.exists(INPUT_FILE):
        print(f"\nERROR: Input file not found: {INPUT_FILE}")
        return

    # --------------------------------------------------------
    # LOAD DATASET
    # --------------------------------------------------------

    print(f"\nLoading dataset from: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print(f"Original dataset shape: {df.shape}")

    print("\nOriginal columns:")
    print(df.columns.tolist())

    # --------------------------------------------------------
    # CREATE FEATURES
    # --------------------------------------------------------

    print("\nCreating anomaly detection features...")

    df_features = create_features(df)

    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("FEATURE ENGINEERING RESULTS")
    print("-" * 60)

    print(f"\nFinal dataset shape: {df_features.shape}")

    print("\nFinal columns:")
    print(df_features.columns.tolist())

    print("\nDataset preview:")
    print(df_features.head().to_string())

    # --------------------------------------------------------
    # FEATURE SUMMARY
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("FEATURE SUMMARY")
    print("-" * 60)

    feature_columns = [
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

    for feature in feature_columns:
        print(f"\n{feature}:")
        print(df_features[feature].describe())

    # --------------------------------------------------------
    # CREATE OUTPUT DIRECTORY
    # --------------------------------------------------------

    output_directory = os.path.dirname(OUTPUT_FILE)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # --------------------------------------------------------
    # SAVE PROCESSED DATASET
    # --------------------------------------------------------

    df_features.to_csv(OUTPUT_FILE, index=False)

    print("\n" + "=" * 60)
    print("FEATURE ENGINEERING COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"\nOriginal records: {len(df)}")
    print(f"Processed records: {len(df_features)}")
    print(f"Total columns: {len(df_features.columns)}")
    print(f"\nSaved to: {OUTPUT_FILE}")


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()