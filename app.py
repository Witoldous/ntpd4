from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel , ValidationError
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = FastAPI()

# Wczytanie datasetu Iris
data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

class PredictionInput(BaseModel):
    features: list[float]

    def validate_features(self):
        if len(self.features) != len(X[0]):
            raise ValueError(f"Expected {len(X[0])} features, but got {len(self.features)}")

@app.get("/")
def read_root():
    return {"message": "Witaj w moim API!"}

@app.get("/info")
def get_model_info():
    return {
        "model": "Logistic Regression",
        "features_count": len(X[0]),
        "classes": list(data.target_names)
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        input_data.validate_features()
        prediction = model.predict([input_data.features])
        predicted_class = data.target_names[prediction[0]]
        return {"prediction": predicted_class}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Wewnętrzny błąd serwera")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)