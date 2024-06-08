from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction_pipeline import prediction_pipeline

text = "What is summarization ?"

app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url = "/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Success")
    except Exception as e:
        return Response(f"Error Occurred: {e}")
    
@app.post("/predict")
async def predict_route(text):
    try:

        obj = prediction_pipeline()
        output = obj.predict(text)
        print("Hey the summary is : \n",output)
        return output
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=8080)



