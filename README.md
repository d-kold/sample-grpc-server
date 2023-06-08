# Sample gRPC server

This application showcases the use of gRPC to serve time-based electricity meter usage data, which is then consumed by a FastAPI server and displayed on a frontend page using Jinja templates.

## Proto - `proto/electricity.proto`

The `electricity.proto` file contains the service and message definitions for the gRPC server and client. Here are the main components:

- `MeterUsageRecord`: A message that represents a single record of meter usage. It has two fields - a `timestamp` string and a `usage` double.

- `GetMeterUsageRequest`: An empty message used to initiate a request for meter usage records.

- `ElectricityResponse`: A message that represents the response from the server. It contains a repeated field of `MeterUsageRecord` messages.

- `ElectricityService`: The service definition. It has one RPC method, `GetElectricityData`, which takes a `GetMeterUsageRequest` message and returns an `ElectricityResponse` message.

### Generate gRPC code using the following command
```commandline
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/electricity.proto
```

## gRPC Server - `server.py`

The gRPC server is implemented in the `ElectricityService` class in `server.py`. This class inherits from `electricity_pb2_grpc.ElectricityServiceServicer`, which is generated from the `.proto` file.

- `GetElectricityData`: This method reads the `meterusage.csv` file, creates `MeterUsageRecord` messages for each row, and returns them in an `ElectricityResponse` message.

The `serve` function starts the gRPC server, registers the `ElectricityService` with it, and binds it to a port.

## FastAPI Client - `client.py`

The FastAPI client in `client.py` communicates with the gRPC server and serves the electricity data over HTTP.

- `/electricity`: The endpoint that fetches electricity data from the gRPC server and returns it as a JSON response.

- `/`: The endpoint that renders the data in a Jinja template.

The client uses the `electricity_pb2_grpc.ElectricityServiceStub` class to make RPC calls to the gRPC server. It parses the server's response and converts it into JSON or an HTML page depending on the endpoint.

## HTML Template - `templates/index.html`

The `index.html` file is a Jinja template that displays the meter usage data in a table. The FastAPI server injects the data into the template and returns the resulting HTML page. The table has a row for each `MeterUsageRecord`, with the `timestamp` and `usage` values in separate columns.