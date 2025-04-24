from data.iris_data import load_iris_data
from utils.preprocessing import preprocess_data
import joblib

if __name__ == "__main__":
    data = load_iris_data()
    X, y = preprocess_data(data)

    model = joblib.load("models/iris_model.pkl")
    sample = X.iloc[0].values.reshape(1, -1)
    prediction = model.predict(sample)

    print(f"Prediction for first sample: {prediction[0]}")
