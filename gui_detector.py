import tkinter as tk
from tkinter import messagebox
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Detect phishing
def detect_url():
    url = url_entry.get()
    if url == "" or url == "Enter URL here...":
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    url_vector = vectorizer.transform([url])
    prediction = model.predict(url_vector)

    if prediction[0] == 1:
        result_label.config(text="⚠️ This URL is Phishing!", fg="red")
    else:
        result_label.config(text="✅ This URL is Safe.", fg="green")

# Clear placeholder on click
def on_click(event):
    if url_entry.get() == "Enter URL here...":
        url_entry.delete(0, tk.END)
        url_entry.config(fg="black")

# GUI setup
window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("400x200")
window.resizable(False, False)

title_label = tk.Label(window, text="Phishing URL Detector", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

url_entry = tk.Entry(window, width=50, fg="grey")
url_entry.insert(0, "Enter URL here...")
url_entry.bind("<FocusIn>", on_click)
url_entry.pack(pady=5)

check_button = tk.Button(window, text="Check URL", command=detect_url)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
