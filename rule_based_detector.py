import re

def is_phishing_url(url):
    # Whitelist: Known legitimate websites
    safe_domains = [
        "google.com", "github.com", "wikipedia.org", "example.com",
        "openai.com", "python.org", "microsoft.com"
    ]

    # Check if URL contains any safe domain
    for domain in safe_domains:
        if domain in url.lower():
            return False

    # Common phishing patterns
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'banking', 'account']
    suspicious_domains = ['.tk', '.ml', '.ga', '.cf', '.gq']
    special_chars = ['@', '//', '-', '=']

    # Heuristic Rules
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    if any(url.endswith(ext) for ext in suspicious_domains):
        return True
    if any(char in url for char in special_chars):
        return True
    if len(url) > 75:
        return True

    return False

# === Main Program ===
test_url = input("🔍 Enter URL: ")
if is_phishing_url(test_url):
    print("⚠️ Suspicious or Phishing URL Detected!")
else:
    print("✅ This URL looks Legitimate.")
