"""
Fetches a daily quote and appends it to a dated log file.
Designed to be run once per day by GitHub Actions.
"""

import os
import datetime
import urllib.request
import json

LOG_DIR = "log"


def fetch_quote():
    """Fetch a random quote from a free public API, with a local fallback."""
    try:
        req = urllib.request.Request(
            "https://zenquotes.io/api/random",
            headers={"User-Agent": "daily-log-bot"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            quote = data[0]["q"]
            author = data[0]["a"]
            return quote, author
    except Exception as e:
        print(f"API fetch failed ({e}), using fallback quote.")
        return "The only way to do great work is to love what you do.", "Steve Jobs"


def main():
    os.makedirs(LOG_DIR, exist_ok=True)

    today = datetime.date.today().isoformat()
    filepath = os.path.join(LOG_DIR, f"{today}.md")

    if os.path.exists(filepath):
        print(f"Entry for {today} already exists, skipping.")
        return

    quote, author = fetch_quote()

    with open(filepath, "w") as f:
        f.write(f"# {today}\n\n")
        f.write(f"> {quote}\n>\n> — {author}\n")

    print(f"Wrote entry for {today}.")


if __name__ == "__main__":
    main()
