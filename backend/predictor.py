import os
import pickle
import pandas as pd

# Load the trained model
MODEL_PATH = os.path.join("models", "model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Predict the best crop based on input parameters.
    """

    sample = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })

    prediction = model.predict(sample)

    return prediction[0]