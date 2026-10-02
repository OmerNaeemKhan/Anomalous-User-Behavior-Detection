import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# ============================================================
# SMALL AUTHENTICATION LOG DATASET GENERATOR
# ============================================================

random.seed(42)
np.random.seed(42)

OUTPUT_FILE = "data/raw/authentication_logs.csv"

os.makedirs("data/raw", exist_ok=True)

users = [
    "alice", "bob", "charlie", "david", "emma",
    "frank", "grace", "henry", "isabella", "jack"
]

normal_ips = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.20",
    "192.168.1.25",
    "192.168.1.30",
]

suspicious_ips = [
    "185.220.101.1",
    "45.33.32.156",
    "91.108.4.20",
]

locations = {
    "192.168.1.10": "New York, USA",
    "192.168.1.15": "New York, USA",
    "192.168.1.20": "Chicago, USA",
    "192.168.1.25": "Chicago, USA",
    "192.168.1.30": "Boston, USA",
    "185.220.101.1": "Unknown",
    "45.33.32.156": "Foreign Location",
    "91.108.4.20": "Foreign Location",
}

devices = ["Windows", "MacOS", "Linux"]

records = []

start_date = datetime(2026, 8, 1, 8, 0, 0)

# ------------------------------------------------------------
# CREATE NORMAL AUTHENTICATION EVENTS
# ------------------------------------------------------------

for i in range(950):
    user = random.choice(users)

    timestamp = start_date + timedelta(
        minutes=random.randint(0, 60 * 24 * 14)
    )

    hour = timestamp.hour

    ip_address = random.choice(normal_ips)
    location = locations[ip_address]
    device = random.choice(devices)

    success = 1 if random.random() < 0.97 else 0

    records.append({
        "event_id": i + 1,
        "timestamp": timestamp,
        "username": user,
        "ip_address": ip_address,
        "location": location,
        "device": device,
        "login_hour": hour,
        "success": success,
        "is_anomaly": 0
    })


# ------------------------------------------------------------
# CREATE ANOMALOUS AUTHENTICATION EVENTS
# ------------------------------------------------------------

for i in range(50):
    user = random.choice(users)

    # Suspicious late-night / early-morning login
    day_offset = random.randint(0, 13)
    hour = random.choice([0, 1, 2, 3, 4, 23])

    timestamp = start_date + timedelta(
        days=day_offset,
        hours=hour,
        minutes=random.randint(0, 59)
    )

    ip_address = random.choice(suspicious_ips)
    location = locations[ip_address]

    records.append({
        "event_id": 951 + i,
        "timestamp": timestamp,
        "username": user,
        "ip_address": ip_address,
        "location": location,
        "device": random.choice(devices),
        "login_hour": hour,
        "success": random.choice([0, 0, 0, 1]),
        "is_anomaly": 1
    })


# ------------------------------------------------------------
# SAVE DATASET
# ------------------------------------------------------------

df = pd.DataFrame(records)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv(OUTPUT_FILE, index=False)

print("=" * 60)
print("AUTHENTICATION DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal records: {len(df)}")
print(f"Normal events: {(df['is_anomaly'] == 0).sum()}")
print(f"Anomalous events: {(df['is_anomaly'] == 1).sum()}")

print("\nDataset preview:")
print(df.head())

print(f"\nSaved to: {OUTPUT_FILE}")