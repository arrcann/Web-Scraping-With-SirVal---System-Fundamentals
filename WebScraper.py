import requests
import certifi
import csv
import json
import browser_cookie3
from datetime import datetime, timedelta

ACCOUNT_ID = "XXX-XXXXXXX-XXXXX-XX"
DEVICE_ID = "XXX-XXXXXXX-XXXXX-XX"

ACCESS_TOKEN = "YOUR COOKIE HERE"


url = f"https://starlink.com/api/telemetryagg/v1/data-usage/account/{ACCOUNT_ID}/service-line/{DEVICE_ID}/annotated"

session = requests.Session()

session.cookies.update({
    "Starlink.Com.Access.V1": ACCESS_TOKEN

})


response = session.get(url)

if response.status_code == 200:
    payload = response.json()

    with open("starlink_data.json", "w") as f:
        json.dump(payload, f, indent=2)

    extracted_rows = []
    billing_cycles = payload.get("content", {}).get("billingCyclesAnnotated", [])

    for cycle in billing_cycles:
        start_date = datetime.strptime(cycle["startDate"].split("T")[0], "%Y-%m-%d")
        for index, usage_wrapper in enumerate(cycle.get("dailyData", [])):
            current_day = (start_date + timedelta(days=index)).strftime("%Y-%m-%d")
            gb_value = round(usage_wrapper[0], 2) if usage_wrapper else 0.0
            extracted_rows.append([current_day, f"{gb_value} GB"])

    with open("starlink_daily_usage.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Data Usage"])
        writer.writerows(extracted_rows)

    print(f"Done! {len(extracted_rows)} rows saved to starlink_daily_usage.csv")
else:
    print(f"Failed: {response.status_code}")