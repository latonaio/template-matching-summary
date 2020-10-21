from src.requests import Requests
from aion.logger import lprint


def run(matching_data):
    # Request to template matching summary server
    with Requests() as r:
        ret = r.get_matching_summary(matching_data)

    if ret['vehicle']['first'] or ret['end']['status']:
        new_metadata = {}
        if ret['vehicle']['first']:
            new_metadata = {
                'args': {
                    'vehicle': False,
                    'vehicle_name': ret['vehicle']['name'],
                    'end': False,
                }
            }
        else:
            new_metadata = {
                'args': {
                    'vehicle': True,
                    'vehicle_name': ret['summary']['name'],
                    'end': True,
                }
            }

        metadata = {
            'TemplateMatchingSummary': ret,
            'TemplateMatchingSetTemplates': new_metadata,
        }
        return metadata, True

    metadata = {
        'TemplateMatchingSummary': ret,
    }
    return metadata, False
