import re
import urllib.parse
import tkinter as tk
from tkinter import messagebox

# List of known legitimate domains
SAFE_DOMAINS = [
    "google.com", "github.com", "wikipedia.org", "openai.com",
    "example.com", "microsoft.com", "amazon.com", "yahoo.com"
]

# List of suspicious TLDs commonly used in phishing
SUSPICIOUS_TLDS = ['.tk', '.ml', '.ga', '.cf', '.gq']

# Keywords often found in phishing URLs
PHISHING_KEYWORDS = ['login', 'verify', 'secure', 'banking', 'account', 'update', 'signin']

# Characters that are unusual or used for redirection/obfuscation
SUSPICIOUS_CHARS = ['@', '//', '-', '=']

def is_ip_address(domain):
    return bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', domain))

def extract_domain(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.netloc or parsed_url.path
        return hostname.lower().replace("www.", "")
    except Exception:
        return ""

def is_phishing_url(url):
    domain = extract_domain(url)

    if any(domain.endswith(safe) for safe in SAFE_DOMAINS):
        return False
    if is_ip_address(domain):
        return True
    if any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS):
        return True
    if any(keyword in url.lower() for keyword in PHISHING_KEYWORDS):
        return True
    if sum(char in url for char in SUSPICIOUS_CHARS) > 2:
        return True
    if len(url) > 80:
        return True

    return False

# ============ GUI Part ============

def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if is_phishing_url(url):
        result_label.config(text="⚠️ Phishing or Suspicious URL!", fg="red")
    else:
        result_label.config(text="✅ Safe and Legitimate URL", fg="green")

# Initialize GUI window
root = tk.Tk()
root.title("🔍 Phishing Website Detector")
root.geometry("400x220")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="Phishing URL Detection Tool", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

url_entry = tk.Entry(root, width=45, font=("Arial", 11))
url_entry.pack(pady=10)
url_entry.insert(0, "https://")

check_button = tk.Button(root, text="Check URL", command=check_url, font=("Arial", 11), bg="#007acc", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
