import pytest
import requests


class TestBreweries:
    def test_rest(self, parser_api_fixture):
        """
        check server response
        :param parser_api_fixture:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture), 'test_res False'

    def test_count_val(self, parser_api_fixture):
        """
        quantity val
        :param parser_api_fixture:
        :return:
        """
        len_val = len(parser_api_fixture.json())
        assert len_val == 20, "test_count_val False"

    @pytest.mark.parametrize("link,num", [('?by_city=san_diego', 2), ('?by_city=san%20diego', 5)])
    def test_check_san_diego(self, link, num, parser_api_fixture):
        """
        filter check by city (San Diego)
        :param link:
        :param num:
        :param parser_api_fixture:
        :return:
        """
        url = parser_api_fixture.url + link
        urls = requests.get(url).json()
        assert urls[num]['city'] == 'San Diego', 'test_check_san_diego False'

    def test_json(self, parser_api_fixture):
        """
        check availability not json
        :param parser_api_fixture:
        :return:
        """
        assert parser_api_fixture.json(), 'test_json False'

    @pytest.mark.parametrize("num", ['2', '44', '55'])
    def test_search_by_id(self, num, parser_api_fixture):
        """
        search by id
        :param num:
        :param parser_api_fixture:
        :return:
        """
        url = parser_api_fixture.url + '/'+num
        urls = requests.get(url).json()
        assert urls['id'] == int(num), 'test_search_by_id False'
