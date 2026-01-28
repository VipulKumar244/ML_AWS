
from fastapi import FastAPI,Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle as pkl
import numpy as np
import pandas as pd
import objects
from sklearn.preprocessing import StandardScaler
from objects import feature_attributes

##import ridge regressor and standardization modules from config

ridge_model=pkl.load(open('configs/ridge.pkl','rb'))
standardizer=pkl.load(open('configs/scaler.pkl','rb'))



##Template object

templates=Jinja2Templates(directory="templates")


application=FastAPI()
app=application

@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse(
        "index.html",{"request":request}
    )



@app.get("/predictdata",response_class=HTMLResponse)
async def get_attributes(request:Request):
    return templates.TemplateResponse(
        "home.html",{"request":request}
    )





@app.post("/predictdata",response_class=HTMLResponse)
async def predict_datapoint(request:Request,
                attributes:feature_attributes=Depends(feature_attributes.as_form)):
    
    


    input_scaled=standardizer.transform([[attributes.Temperature,attributes.RH,
                             attributes.Ws,
                             attributes.Rain,
                             attributes.FFMC,
                             attributes.DMC,
                             attributes.ISI,
                             attributes.Classes,
                             attributes.Region]])
    



    result=ridge_model.predict(input_scaled)


    
    return templates.TemplateResponse("home.html",
                                      {"request":request,"result":result})

    


