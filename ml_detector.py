import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Step 1: Load Dataset
df = pd.read_csv("data/phishing_dataset.csv", header=None, names=["url", "label"])

# Step 2: Convert labels
label_mapping = {
    "benign": 0,
    "phishing": 1,
    "malware": 1
}
df["label"] = df["label"].map(label_mapping)

# 🧹 Drop rows where label couldn't be mapped (NaN)
df.dropna(subset=["label"], inplace=True)
df["label"] = df["label"].astype(int)


# Step 3: Feature extraction from URL using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["url"])
y = df["label"]

# Step 4: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc:.2f}")

# Step 7: Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
