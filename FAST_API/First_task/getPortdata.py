import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Port Data API"}


@app.get("/port-data")
def get_port_data():
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        return {
            "status_code": response.status_code,
            "url": url,
            "data": data,
            "message": "Port Data fetched successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


@app.get("/custom-url")
def get_custom_url_data(url: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Request failed: {str(e)}")


@app.get("/custom-url-data")
def get_custom_url_summary(url: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Extract top-level fields from the JSON
        type_ = data.get("type")
        seq = data.get("seq")
        expires = data.get("expires")
        mac = data.get("mac")
        ip = data.get("ip")
        ver = data.get("ver")
        max_ports = data.get("max-ports")
        max_slot = data.get("max-slot")

        # Handle multiple statuses
        status_list = data.get("status", [])
        first_status = status_list[0] if status_list else None

        return {
            "type": type_,
            "seq": seq,
            "expires": expires,
            "mac": mac,
            "ip": ip,
            "ver": ver,
            "max_ports": max_ports,
            "max_slot": max_slot,
            "first_status": first_status
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
@app.get("/get-statuses")
def get_all_statuses(url: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Get all statuses
        status_list = data.get("status", [])

        return {"statuses": status_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

@app.get("/get-sn")
def get_custom_url_summary(url: str, statusIndex: int):
    try:
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
    


    # {
    # "type": "dev-status",
    # "seq": 7,
    # "expires": -1,
    # "mac": "00-31-f1-02-03-33",
    # "ip": "192.168.4.60",
    # "ver": "664-801-900-061-100-000",
    # "max_ports": 64,
    # "max_slot": 1,
    # "first_status": {
    #     "port": "1.01",
    #     "sim": "",
    #     "seq": 7,
    #     "st": 3,
    #     "imei": "353149593839770",
    #     "active": 1,
    #     "inserted": 1,
    #     "slot_active": 1,
    #     "led": 0,
    #     "network": 4,
    #     "iccid": "89148000012104174376",
    #     "imsi": "311480178088371",
    #     "sn": "14173839711",
    #     "opr": "311480 mobileX",
    #     "bal": "0.00",
    #     "sig": 24
    # }