import requests
import re
from datetime import datetime

url = "https://socialblade.com/instagram/user/polarsecco"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
response.raise_for_status()

# Regex to find the follower count in the HTML
match = re.search(r"Followers</span></div>\s*<span[^>]*>([\d,]+)</span>", response.text)
if not match:
    raise Exception("Could not find follower count")

followers = match.group(1).replace(",", "")

# Write to CSV (append; create file and header if not exist)
csv_file = "followers_log.csv"
try:
    with open(csv_file, "x") as f:
        f.write("Timestamp,Followers\n")
except FileExistsError:
    pass

with open(csv_file, "a") as f:
    f.write(f"{datetime.now().isoformat()},{followers}\n")

print(f"Current followers: {followers}")
