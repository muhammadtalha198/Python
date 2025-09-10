from dotenv import load_dotenv
import os
import requests
from fastapi import FastAPI, HTTPException

load_dotenv()

url = os.getenv("URL")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Port Data Env Version"}

@app.get("/get-data")
def get_custom_url_data():
    try:
           # Get URL from .env
        url = os.getenv("GOIP_URL")

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Request failed: {str(e)}")


@app.get("/get-statuses")
def get_all_statuses():
    try:
        url = os.getenv("GOIP_URL")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Get all statuses
        status_list = data.get("status", [])

        return {"statuses": status_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


@app.get("/get-sn")
def get_custom_url_summary( statusIndex: int):
    try:
        url = os.getenv("GOIP_URL")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Handle multiple statuses
        status_list = data.get("status", [])
        selected_status = status_list[statusIndex] if 0 <= statusIndex < len(status_list) else None

        # Extract only the SN value
        sn = selected_status.get("sn") if selected_status else None

        return {"sn": sn}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")