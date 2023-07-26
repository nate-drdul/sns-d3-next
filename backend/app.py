from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np
import seaborn as sns

import json

from datetime import datetime, timedelta

#########################################################################################################

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#########################################################################################################
#########################################################################################################
#### Helper functions that could be useful for missing data
###########################################################################33

def filter_rows_by_values(df, col, values):
    return df[~df[col].isin(values)]

def missing(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)

    return mis_val_table_ren_columns


#########################################################################################################

@app.get("/")
async def root():
    return {"message": "Seaborn API!"}

#########################################################################################################

#### Test data end point, returns random data as json from pandas and numpy ############################
#### http://127.0.0.1:8000/testdata ####################################################################

@app.get("/testdata")
async def get_test_data():
    data = pd.DataFrame(np.random.uniform(-1, 1, size=(10, 1)), columns=["data"])
    return JSONResponse(content=data.to_dict(orient="records"))


#########################################################################################################
# Returns a list as json of the example datasets in seaborn
#### http://127.0.0.1:8000/listData

@app.get("/listData")
async def listData():
    return {"data": sns.get_dataset_names()}

#########################################################################################################
#### http://127.0.0.1:8000/randomTimeData

@app.get("/randomTimeData")
async def randomTimeData():

    # Variables for the range of random values
    x = 0
    y = 100

    now = datetime.now()
    dates = pd.date_range(start=now, periods=31)
    df = pd.DataFrame(index=dates, data={'value': np.random.randint(x, y, size=len(dates))})

    #remove the time stamp so just dates
    df.index = df.index.date

    #reset the index to get the dates in their own column
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'date'}, inplace = True)

    return {"data": df.to_dict(orient="records")}

#########################################################################################################
#### http://127.0.0.1:8000/randomWalk

@app.get("/randomWalk")
async def randomwalk():

   # Variables for the range of random values
    x = -100
    y = 100

    now = datetime.now()
    dates = pd.date_range(start=now, periods=31)
    df = pd.DataFrame(index=dates, data={'value': np.random.randint(x, y, size=len(dates))})

    # Create a cumulative sum of 'value' column
    df['value'] = df['value'].cumsum()

    #remove the time stamp so just dates
    df.index = df.index.date

    #reset the index to get the dates in their own column
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'date'}, inplace = True)

    return {"data": df.to_dict(orient="records")}



























