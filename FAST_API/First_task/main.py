from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


teas : List[Tea] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API"}

@app.get("/teas")
def get_teas():
    return {"teas": [tea.dict() for tea in teas]}

@app.post("/teas")
def add_tea(tea: Tea):
    for t in teas:
        if t.id == tea.id:
            return {"message": "Tea with this ID already exists"}
    teas.append(tea)
    return {"message": "Tea created successfully"}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, tea: Tea):
    for idx, t in enumerate(teas):
        if t.id == tea_id:
            teas[idx] = tea
            return {"message": "Tea updated successfully"}
    return {"message": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for idx, t in enumerate(teas):
        if t.id == tea_id:
            deleted = teas.pop(idx)
            return {"message": "Tea deleted successfully", "deleted": deleted.dict()}
    return {"message": "Tea not found"}