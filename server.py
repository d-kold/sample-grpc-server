import grpc
from concurrent import futures

# Import the generated classes
from proto import electricity_pb2, electricity_pb2_grpc


class ElectricityService(electricity_pb2_grpc.ElectricityServiceServicer):
    def GetElectricityData(self, request, context):
        with open('data/meterusage.csv', 'r') as f:
            data = f.readlines()
        records = []
        for line in data[1:]:  # skip header
            timestamp, usage = line.strip().split(',')
            record = electricity_pb2.MeterUsageRecord(timestamp=timestamp, usage=float(usage))
            records.append(record)
        return electricity_pb2.ElectricityResponse(records=records)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    electricity_pb2_grpc.add_ElectricityServiceServicer_to_server(ElectricityService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
