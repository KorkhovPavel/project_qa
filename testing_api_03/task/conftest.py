import pytest
import requests


@pytest.fixture()
def parser_api_fixture_jsonplaceholder():
    res = requests.get('https://jsonplaceholder.typicode.com/')
    return res


@pytest.fixture()
def parser_api_fixture_dog():
    res = requests.get('https://dog.ceo/api/breeds/list/all')
    return res


@pytest.fixture()
def parser_api_fixture_dog_breweries():
    res = requests.get('https://api.openbrewerydb.org/breweries')
    return res
