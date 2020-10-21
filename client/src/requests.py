import os
import grpc

from proto import template_matcning_summary_pb2, template_matcning_summary_pb2_grpc
from google.protobuf.struct_pb2 import Struct
from aion.logger import lprint

SERVER_HOST = os.environ.get("SERVER_HOST", "template-matching-summary-server-001-srv")
SERVER_PORT = os.environ.get("SERVER_PORT", 50052)


class Requests():
    def __init__(self):
        self.channel = None
        self.stub = None

    def __enter__(self):
        self.channel = grpc.insecure_channel(SERVER_HOST + ':' + str(SERVER_PORT))
        self.stub = template_matcning_summary_pb2_grpc.TemplateMatchingSummaryStub(self.channel)
        return self

    def __exit__(self, exe_type, exe_value, traceback):
        if self.channel is not None:
            self.channel.close()
        self.channel = None
        self.stub = None

        if exe_type is not None:
            raise RuntimeError(exe_value)
        return

    def get_matching_summary(self, matching_data):
        s = Struct()
        s.update({'templateMatchingByOpenCV': matching_data})
        request = template_matcning_summary_pb2.SummaryRequest(matching_data=s)

        try:
            ret = self.stub.get_matching_summary(request)
        except grpc.RpcError as e:
            lprint(e)
            return False
        else:
            return self._unpack_struct(ret.summary_data)

    def _unpack_struct(self, val):
        if isinstance(val, Struct):
            dic = {}
            dic.update(val)
            for k, x in dic.items():
                dic[k] = self._unpack_struct(x)
            return dic
        elif isinstance(val, list):
            lis = []
            for x in val:
                lis.append(self._unpack_struct(x))
            return lis
        else:
            return val
