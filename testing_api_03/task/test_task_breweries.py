import pytest
import requests


class TestBreweries:
    def test_rest(self, parser_api_fixture_dog_breweries):
        """
        check server response
        :param parser_api_fixture_dog_breweries:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture_dog_breweries), 'test_res False'

    def test_count_val(self, parser_api_fixture_dog_breweries):
        """
        quantity val
        :param parser_api_fixture_dog_breweries:
        :return:
        """
        len_val = len(parser_api_fixture_dog_breweries.json())
        assert len_val == 20, "test_count_val False"

    @pytest.mark.parametrize("link,num", [('?by_city=san_diego', 2), ('?by_city=san%20diego', 5)])
    def test_check_san_diego(self, link, num, parser_api_fixture_dog_breweries):
        """
        filter check by city (San Diego)
        :param link:
        :param num:
        :param parser_api_fixture_dog_breweries:
        :return:
        """
        url = parser_api_fixture_dog_breweries.url + link
        urls = requests.get(url).json()
        assert urls[num]['city'] == 'San Diego', 'test_check_san_diego False'

    def test_json(self, parser_api_fixture_dog_breweries):
        """
        check availability not json
        :param parser_api_fixture_dog_breweries:
        :return:
        """
        assert parser_api_fixture_dog_breweries.json(), 'test_json False'

    @pytest.mark.parametrize("num", ['2', '44', '55'])
    def test_search_by_id(self, num, parser_api_fixture_dog_breweries):
        """
        search by id
        :param num:
        :param parser_api_fixture_dog_breweries:
        :return:
        """
        url = parser_api_fixture_dog_breweries.url + '/'+num
        urls = requests.get(url).json()
        assert urls['id'] == int(num), 'test_search_by_id False'
