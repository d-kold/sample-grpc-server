import grpc
import math

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from proto import electricity_pb2, electricity_pb2_grpc


app = FastAPI()
templates = Jinja2Templates(directory="templates")


def fetch_data_from_grpc():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = electricity_pb2_grpc.ElectricityServiceStub(channel)
        response = stub.GetElectricityData(electricity_pb2.GetMeterUsageRequest())
        return response.records


def get_processed_records(records):
    processed_records = []
    for record in records:
        usage = record.usage
        if usage == float('Infinity'):
            usage = "Infinity"
        elif usage == float('-Infinity'):
            usage = "-Infinity"
        elif math.isnan(usage):
            usage = "NaN"
        processed_records.append({"timestamp": record.timestamp, "usage": usage})
    return processed_records


@app.get("/electricity", response_class=JSONResponse)
def get_electricity_data():
    records = fetch_data_from_grpc()
    return {"records": get_processed_records(records)}


@app.get("/")
def read_template(request: Request):
    records = fetch_data_from_grpc()
    return templates.TemplateResponse("index.html", {"request": request, "records": get_processed_records(records)})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
