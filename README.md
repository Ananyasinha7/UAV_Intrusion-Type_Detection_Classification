# UAV_Intrusion-Type_Detection_Classification
Here's a professional and clear `README.md` file for your **UAV Intrusion-Type Detection Classification** project. It assumes you're using machine learning (Gradient Boosting, etc.) to classify intrusion types from UAV network traffic features:

---

## 🛰️ UAV Intrusion-Type Detection Classification

A machine learning-based system for detecting and classifying different types of intrusions in UAV (Unmanned Aerial Vehicle) network traffic using statistical features extracted from radio frequency and packet data.
It classifies the type of Cyber UAV Intrusion as:
- Benign
- Replay
- evil-twin
- DOS attack
- FDI

---

### 📊 Project Overview

This project applies supervised learning models to classify network intrusion types based on extracted features such as:

- Packet timestamps, lengths, and protocol details  
- TCP/UDP port and sequence information  
- WLAN and IP header fields  
- Statistical traffic features like flow mean, size std, etc.

The best-performing model (`GradientBoostingClassifier`) achieves **99.6%+ accuracy** on the test set.

---

### 🔍 Features Used

The dataset contains **37 engineered features**, including:

- `frame.len`, `data.len`, `tcp.window_size`
- `wlan.*`, `ip.*`, `tcp.*`, `udp.*`
- Time-based attributes like `timestamp_c` and `time_since_last_packet`

---

### 🧠 ML Models Trained

- ✅ Gradient Boosting Classifier *(Best Performance)*
- Random Forest Classifier  
- Decision Tree Classifier  
- K-Nearest Neighbors  
- ❌ AdaBoost Classifier *(Poor performance)*

All models were evaluated on metrics like **accuracy**, **F1-score**, **ROC AUC**, **precision**, and **recall**.


### 🚀 Usage

#### 1. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Make predictions from user input

```python
# Example from main.py
user_input = {
    'timestamp_c': 1714382765.0,
    'frame.number': 1000.0,
    ...
    'tcp.seq_raw': 123456789.0
}

prediction, proba = predict_from_input(user_input, models['GradientBoost Classifier'], scaler)
print("Predicted class:", le.inverse_transform([prediction])[0])
```

---

### 🧪 Model Performance Summary

| Model                  | Accuracy | F1 Score | ROC AUC | Notes                  |
|------------------------|----------|----------|---------|------------------------|
| ✅ Gradient Boosting    | 99.6%    | 0.9962   | 1.000   | Best generalization    |
| Random Forest          | 99.4%    | 0.9941   | 0.9999  | Strong performance     |
| Decision Tree          | 99.4%    | 0.9944   | 0.9966  | Slight overfitting     |
| K-Nearest Neighbors    | 93.2%    | 0.9320   | 0.9874  | Lower generalization   |
| ❌ AdaBoost             | 50.9%    | 0.3780   | 0.9465  | Ineffective            |

---

### 📌 Requirements

- Python 3.8+
- Scikit-learn
- NumPy / Pandas
- Matplotlib / Seaborn (for evaluation)
- Streamlit



---
### Deployed site: https://uavintrusion-typedetectionclassification-25yjm8psd9pnksqpu7rs3.streamlit.app/
---

### 🙋‍♀️ Author

**Ananya Sinha**  


