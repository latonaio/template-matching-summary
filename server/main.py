import sys
import os
import grpc

from concurrent import futures
from aion.logger import initialize_logger, lprint
from src.errors import TemplateMatchingSummaryServerError
from src.vehicle import VehicleSummary
from src.trigger import TriggerSummary
from proto import template_matcning_summary_pb2, template_matcning_summary_pb2_grpc
from google.protobuf.json_format import MessageToDict
from google.protobuf.struct_pb2 import Struct

SERVICE_NAME = os.environ.get("SERVICE")
CURRENT_DEVICE_NAME = os.environ.get("CURRENT_DEVICE_NAME")
SERVER_PORT = 50052

initialize_logger(SERVICE_NAME)


class VehicleSummaryServer(template_matcning_summary_pb2_grpc.TemplateMatchingSummaryServicer):
    def __init__(self):
        super().__init__()
        self.summary = VehicleSummary()

    def get_matching_summary(self, request, context):
        lprint("connect from template-matching-summary client")

        data = MessageToDict(request.matching_data)
        matching_data = data['templateMatchingByOpenCV']

        self.summary.set(matching_data)
        vehicle = self.summary.get_vehicle()
        end = self.summary.get_end()
        ret = self.summary.get_metadata()
        self.summary.stack()
        summary = self.summary.get_all_vehicles()
        ret['vehicle'] = vehicle
        ret['end'] = end
        ret['summary'] = summary

        if end['status']:
            self.summary.reset()

        s = Struct()
        s.update(ret)
        return template_matcning_summary_pb2.SummaryResponse(summary_data=s)


class TriggerSummaryServer(template_matcning_summary_pb2_grpc.TemplateMatchingSummaryServicer):
    def __init__(self):
        super().__init__()
        self.summary = TriggerSummary()

    def get_matching_summary(self, request, context):
        lprint("connect from template-matching-summary client")

        data = MessageToDict(request.matching_data)
        matching_data = data['templateMatchingByOpenCV']

        should_be_reset = self.summary.should_be_reset(matching_data)
        if should_be_reset:
            self.summary.reset()

        self.summary.set(matching_data)
        trigger = self.summary.get_trigger()
        end = self.summary.get_end()
        ret = self.summary.get_metadata()
        ret['trigger'] = trigger
        ret['end'] = end

        if end['status']:
            self.summary.reset()

        s = Struct()
        s.update(ret)
        return template_matcning_summary_pb2.SummaryResponse(summary_data=s)


def main():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

        if CURRENT_DEVICE_NAME in ['tartarus', 'poseidon', 'lib']:
            template_matcning_summary_pb2_grpc.add_TemplateMatchingSummaryServicer_to_server(
                VehicleSummaryServer(), server,
            )
        elif CURRENT_DEVICE_NAME in ['deneb', 'elpis', 'neo', 'moca']:
            template_matcning_summary_pb2_grpc.add_TemplateMatchingSummaryServicer_to_server(
                TriggerSummaryServer(), server,
            )
        else:
            raise TemplateMatchingSummaryServerError("Device Name " + CURRENT_DEVICE_NAME + " is wrong.")

        server.add_insecure_port('[::]:' + str(SERVER_PORT))
        server.start()
        server.wait_for_termination()
    except Exception as e:
        lprint(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
