# Daily Log

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

## Author

Created and maintained by [@ygangeshwar954-max](https://github.com/ygangeshwar954-max).

## License

MIT License

Copyright (c) 2026 ygangeshwar954-max

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
