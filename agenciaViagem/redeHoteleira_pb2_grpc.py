# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import redeHoteleira_pb2 as redeHoteleira__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in redeHoteleira_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RedeHoteleiraStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BookHotel = channel.unary_unary(
                '/redeHoteleira.RedeHoteleira/BookHotel',
                request_serializer=redeHoteleira__pb2.BookHotelRequest.SerializeToString,
                response_deserializer=redeHoteleira__pb2.BookHotelResponse.FromString,
                _registered_method=True)
        self.CancelBookHotel = channel.unary_unary(
                '/redeHoteleira.RedeHoteleira/CancelBookHotel',
                request_serializer=redeHoteleira__pb2.CancelBookHotelRequest.SerializeToString,
                response_deserializer=redeHoteleira__pb2.CancelBookHotelResponse.FromString,
                _registered_method=True)


class RedeHoteleiraServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BookHotel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelBookHotel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedeHoteleiraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BookHotel': grpc.unary_unary_rpc_method_handler(
                    servicer.BookHotel,
                    request_deserializer=redeHoteleira__pb2.BookHotelRequest.FromString,
                    response_serializer=redeHoteleira__pb2.BookHotelResponse.SerializeToString,
            ),
            'CancelBookHotel': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelBookHotel,
                    request_deserializer=redeHoteleira__pb2.CancelBookHotelRequest.FromString,
                    response_serializer=redeHoteleira__pb2.CancelBookHotelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'redeHoteleira.RedeHoteleira', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('redeHoteleira.RedeHoteleira', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RedeHoteleira(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BookHotel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/redeHoteleira.RedeHoteleira/BookHotel',
            redeHoteleira__pb2.BookHotelRequest.SerializeToString,
            redeHoteleira__pb2.BookHotelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CancelBookHotel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/redeHoteleira.RedeHoteleira/CancelBookHotel',
            redeHoteleira__pb2.CancelBookHotelRequest.SerializeToString,
            redeHoteleira__pb2.CancelBookHotelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
