from src.data_loader import load_data
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_results

df = load_data("data/air_quality.csv")

print("\n--- VERİ SETİ ---")
print(df.head())

model, X_test, y_test = train_model(df)

predictions = evaluate_model(
    model,
    X_test,
    y_test
)

plot_results(y_test, predictions)

new_data = [[29, 50, 11]]

prediction = model.predict(new_data)

print("\n--- New Prediction ---")
print(f"Predicted PM2.5 value: {prediction[0]:.2f}")