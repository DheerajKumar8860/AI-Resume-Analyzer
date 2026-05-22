import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "resume_classifier.pkl"
)

print("MODEL PATH:", MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)

def predict_resume_role(text):
    prediction = model.predict([text])
    return prediction[0]