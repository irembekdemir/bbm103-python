from sklearn.metrics import mean_absolute_error, r2_score


def evaluate_model(model, X_test, y_test):
    """
    Model performance metric
    """

    # prediction
    predictions = model.predict(X_test)

    # error calculation
    mae = mean_absolute_error(y_test, predictions)

    # success score
    r2 = r2_score(y_test, predictions)

    print("\n--- MODEL RESULTS ---")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R2 Score: {r2:.2f}")

    return predictions