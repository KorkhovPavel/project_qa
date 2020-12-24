import pytest
import requests

# https://api.openbrewerydb.org/breweries
# https://dog.ceo/api/breeds/list/all
# https://jsonplaceholder.typicode.com/
@pytest.fixture()
def parser_api_fixture():
    res = requests.get('https://jsonplaceholder.typicode.com/')
    return res

