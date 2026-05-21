# Starlink Daily Data Usage Scraper

Scrapes daily data usage from your Starlink account and saves it to a CSV file.

---

## Requirements

- Python 3.x
- An active Starlink account
- Be logged into Starlink on your browser before running the script

Install dependencies:

```bash
pip install requests certifi
```

---

## Setup

### 1. Find your Account and Service Line IDs

Log into Starlink and go to your usage page. The URL will look like:

```
https://starlink.com/account/service-line/AST-XXXXXXX-XXXXX-XX?selectedDevice=...
```
**No need to update your URL in the .py file**

Open `WebScraper.py` and update these two values at the top of the file:

```python
ACCOUNT_ID = "ACC-XXXXXXX-XXXXX-XX"       # your account number
SERVICE_LINE_ID = "AST-XXXXXXX-XXXXX-XX"  # from the URL
```

### 2. Set your ACCESS TOKEN

Needs to manually input the cookies from your browser where you have the page logged in.

Right click to inspect the Data Usage section, look for the 'Application' tab, Dropdown 'Cookies', head to 'Starlink.Com.Access.V1' in the table. 

Make sure to copy the entire cookie line by double tapping the section.

Update this line in `WebScraper.py`:

```python
ACCESS_TOKEN = "PLACE YOUR COOKIE HERE"
```


---

## Running the Script
Run the script:

```bash
python WebScraper.py
```

**Mac / Linux:**

```bash
sudo python3 WebScraper.py
```

---

## Output

The script produces two files:

- `starlink_data.json` — raw API response (for reference)
- `starlink_daily_usage.csv` — daily usage data with two columns:

```
Date,Data Usage
2025-11-17,??? GB
2025-11-18,??? GB
2025-11-19,??? GB
...
```

---

## Troubleshooting

**401 Unauthorized**
Your session cookies have expired. Log back into Starlink in your browser, update the cookies for the ACCESS TOKEN section and run the script again immediately.


---

## requirements.txt

```
requests
certifi
```
