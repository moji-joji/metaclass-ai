from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import numpy as np
import joblib  # If your model is a .pkl file
from tensorflow import keras  # If your model is a .h5 file
import logging
print("Starting server...")
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Define the data model for request validation


class PredictionItem(BaseModel):
    pitch: float
    roll: float
    yaw: float


class PredictionList(BaseModel):
    dataList: list[PredictionItem] = Field(..., example=[
                                           {"pitch": 10.5, "roll": 20.0, "yaw": 30.5}])


# Load your trained model
model_path = "LSTMlast-2024_03_11-01_23_33_PM.h5"
model = keras.models.load_model(model_path)

print("Model loaded successfully")


@app.post("/predict")
async def predict(prediction_list: PredictionList):
    try:
        data_list = prediction_list.dataList
        prediction_input = np.array(
            [[entry.pitch, entry.roll, entry.yaw] for entry in data_list])

        prediction_input[:, 0] = (prediction_input[:, 0] + 180) % 360
        prediction_input[:, -1] = (prediction_input[:, -1] + 180) % 360

        arr = np.array([prediction_input])
        result_value = model.predict(arr)
        response = True if result_value[0][0] > 0.55 else False

        logging.info(
            f'Prediction successful. Response: {response}, Result: {result_value[0][0]}')

        return {"is_attentive": response, "result": str(result_value[0][0])}

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
# uvicorn main:app --reload --port 5000