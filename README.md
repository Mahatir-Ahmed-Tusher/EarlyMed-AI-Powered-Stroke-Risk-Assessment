![logo](https://github.com/user-attachments/assets/70ddc336-ded0-43e1-9982-3a26d0740b5a)

# EarlyMed: AI-Powered Stroke Risk Assessment 🏥🧠

## Overview

**EarlyMed: AI-Powered Stroke Risk Assessment** is a side project of **EarlyMed**, an initiative by our team at **VIT-AP University** dedicated to empowering individuals with early health insights. Leveraging AI for early detection, our mission is simple: **"Early Detection, Smarter Decision."**

This project provides a predictive model for assessing stroke risk using machine learning. It estimates:
- **Binary Classification:** Whether a person is at risk of a stroke (Yes/No).
- **Regression Analysis:** The probability percentage of stroke occurrence.

Our goal is to help users make informed decisions before consulting a doctor.

## 🚀 Live Demo

Try the **EarlyMed Stroke Risk Prediction Tool** on Hugging Face: [Click Here](https://huggingface.co/spaces/MahatirTusher/EarlyMed-Stroke-Risk-Prediction)

![image](https://github.com/user-attachments/assets/4802cd4b-8496-4ffa-b1a0-7181bcb757b6)


---

## 📊 Dataset

The dataset used for this model is available on Kaggle: [Stroke Risk Prediction Dataset](https://www.kaggle.com/datasets/mahatiratusher/stroke-risk-prediction-dataset/data).

### 🔬 Features of the Dataset
Each record represents an individual’s medical condition, symptoms, and risk assessment.

#### 1️⃣ Symptoms (Primary Predictors)
These binary features (1 = Present, 0 = Absent) significantly influence stroke risk:
- Chest Pain
- Shortness of Breath
- Irregular Heartbeat
- Fatigue & Weakness
- Dizziness
- Swelling (Edema)
- Pain in Neck/Jaw/Shoulder/Back
- Excessive Sweating
- Persistent Cough
- Nausea/Vomiting
- High Blood Pressure
- Chest Discomfort (Activity)
- Cold Hands/Feet
- Snoring/Sleep Apnea
- Anxiety/Feeling of Doom

#### 2️⃣ Target Variables (Predicted Outcomes)
- **At Risk (Binary):** 1 if the person is at risk of stroke, 0 otherwise.
- **Stroke Risk (%):** Estimated probability of stroke occurrence (0-100).

### 📜 Dataset Generation Process
The dataset was created using medical literature, expert consultations, and statistical modeling. Feature distributions were inspired by real-world clinical observations to ensure validity.

### 📖 Medical References & Sources
- American Stroke Association (ASA)
- Mayo Clinic & Cleveland Clinic
- "Harrison’s Principles of Internal Medicine" (20th Edition)
- "Stroke Prevention, Treatment, and Rehabilitation" (Oxford University Press, 2021)
- "The Stroke Book" (Cambridge Medicine, 2nd Edition)
- World Health Organization (WHO) Reports on Stroke Risk and Prevention

---

## 🏗️ How It Works

### 🔍 **Functionality**
1. The user inputs their symptoms and medical details.
2. The model processes the inputs and predicts:
   - **Binary Classification:** Whether the user is at risk of stroke.
   - **Risk Percentage:** The likelihood of a stroke occurring.
3. The results help users understand their potential risk and take early action.

   ![image](https://github.com/user-attachments/assets/8bd51bb1-ac5b-4821-a824-2ce8d2a8a487)


### ⚙️ **Technology Stack**
- **Machine Learning Framework:** TensorFlow
- **Model Type:** Classification & Regression (Stroke Risk Prediction)
- **Backend:** Gradio
- **Frontend:**  Python Gradio
- **Deployment:** Hosted on Hugging Face Spaces

---

## 📊 Model Performance & Results

## Regression Performance

### Random Forest (Regression)
| Metric                    | Value |
|---------------------------|-------|
| Mean Absolute Error (MAE) | 2.144 |
| Root Mean Squared Error (RMSE) | 2.706 |
| R2 Score                  | 0.964 |

### XGBoost (Regression)
| Metric                    | Value |
|---------------------------|-------|
| Mean Absolute Error (MAE) | 1.076 |
| Root Mean Squared Error (RMSE) | 1.350 |
| R2 Score                  | 0.991 |

### Discussion
- **XGBoost significantly outperforms Random Forest** in regression tasks, with a **lower MAE and RMSE**, indicating that it provides more precise predictions.
- The **R2 Score for XGBoost is 0.991**, showing that the model explains almost all the variance in stroke risk percentage, compared to **0.964 for Random Forest**.

## Binary Classification Performance

### Random Forest (Binary Classification)
| Metric      | Value  |
|------------|--------|
| Accuracy   | 0.948  |
| Precision  | 0.954  |
| Recall     | 0.967  |
| AUC        | 0.991  |

#### Classification Report
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.94      | 0.91   | 0.92     | 4892    |
| 1     | 0.95      | 0.97   | 0.96     | 9108    |
| **Overall** | **0.95** | **0.95** | **0.95** | **14000** |

#### Confusion Matrix
| Actual \ Predicted | 0   | 1   |
|--------------------|-----|-----|
| 0                 | 4465 | 427 |
| 1                 | 299  | 8809 |

### XGBoost (Binary Classification)
| Metric      | Value  |
|------------|--------|
| Accuracy   | 0.997  |
| Precision  | 0.997  |
| Recall     | 0.998  |
| AUC        | 0.999  |

#### Classification Report
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.99   | 1.00     | 4892    |
| 1     | 1.00      | 1.00   | 1.00     | 9108    |
| **Overall** | **1.00** | **1.00** | **1.00** | **14000** |

#### Confusion Matrix
| Actual \ Predicted | 0   | 1   |
|--------------------|-----|-----|
| 0                 | 4865 | 27  |
| 1                 | 15   | 9093 |

### Discussion
- **XGBoost shows exceptional performance** in binary classification, achieving almost perfect scores across all metrics.
- Compared to Random Forest, **XGBoost has significantly higher accuracy (0.997 vs 0.948), recall (0.998 vs 0.967), and AUC (0.999 vs 0.991)**.
- The **confusion matrix for XGBoost is near perfect**, with only **42 misclassifications out of 14,000 predictions**, compared to **726 misclassifications by Random Forest**.
- **This makes XGBoost the preferred model** for both stroke risk classification and regression tasks.

---

## 🔴 What to Do If Your Stroke Risk Is High?

- **Stay Calm:** This tool is an early prediction system, not a medical diagnosis.
- **Consult a Doctor:** If your risk percentage is high, consult a healthcare professional immediately.
- **Monitor Your Health:** Keep track of symptoms and maintain a healthy lifestyle.
- **Follow Medical Advice:** Take necessary precautions as suggested by medical experts.

---

## 💻 Installation & Usage

### 🔹 Clone the Repository
```bash
git clone https://github.com/Mahatir-Ahmed-Tusher/EarlyMed-Stroke-Risk-Assessment.git
cd EarlyMed-Stroke-Risk-Assessment
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Run the Application
```bash
python app.py
```

---

## 🤝 Acknowledgements

Special thanks to **Saket Choudary Kongara** for his cooperation and support in this project. He built the model based on my task and dataset.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and contribute!

---

## 📬 Contact

For any queries or collaborations, reach out to me:
- **GitHub:** [Mahatir-Ahmed-Tusher](https://github.com/Mahatir-Ahmed-Tusher)
- **LinkedIn:** [Mahatir Ahmed Tusher](https://in.linkedin.com/in/mahatir-ahmed-tusher-5a5524257)
- **Google Scholar:** [Mahatir Ahmed Tusher](https://scholar.google.com/citations?user=k8hhhx4AAAAJ&hl=en)

🚀 **Stay informed, stay healthy!** 🏥💙

