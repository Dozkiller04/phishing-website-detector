# 🛡️ Phishing Website Detector

A cybersecurity project to detect phishing websites using two approaches:
- **Rule-Based Detection**: Pattern matching on URL structure
- **Machine Learning Detection**: Logistic Regression-based trained classifier

Includes both **GUI interface** and **terminal support** for practical testing.

> 🎓 Built as part of Internship 2025 – For educational awareness only.

---

## ✨ Features

- 🔍 Detect phishing links using suspicious patterns (`@`, IPs, long URLs, etc.)
- 🤖 Machine learning model trained on URL-based features
- 🖥️ GUI support for both detection methods using `Tkinter`
- 📦 Includes terminal output version and Jupyter notebook for ML training
- ✅ Clean, educational, and open-source

---

## 📸 Screenshots

| CLI – Input Prompt | CLI – Legitimate Output |
|--------------------|-------------------------|
| ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/01_CLI_input_prompt.png.png?raw=true) | ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/02_CLI_legitimate_output.png.png?raw=true) |

| CLI – Another Input | CLI – Phishing Output |
|---------------------|------------------------|
| ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/03_CLI_input_prompt.png.png?raw=true) | ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/04_CLI_phishing_output.png.png?raw=true) |

| GUI – Input Prompt | GUI – Legitimate Output |
|--------------------|--------------------------|
| ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/05_GUI_input_prompt.png.png?raw=true) | ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/06_GUI_legitimate_output.png.png?raw=true) |

| GUI – Another Input | GUI – Phishing Output |
|---------------------|------------------------|
| ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/07_GUI_input_prompt.png.png?raw=true) | ![](https://github.com/Dozkiller04/phishing-website-detector/blob/main/Screenshots/08_GUI_phishing_output.png.png?raw=true) |

---

## 🎥 Demo Video

👉 [Click to Watch Full Demo](https://drive.google.com/file/d/1Y1tnySStdVcGIskZtcQF9knRdFD-kb/view?usp=drive_link)

> Covers rule-based detection, ML GUI detection, training model overview, and ethics.

---

## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/Dozkiller04/phishing-website-detector.git
cd phishing-website-detector
````

### 📦 Install Requirements

> 📌 Tested on Python **3.10+**

```bash
pip install -r requirements.txt
```

---

## 🖥️ Run the Application

### ▶️ Rule-Based GUI

```bash
python phishing_detector.py
```

### ▶️ ML-Based GUI

```bash
python phishing_ml_gui.py
```

### ▶️ Terminal (Rule-Based)

```bash
python phishing_detector.py
```

> Terminal output appears after entering a URL in the prompt window.

---

## 🧠 Machine Learning Details

* Model: **Logistic Regression**
* Trained on dataset with phishing and legitimate URLs
* Extracted features include:

  * Presence of `@`, `-`, or IPs
  * URL length
  * Presence of `https`
  * Number of subdomains
* Stored as: `model.pkl`

To retrain the model:

* Open `PhishingDetectionML.ipynb`
* Run all cells to generate a new `model.pkl`

---

## 📁 Folder Structure

```
phishing-website-detector/
├── phishing_detector.py          # Rule-based GUI + logic
├── phishing_ml_gui.py            # ML GUI using model.pkl
├── PhishingDetectionML.ipynb     # Jupyter notebook to train model
├── model.pkl                     # Trained logistic regression model
├── requirements.txt              # Required Python packages
├── LICENSE                       # MIT license
├── README.md                     # This file
└── Screenshots/                  # 8 screenshots
    ├── 01_rule_gui_detected.png
    ├── 02_rule_gui_legit.png
    ├── 03_ml_gui_detected.png
    ├── 04_ml_gui_legit.png
    ├── 05_terminal_rule_detected.png
    ├── 06_terminal_rule_legit.png
    ├── 07_ml_training_notebook.png
    └── 08_repo_structure.png
```

---

## 📦 Dependencies

Install all packages with:

```bash
pip install -r requirements.txt
```

### `requirements.txt` includes:

* `pandas`
* `scikit-learn`
* `tkinter` (default in Python)
* `joblib`

---

## 👨‍💻 Author

**Soham Pramod Tayade**
🎓 B.Sc. Cyber & Digital Science
🏆 RISE Internship 2025 – Final Project
🔗 GitHub: [@Dozkiller04](https://github.com/Dozkiller04)

---

## ⚖️ License

Licensed under the [MIT License](./LICENSE).

---

## ⚠️ Disclaimer

> This project is built for **educational and ethical purposes only**.
> Misuse of this tool for illegal or malicious activities is **strictly prohibited**.

