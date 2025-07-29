import requests
import re
from datetime import datetime

INSTAGRAM_URL = "https://www.instagram.com/polarsecco/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(INSTAGRAM_URL, headers=HEADERS)
if response.status_code != 200:
    raise Exception(f"Failed to load page: {response.status_code}")

# Regex to extract follower count from JSON embedded in HTML
match = re.search(r'"edge_followed_by":{"count":(\d+)}', response.text)
if match:
    followers = match.group(1)
else:
    raise Exception("Could not find follower count")

# Save with timestamp
with open("followers_log.csv", "a") as f:
    f.write(f"{datetime.now().isoformat()},{followers}\n")
print(f"Current followers: {followers}")
