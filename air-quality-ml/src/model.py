from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def train_model(df):
    """
    Trains the model
    Returns the necessary data
    """

    # features
    X = df[["temp", "humidity", "wind_speed"]]

    # Predicted value
    y = df["pm2_5"]

    # training vs test 
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # forming the model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # model training
    model.fit(X_train, y_train)

    return model, X_test, y_test