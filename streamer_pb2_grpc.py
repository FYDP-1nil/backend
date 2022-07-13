# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import streamer_pb2 as streamer__pb2


class StreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ObtainTwitchKey = channel.unary_unary(
                '/streamer.Streamer/ObtainTwitchKey',
                request_serializer=streamer__pb2.ObtainTwitchKeyRequest.SerializeToString,
                response_deserializer=streamer__pb2.ObtainTwitchKeyResponse.FromString,
                )
        self.ObtainYoutubeKey = channel.unary_unary(
                '/streamer.Streamer/ObtainYoutubeKey',
                request_serializer=streamer__pb2.ObtainYoutubeKeyRequest.SerializeToString,
                response_deserializer=streamer__pb2.ObtainYoutubeKeyResponse.FromString,
                )


class StreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ObtainTwitchKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtainYoutubeKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ObtainTwitchKey': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtainTwitchKey,
                    request_deserializer=streamer__pb2.ObtainTwitchKeyRequest.FromString,
                    response_serializer=streamer__pb2.ObtainTwitchKeyResponse.SerializeToString,
            ),
            'ObtainYoutubeKey': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtainYoutubeKey,
                    request_deserializer=streamer__pb2.ObtainYoutubeKeyRequest.FromString,
                    response_serializer=streamer__pb2.ObtainYoutubeKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'streamer.Streamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Streamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ObtainTwitchKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamer.Streamer/ObtainTwitchKey',
            streamer__pb2.ObtainTwitchKeyRequest.SerializeToString,
            streamer__pb2.ObtainTwitchKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObtainYoutubeKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamer.Streamer/ObtainYoutubeKey',
            streamer__pb2.ObtainYoutubeKeyRequest.SerializeToString,
            streamer__pb2.ObtainYoutubeKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
