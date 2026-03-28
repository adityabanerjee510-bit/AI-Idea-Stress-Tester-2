from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field, computed_field
from typing import List, Optional,Annotated,Literal
import json


app = FastAPI()
@app.get("/index.html")
def read_root():
    return FileResponse("Frontend-2/index.html")


@app.get("/Signup.html")
def read_signup():
    return FileResponse("Frontend-2/Signup.html") 

# @app.get("/Login.html")
# def read_login():
#     return FileResponse("Frontend-2/Login2.html")

@app.get("/Dashboard.html")
def read_dashboard():
    return FileResponse("Frontend-2/Dashboard.html")

@app.get("/simulator.html")
def read_simulator():
    return FileResponse("Frontend-2/simulator.html")