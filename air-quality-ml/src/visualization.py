import matplotlib.pyplot as plt


def plot_results(y_test, predictions):
    """
    comparing real data with predictions
    """

    plt.figure(figsize=(8, 5))

    # real data
    plt.plot(
        y_test.values,
        label="True Values",
        marker="o"
    )

    # predictions
    plt.plot(
        predictions,
        label="Predictions",
        marker="x"
    )

    plt.title("Truth vs Prediction")
    plt.xlabel("Data")
    plt.ylabel("PM2.5")

    plt.legend()

    plt.show()