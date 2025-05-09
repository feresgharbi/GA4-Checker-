# GA4 Presence Checker 🕵️‍♂️

A Python script that crawls through a website and checks whether [Google Analytics 4 (GA4)] tracking code is present on each page. It helps you quickly identify which pages are missing GA4 integration.

## 🚀 Features

- Crawls internal links from a starting URL
- Detects GA4 by scanning for:
  - `gtag('config', 'G-XXXXXXXXXX')`
  - `https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX`
- Outputs a list of pages where GA4 is **missing**
- Console output with clear ✅/❌ indicators

## 📌 Requirements

- Python 3.7+
- Install required packages:

```bash
pip install -r requirements.txt

