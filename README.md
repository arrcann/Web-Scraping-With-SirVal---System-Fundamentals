# Starlink Daily Data Usage Scraper

Scrapes daily data usage from your Starlink account and saves it to a CSV file.

---

## Requirements

- Python 3.x
- An active Starlink account
- Be logged into Starlink on your browser before running the script

Install dependencies:

```bash
pip install requests certifi browser-cookie3
```

---

## Setup

### 1. Find your Account and Service Line IDs

Log into Starlink and go to your usage page. The URL will look like:

```
https://starlink.com/account/service-line/AST-XXXXXXX-XXXXX-XX?selectedDevice=...
```

Open `WebScraper.py` and update these two values at the top of the file:

```python
ACCOUNT_ID = "ACC-XXXXXXX-XXXXX-XX"       # your account number
SERVICE_LINE_ID = "AST-XXXXXXX-XXXXX-XX"  # from the URL
```

### 2. Set your browser

The script reads cookies directly from your browser so you don't have to copy anything manually. Find your browser in the list below and update this line in `WebScraper.py`:

```python
cookies = browser_cookie3.chrome(domain_name="starlink.com")
```

| Browser | Code |
|---|---|
| Chrome | `browser_cookie3.chrome(domain_name="starlink.com")` |
| Firefox | `browser_cookie3.firefox(domain_name="starlink.com")` |
| Edge | `browser_cookie3.edge(domain_name="starlink.com")` |
| Opera | `browser_cookie3.opera(domain_name="starlink.com")` |
| Opera GX | `browser_cookie3.opera_gx(domain_name="starlink.com")` |
| Brave | `browser_cookie3.brave(domain_name="starlink.com")` |
| Chromium | `browser_cookie3.chromium(domain_name="starlink.com")` |

### 3. (Optional) Set cookie file path manually

If the script can't find your cookies automatically, you can point it to the cookie file directly.

**How to find your cookie file:**

| Browser | Default cookie file location |
|---|---|
| Chrome (Windows) | `C:\Users\<you>\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies` |
| Chrome (Mac) | `~/Library/Application Support/Google/Chrome/Default/Cookies` |
| Chrome (Linux) | `~/.config/google-chrome/Default/Cookies` |
| Edge (Windows) | `C:\Users\<you>\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies` |
| Opera GX (Windows) | `C:\Users\<you>\AppData\Roaming\Opera Software\Opera GX Stable\Default\Network\Cookies` |
| Firefox (Windows) | `C:\Users\<you>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\cookies.sqlite` |

Then pass it in like this:

```python
cookies = browser_cookie3.chrome(
    cookie_file=r"C:\Users\<you>\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies",
    domain_name="starlink.com"
)
```

---

## Running the Script

> **Important:** On Windows you must run as Administrator so the script can access browser cookies.

**Windows — run as admin:**

1. Press the Windows key, search for **Command Prompt** or **PowerShell**
2. Right-click → **Run as administrator**
3. Navigate to the project folder:

```bash
cd path\to\your\project
```

4. Run the script:

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
Your session cookies have expired. Log back into Starlink in your browser and run the script again immediately.

**Failed to find cookies for browser**
- Make sure you are using the correct browser function (see Setup Step 2)
- Try setting the cookie file path manually (see Setup Step 3)
- Make sure you are running as Administrator (Windows) or with `sudo` (Mac/Linux)

**Empty CSV**
The JSON structure may have changed. Open `starlink_data.json` and check if `billingCyclesAnnotated` exists inside `content`.

---

## requirements.txt

```
requests
certifi
browser-cookie3
```
