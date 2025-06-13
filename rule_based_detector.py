import re

def is_phishing_url(url):
    # Common phishing patterns
    suspicious_keywords=['login','verify','update','secure','banking','account']
    suspicious_domains=['.tk','.ml','.ga','.cf','.gq']
    special_chars=['@','//','-','=']

    #Heuristic Rules
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    if any(url.endswith(ext) for ext in suspicious_domains):
        return True
    if any(char in url for char in special_chars):
        return True
    if len(url)>75:
        return True
    return False

# Example
test_url = input("Enter URL: ")
if is_phishing_url(test_url):
    print("⚠️ Suspicious URL detected!")
else:
    print("✅ URL looks safe.")


