from pprint import pprint

import pytest

from main import send_request_to_server


# TODO:
# This test code is not perfectlly

@pytest.mark.skip()
def test_send_request_to_server_1():
    matching_dicts = [
        {'matching_val': 0.5, 'template_id': 1},
        {'matching_val': 0.2, 'template_id': 2},
        {'matching_val': 0.5, 'template_id': 18},
        {'matching_val': 0.2, 'template_id': 19},
    ]
    res = send_request_to_server(matching_dicts)
    pprint(res)
    return


@pytest.mark.skip()
def test_send_request_to_server_2():
    matching_dicts = [
        {'matching_val': 0.5, 'template_id': 1},
        {'matching_val': 0.9, 'template_id': 2},
        {'matching_val': 0.5, 'template_id': 18},
        {'matching_val': 0.2, 'template_id': 19},
    ]
    res = send_request_to_server(matching_dicts)
    pprint(res)
    return


@pytest.mark.skip()
def test_send_request_to_server_3():
    matching_dicts = [
        {'matching_val': 0.5, 'template_id': 1},
        {'matching_val': 0.2, 'template_id': 2},
        {'matching_val': 0.5, 'template_id': 18},
        {'matching_val': 0.8, 'template_id': 19},
    ]
    res = send_request_to_server(matching_dicts)
    pprint(res)
    return


@pytest.mark.skip()
def test_send_request_to_server_4():
    matching_dicts = [
        {'matching_val': 0.5, 'template_id': 1},
        {'matching_val': 0.9, 'template_id': 2},
        {'matching_val': 0.5, 'template_id': 18},
        {'matching_val': 0.9, 'template_id': 19},
    ]
    res = send_request_to_server(matching_dicts)
    pprint(res)
    return
