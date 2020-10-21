from src.requests import Requests


def run(matching_data):
    # Request to template matching summary server
    with Requests() as r:
        ret = r.get_matching_summary(matching_data)

    if ret['trigger']['status'] or ret['end']['status']:
        metadata = {
            'TemplateMatchingSummary': ret,
        }
        return metadata, True

    metadata = {
        'TemplateMatchingSummary': ret,
    }
    return metadata, False
