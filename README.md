# Chart# Daily Log

A small automated repo that fetches a quote every day and commits it to `log/YYYY-MM-DD.md`.

## How it works

- `script.py` fetches a random quote from [ZenQuotes](https://zenquotes.io) (falls back to a hardcoded quote if the API is unreachable) and writes it to today's dated file.
- `.github/workflows/daily-quote.yml` runs the script once a day via GitHub Actions and pushes the commit automatically — no server or local machine needed.

## Setup

1. Create a new **public** GitHub repo (private repos work too, but only show on your graph if "Include private contributions" is enabled in your profile settings).
2. Copy these files into it:
   - `script.py`
   - `.github/workflows/daily-quote.yml`
   - `README.md`
3. Push to GitHub.
4. Go to the repo's **Settings → Actions → General** and make sure "Read and write permissions" is enabled for the `GITHUB_TOKEN` (needed for the workflow to push).
5. That's it — the workflow runs daily on the schedule in the `.yml` file. You can also trigger it manually anytime from the **Actions** tab ("Run workflow").

## Customizing

- Change the run time by editing the `cron` line in the workflow file (times are UTC).
- Swap `fetch_quote()` in `script.py` for any other daily content you'd like to log (a fact, a stat, weather, etc.).
