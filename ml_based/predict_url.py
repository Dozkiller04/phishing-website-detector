import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Ask for URL input
url = input("🔍 Enter a URL to check: ")

# Transform and predict
url_vector = vectorizer.transform([url])
prediction = model.predict(url_vector)

# Show result
if prediction[0] == 1:
    print("⚠️ Suspicious: This URL may be a phishing site!")
else:
    print("✅ Safe: This URL looks safe.")
