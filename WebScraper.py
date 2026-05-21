import requests
import certifi
import csv
import json
import browser_cookie3
from datetime import datetime, timedelta

ACCOUNT_ID = "ACC-2735603-74738-20"
DEVICE_ID = "AST-2293597-46342-54"

ACCESS_TOKEN = "CfDJ8B0rUwu9drZBtlp6Z3PrbGW8dM25QgjyMyroVxApOaywC0ydg9k80ww8XrgoYNHelgT7uqIOy4zCMer7zrARO9yGektdlm20O2cMcDSgP8MYfk8w4W2HzvUu2fyYzfNepbWjTQDFqzmqTa7wYtUXaZVg7SE-4-euJe4peygHrCvP1Acmwzh3X8I05WwmkL7t6AEJo5FeYImynLArSs38YLSPQcS64aviU0Q25LK-4VuZDp_UpJZuBy3tBjib5s0FWmiUkhqoV3ZVcdj8lO0FZwWAblKevwP0dq_yACYk8wBgpkRFCSJgwu6aMd3LzjP4L0otmtA2DgyeghjPqE8krZQvdWM0RhjxUfKklla9qhACQ3i35BebTgz9Ka8JVpauKnjCFc964Y6hOW6VCINUrVEgXIvIVYZItgMHb3vpNiB0ef-ih2AN2e5KVCOrNrxHEnY6cXjK_an8mHE_3v4_nGFjFggGFZAVLw1FnLFKDzlnEo8kwQYp7ip4SZYq0lyT2zADSjbrEwm9A5RXVpV-WiyMxDUZiKlCUTr1Y1hTcSNgT-f695MLOCG0SrmhYLVwVqvnp0EfAUJWZpviFOBMTRPtEjXaaTzY5swC-D9rZJ3S6RUgG2um8iJta9d04oaVDhuuL_JNKReLCJLj1JQdtnu1doR7jIuOnyBZ-B8X-jo3t9MWfIkkQHnr-lI4qgrhVT-RivlCDZ6mjWzEbootV0zaqC9KA8i1VdbHlUTVL4kJ-uXgZ3vQ2zSjNBhoogKdnAo3hLr1paMZMz-j22Q-YahtJulqJKNedusIXFn9UlyL3oSII62NeY0sUhQdTmgYH3H-4UCwrGu0MmHZpkSBOxu0FrxR_dyWHscEo67nbLBk9BQVxxxjZkfdTjE8Sj4eq-dPc2KblOXf6WxGrUuvnadHLoc3jvNHwRqxKG3eeBQG7D4NgPcRdBxvsc5dF50aJK3qa0D0rv8KFQahp2zWmNiu5oe5gQ5bjQe2hxRaSOyb1Ug52r3gtYYMlIQKk0Dn9roOwHkJU-yrjx4Z13FN7bQKTnvCME63ytM--O4dNzQURJlsyvW9hhakJqWez4f3Ao9DwXYUCr73nc2RHhl9xkC5_d40svxxeSRJE4lbC2sGVKhi7sC--tXqi-nHvjeeBRniEJPdHhZRE1nGOE5bGIc5igLxFnjCJYeodZZF4QOxXKyN05sogU8Sp-Pv3qrB7V5cQn4XIVIYAg5wVjqVx9aRWqeF6q3uEDxyfglb8RnDFpsYATO6mRzQRS9v9ElE2hQHnNDoRP1hNoOYYtm-wns5PE-Etnafvl_bGe6YYZEogHhx5XVE_9uh5PB9WbWC23Fd1LKJwxh_HwXagiaBj499ciQT505h6p43ZtLLI8dfogrD4Cc_5WdJRi1b2T0K-_ZqyxkNueECGhcFOsYzGYQqE9zgs_s1U_CAcDytgOgH0kM7pX3HLEr59JFkU7CuF3iYuAK41rRpp1j9hi8Ed7RQ-jINLLhiN8rLbDgwoqpPtbCDhpW27XoTHCgMn5VKBqdBIvqiv1sAPCIuIAIcbfaUIbkPR3zxvkFRn6X2tmXAx2EiMpaKspNgSLmSvzYVaj8aImoKMFLThld1SrhtQVzTddRNbqsI6yjqchlk2pK8ptmsRqX_43I0ygGy5iYuFa_7qT26XQ-lwE3wdueoHsW-pD1Ssuxs9F0E8KbtjvaPjAamppoozDaCwbBcARAlbCAaOe2iloo-_0-oxbiAXnGYRkyrxYcGe7PJSLyY-VFi0PVyr58-mBEMqzXqfbTbTRWDNmJn9npJcZ7Z2Ox7a2NfYlFFzlYVahPLZTm30NM1XSNG34C4q01G6oKaRl_NXqBGBDF-v50IjS5KZ8t00JbdnU15jY0WONVdZTQ0T7k27xBL6L_sjNqtjCx2Ulb_QaVShW8hYJzMHKOnihAdKr-EVRoDy-6G1idfIEheW51NlLnKFWrnGm04J16qoaVuWJrtBFgeYou5X7l7lr5zJpNOnYQkpR_oeVu9VhoaQwwzryr42_uJVWvQpocpLTox1SrxO0fdNxKc8Yc9yfVfWA70LQLKIz0RAC1ffmNi80bMtiIY0eTzOauj3b_Hzidkbu0lKqAwf36EB2AauGOzufPR1xnDRx4eRV9XvIrjeGidMDJX6X1CxlT_JgNHBRcvFQlBuc5tCsmtk-UV1sDSkHs1mHoUodHHYDn3Me-_M1Xr-fy14h-1c62rGgXzqf9kEN9QLAI3LafbCYL8YjmfCDtmDSN3HJoQymJCRAk3ozzPpYC3BOh-u-SgMCHbWu3p83P55lYHOL0qjZB8pHBuA8xZP9WQ-Cwm3FoVjliZv6ca4wzSxrPTQboh6DFLYr1tXIRcp28C32joAbdlKLUB1HTpNnrn7W_SIcegTFhUBCKHW4ZWnEWC9zCjhU9RQmXmTzneFKf4MMcDE1JuCchxhIuhUiQVNFkaAtYJfqigAzQtijgelhW7UHtKdPh70PjEezFtxuRAVFFWx7jA8PxLPKwJ7F3ev-hlX-9Wh2ndOYkiSs_KBZ91qdP-KCsRq9uaSJgyFMNi3-Fw_9UnSzH9VUAPPfjyDA26r4RHyfcIpfcyDnC-rMgJEr6h4b-QhooFTdg4G6bq78Myd1jq-QLTvUTtl3qzN409yA0f-2VOaoE9URHRNuxJc1xZgLVAGdI58_m40y-xhj7hAvi5v6J7Xv-aiaYgLanb0VoHp1eQJMRapGmMzI2YDl2YvYdohn_09_yfYFeFhYJSCZfyr5Ju8prCp3Nz5vIoi2PC0k5xv3SNskRXdEjwpyt1SJ56qRbpytDFtSjCGdmZ6_XuaEkfd6AZeYpSsKB9SCMt7vn3PkrXJaBKQrep_f0_jKzrp8sOupiuziVGXt3N9AsxhoayAEmggJ--HqX1oZ5YwAs425CY8H036BOOyfuSxgXVTCqvYL6F5Ww01LiPqYT6QalP1c-2qloBwruGNMMtfq62LrWpGwDGHxR5bwGo4Z3em1FQIrhSVyc6SbgSVEeIa5PYD94T-KDOkZ-MrCMU9kdrINlOGOoAnCSN4PZhxPlceCnr6bvI0SpErEHwdaHOcZDy6vxg3KW4XwpunD7aPV7Ufvd3WKIkjgg3T-Vv4ioQpSqrS2tMVThD04BP15XbskGuyOA3Sj25XTkR8Scocw-BWiOm9vikR65s4NfsOZVy4WT1rg"



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