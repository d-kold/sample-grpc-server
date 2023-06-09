# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import electricity_pb2 as proto_dot_electricity__pb2


class ElectricityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetElectricityData = channel.unary_unary(
                '/ElectricityService/GetElectricityData',
                request_serializer=proto_dot_electricity__pb2.GetMeterUsageRequest.SerializeToString,
                response_deserializer=proto_dot_electricity__pb2.ElectricityResponse.FromString,
                )


class ElectricityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetElectricityData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ElectricityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetElectricityData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetElectricityData,
                    request_deserializer=proto_dot_electricity__pb2.GetMeterUsageRequest.FromString,
                    response_serializer=proto_dot_electricity__pb2.ElectricityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ElectricityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ElectricityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetElectricityData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElectricityService/GetElectricityData',
            proto_dot_electricity__pb2.GetMeterUsageRequest.SerializeToString,
            proto_dot_electricity__pb2.ElectricityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
