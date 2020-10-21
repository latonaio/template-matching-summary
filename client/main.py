import sys
import os
import traceback

from src.errors import TemplateMatchingSummaryError
from src import vehicle, trigger
from aion.microservice import main_decorator, Options
from aion.logger import initialize_logger, lprint

SERVICE_NAME = os.environ.get("SERVICE")
CURRENT_DEVICE_NAME = os.environ.get("CURRENT_DEVICE_NAME")

initialize_logger(SERVICE_NAME)


@main_decorator(SERVICE_NAME)
def main(opt: Options):
    conn = opt.get_conn()
    num = opt.get_number()

    try:
        for kanban in conn.get_kanban_itr(SERVICE_NAME, num):
            result = False
            output_metadata = {}

            metadata = kanban.get_metadata()
            matching_data_list = metadata['matching_data_list']
            lprint("recieve matching_data_list from template-matching-by-opencv")

            if CURRENT_DEVICE_NAME in ['tartarus', 'poseidon', 'lib']:
                ret = vehicle.run(matching_data_list)
                output_metadata = ret[0]
                result = ret[1]
            elif CURRENT_DEVICE_NAME in ['deneb', 'elpis', 'neo', 'moca']:
                ret = trigger.run(matching_data_list)
                output_metadata = ret[0]
                result = ret[1]
            else:
                raise TemplateMatchingSummaryError("Device Name " + CURRENT_DEVICE_NAME + " is wrong.")

            lprint("end status: ", output_metadata['TemplateMatchingSummary']['end']['status'])
            conn.output_kanban(
                result=result,
                connection_key="default",
                metadata=output_metadata,
            )


    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
