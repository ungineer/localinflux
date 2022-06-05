from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
import flux

app = FastAPI()

influx_db = flux.InfluxAdaptor(config_path='/fluxconfig/influx-configs', influx_url='http://fluxdb:8086') 

class PointModel(BaseModel):
    location: str
    field: str
    value: float

@app.post("/point/")
def add_a_data_point(point: PointModel, bucket: Optional[str] = None):
    influx_db.write(point.location, point.field, point.value, bucket)
    return True

@app.get("/")
def ping():
    return "pong"
