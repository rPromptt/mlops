import pickle
import numpy as np
import os

def test_model_prediction():
    model_path = os.path.join(os.path.dirname(__file__), "model/model.pkl")
    with open(model_path, "rb") as f:
        clf = pickle.load(f)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = clf.predict(sample)
    assert prediction[0] in [0, 1, 2]  # For Iris dataset classes
