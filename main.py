from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
import uvicorn
import pandas as pd
import joblib
from pydantic import BaseModel

model = joblib.load("model1.pkl")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(requests: Request):
    return templates.TemplateResponse("index.html", {"request": requests})

@app.post("/predict", response_class=HTMLResponse)
def predictData(requests : Request, radius : float = Form(), texture : float = Form()):
    print(radius, texture)
    dataframe = pd.DataFrame({"radius_mean": [radius], "texture_mean": [texture]})
    prediction = model.predict(dataframe)
    prediction = list(prediction)
    print(radius, texture, prediction)
    return templates.TemplateResponse("predict.html", {"request": requests, "radius": radius, "texture": texture, "prediction": "Malignant" if prediction[0] == 0 else "Benign"})

uvicorn.run(app)