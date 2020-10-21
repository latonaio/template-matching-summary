# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import template_matcning_summary_pb2 as proto_dot_template__matcning__summary__pb2


class TemplateMatchingSummaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_matching_summary = channel.unary_unary(
                '/templatematchingSummary.TemplateMatchingSummary/get_matching_summary',
                request_serializer=proto_dot_template__matcning__summary__pb2.SummaryRequest.SerializeToString,
                response_deserializer=proto_dot_template__matcning__summary__pb2.SummaryResponse.FromString,
                )


class TemplateMatchingSummaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_matching_summary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TemplateMatchingSummaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_matching_summary': grpc.unary_unary_rpc_method_handler(
                    servicer.get_matching_summary,
                    request_deserializer=proto_dot_template__matcning__summary__pb2.SummaryRequest.FromString,
                    response_serializer=proto_dot_template__matcning__summary__pb2.SummaryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'templatematchingSummary.TemplateMatchingSummary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TemplateMatchingSummary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_matching_summary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/templatematchingSummary.TemplateMatchingSummary/get_matching_summary',
            proto_dot_template__matcning__summary__pb2.SummaryRequest.SerializeToString,
            proto_dot_template__matcning__summary__pb2.SummaryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)