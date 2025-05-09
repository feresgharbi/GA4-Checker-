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

🛠 Usage
Clone the repository or download the script.

Run the script:

bash
Copier
Modifier
python check_ga4.py
Enter the required input when prompted:

mathematica
Copier
Modifier
Enter the base URL (e.g., https://example.com):
Max pages to scan (e.g., 50):
Wait for the results. You'll see:

✅ GA4 found: <page URL>

❌ GA4 NOT found: <page URL>

At the end, it prints a full list of pages without GA4.

📝 Example Output
arduino
Copier
Modifier
[✅] GA4 found: https://example.com
[✅] GA4 found: https://example.com/about
[❌] GA4 NOT found: https://example.com/contact

=== Pages Without GA4 ===
https://example.com/contact
⚠️ Notes
This is a basic crawler and follows internal links up to a given limit.

Does not obey robots.txt.

May not detect GA4 if loaded dynamically via JavaScript frameworks or Tag Managers without standard patterns.

📄 License
MIT License. Feel free to use and modify.
