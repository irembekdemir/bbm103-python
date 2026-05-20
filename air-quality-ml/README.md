# 🏭 Air Quality Prediction System (AI Project)

##  Project Overview

This project is a machine learning-based system that predicts **PM2.5 air pollution levels** using environmental factors such as temperature, humidity, and wind speed.

The goal is to demonstrate how artificial intelligence can be used in environmental monitoring and contribute to smarter, data-driven environmental decision systems.

---

## Problem Statement

Air pollution is a critical environmental issue affecting public health and climate conditions.

This project aims to:
- Predict PM2.5 air quality levels based on weather conditions
- Help understand how environmental factors influence air pollution
- Provide a simple AI-based predictive model for educational and practical purposes

---

## Machine Learning Approach

The project uses supervised machine learning to perform regression on air quality data.

---

### Model Used:
- Random Forest Regressor

---

### Why this model?
- Handles non-linear relationships well
- Works effectively on small datasets
- Robust against overfitting

---

## ✨ Features Used

The model uses the following input features:

-  Temperature (°C)
-  Humidity (%)
-  Wind Speed (m/s)

---

### Target Variable:
- PM2.5 air pollution level

---

##  Project Structure
```
air-quality-ml/
│
├── data/
│ └── air_quality.csv
│
├── src/
│ ├── data_loader.py
│ ├── model.py
│ ├── evaluation.py
│ └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⬇️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/air-quality-ml.git
cd air-quality-ml
```
---

### 2. Install dependencies
``` bash
pip install -r requirements.txt
```
---

## 🚀 How to Run

Run the main script:

```python main.py```

---

## Output

The system provides:

- Model training on historical data
- Evaluation metrics:
  - Mean Absolute Error (MAE)
  - R² Score
- Visualization comparing:
  - Actual vs Predicted PM2.5 values
- Prediction for new environmental conditions

  ---
  
## Example Prediction
```
Input:
Temperature = 29°C
Humidity = 50%
Wind Speed = 11 m/s

Output:
Predicted PM2.5 = 67.42
```
---

## 📊 Model Evaluation Metrics

The model is evaluated using:

- Mean Absolute Error (MAE) → Measures average prediction error
- R² Score → Measures how well the model explains variance in data

--- 

## Real-World Applications

This project demonstrates concepts that can be applied in:

- Smart city systems
- Environmental monitoring
- Climate change analysis
- Public health prediction systems
- IoT-based air quality sensors

---

## Technologies Used
- Python 
  - Pandas
  - Scikit-learn
  - Matplotlib

---

## 🎯 Future Improvements
- Integration with real-time air quality APIs
- Web interface using Flask or FastAPI
- Deep learning models for higher accuracy
- Deployment to cloud (AWS / Heroku)
- Mobile-friendly dashboard
  
## Author

Built as an educational AI project combining machine learning concepts with experimental vibe coding workflows.

## License

This project is open-source and available under the MIT License.
