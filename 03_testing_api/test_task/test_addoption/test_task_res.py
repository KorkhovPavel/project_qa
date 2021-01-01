import requests


def test_answer(url_param):
    assert '<Response [200]>' == str(requests.get(url_param)), 'test_res False'
