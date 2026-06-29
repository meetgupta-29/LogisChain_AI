import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Load Dataset

df = pd.read_csv("data/shipments.csv")
print(df["Supplier"].unique())
print(df["Origin"].unique())
print(df["Destination"].unique())
print(df["Carrier"].unique())
print(df["Weather"].unique())
print(df["Risk_Level"].unique())

# Encode Categorical Columns

label_encoders = {}

categorical_columns = [
    "Supplier",
    "Origin",
    "Destination",
    "Carrier",
    "Weather",
    "Risk_Level"
]

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder


# Features & Target

X = df[
    [
        "Supplier",
        "Origin",
        "Destination",
        "Carrier",
        "Distance_km",
        "Weather",
        "Risk_Level"
    ]
]

y = df["Delay_Days"]

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Prediction


predictions = model.predict(X_test)

# Accuracy


mae = mean_absolute_error(y_test, predictions)

print("\nModel Trained Successfully!")

print("\nMean Absolute Error:", round(mae,2))


# Save Model

joblib.dump(
    {
        "model": model,
        "encoders": label_encoders
    },
    "models/shipment_model.pkl"
)

print("\nModel Saved Successfully!")