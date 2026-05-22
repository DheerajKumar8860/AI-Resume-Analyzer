import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

import joblib


# Load Dataset

data = pd.read_csv(
    "model/UpdatedResumeDataSet.csv"
)


# Features and Labels

X = data["Resume"]

y = data["Category"]


# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42

)


# ML Pipeline

model = Pipeline([

    (

        "tfidf",

        TfidfVectorizer(
            stop_words="english"
        )

    ),

    (

        "classifier",

        LogisticRegression()

    )

])


# Train Model

model.fit(
    X_train,
    y_train
)


# Accuracy

accuracy = model.score(
    X_test,
    y_test
)

print(
    f"Model Accuracy: {accuracy}"
)


# Save Model

joblib.dump(

    model,

    "model/resume_classifier.pkl"

)

print(
    "Model trained and saved successfully!"
)