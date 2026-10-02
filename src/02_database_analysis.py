import pandas as pd
import sqlite3
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

CSV_FILE = Path("data/raw/authentication_logs.csv")
DB_FILE = Path("database/authentication.db")


def main():

    print("=" * 60)
    print("DATABASE ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. CHECK DATASET
    # --------------------------------------------------------

    if not CSV_FILE.exists():
        print(f"\nERROR: Dataset not found: {CSV_FILE}")
        return

    # Create database folder if it does not exist
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------
    # 2. LOAD DATASET
    # --------------------------------------------------------

    print("\nLoading authentication dataset...")

    df = pd.read_csv(CSV_FILE)

    print(f"Total records loaded: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    print("\nDataset columns:")
    print(df.columns.tolist())

    # --------------------------------------------------------
    # 3. CREATE SQLITE DATABASE
    # --------------------------------------------------------

    print("\nCreating SQLite database...")

    conn = sqlite3.connect(DB_FILE)

    # Save dataset into SQLite table
    df.to_sql(
        "authentication_logs",
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Database created successfully: {DB_FILE}")

    # --------------------------------------------------------
    # 4. SQL ANALYSIS - TOTAL EVENTS
    # --------------------------------------------------------

    total_events = pd.read_sql_query(
        """
        SELECT COUNT(*) AS total_events
        FROM authentication_logs
        """,
        conn
    )

    print("\n" + "-" * 60)
    print("TOTAL AUTHENTICATION EVENTS")
    print("-" * 60)

    print(total_events.to_string(index=False))

    # --------------------------------------------------------
    # 5. SQL ANALYSIS - USER ACTIVITY
    # --------------------------------------------------------

    user_analysis = pd.read_sql_query(
        """
        SELECT
            username,
            COUNT(*) AS total_logins,
            SUM(is_anomaly) AS anomaly_count
        FROM authentication_logs
        GROUP BY username
        ORDER BY anomaly_count DESC, total_logins DESC
        """,
        conn
    )

    print("\n" + "-" * 60)
    print("USER ACTIVITY ANALYSIS")
    print("-" * 60)

    print(user_analysis.to_string(index=False))

    # --------------------------------------------------------
    # 6. SQL ANALYSIS - LOGIN SUCCESS
    # --------------------------------------------------------

    success_analysis = pd.read_sql_query(
        """
        SELECT
            success,
            COUNT(*) AS total
        FROM authentication_logs
        GROUP BY success
        ORDER BY total DESC
        """,
        conn
    )

    print("\n" + "-" * 60)
    print("LOGIN SUCCESS ANALYSIS")
    print("-" * 60)

    print(success_analysis.to_string(index=False))

    # --------------------------------------------------------
    # 7. SQL ANALYSIS - ANOMALY SUMMARY
    # --------------------------------------------------------

    anomaly_analysis = pd.read_sql_query(
        """
        SELECT
            is_anomaly,
            COUNT(*) AS total_events
        FROM authentication_logs
        GROUP BY is_anomaly
        ORDER BY is_anomaly
        """,
        conn
    )

    print("\n" + "-" * 60)
    print("ANOMALY SUMMARY")
    print("-" * 60)

    print(anomaly_analysis.to_string(index=False))

    # --------------------------------------------------------
    # 8. SQL ANALYSIS - ANOMALIES BY USER
    # --------------------------------------------------------

    anomaly_by_user = pd.read_sql_query(
        """
        SELECT
            username,
            COUNT(*) AS anomaly_events
        FROM authentication_logs
        WHERE is_anomaly = 1
        GROUP BY username
        ORDER BY anomaly_events DESC
        """,
        conn
    )

    print("\n" + "-" * 60)
    print("ANOMALOUS ACTIVITY BY USER")
    print("-" * 60)

    print(anomaly_by_user.to_string(index=False))

    # --------------------------------------------------------
    # CLOSE DATABASE
    # --------------------------------------------------------

    conn.close()

    print("\n" + "=" * 60)
    print("DATABASE ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()