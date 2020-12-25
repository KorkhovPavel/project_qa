import pytest
import requests


class TestDog:
    def test_res(self, parser_api_fixture_jsonplaceholder):
        """
        check server response
        :param parser_api_fixture_jsonplaceholder:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture_jsonplaceholder), 'test_res False'

    def test_count_val(self, parser_api_fixture_jsonplaceholder):
        """
        link check number of 100 posts
        :param parser_api_fixture_jsonplaceholder:
        :return:
        """
        url = parser_api_fixture_jsonplaceholder.url + 'posts'
        jsonn = requests.get(url).json()
        assert len(jsonn) == 100, 'test_count_val False'

    @pytest.mark.parametrize('num,name', [(0, 'quidem molestiae enim'), (-1, 'enim repellat iste')])
    def test_checking_name_album(self, parser_api_fixture_jsonplaceholder, num, name):
        """
        checking the name of the first and last album
        :param parser_api_fixture_jsonplaceholder:
        :param num:
        :param name:
        :return:
        """

        url = parser_api_fixture_jsonplaceholder.url + 'albums'
        jsonn = requests.get(url).json()
        assert jsonn[num]['title'] == name, 'test_checking_name_album False'

    @pytest.mark.parametrize('num', [0, 1, 2, 4997, 4998, 4999])
    def test_checking_url_photo(self, parser_api_fixture_jsonplaceholder, num):
        """
        check url photo
        :param parser_api_fixture_jsonplaceholder:
        :param num:
        :return:
        """
        url = parser_api_fixture_jsonplaceholder.url + 'photos'
        jsonn = requests.get(url).json()
        assert 'https://via.placeholder.com/600/' in jsonn[num]['url'], 'test_checking_name_album False'

    @pytest.mark.parametrize('num, appraisal',
                             [(0, 'False'), (1, 'False'), (2, 'False'), (197, 'True'), (198, 'True'), (199, 'False')])
    def test_checking_task(self, parser_api_fixture_jsonplaceholder, num, appraisal):
        """
        check task
        :param parser_api_fixture_jsonplaceholder:
        :param num:
        :return:
        """
        url = parser_api_fixture_jsonplaceholder.url + 'todos'
        jsonn = requests.get(url).json()
        assert str(jsonn[num]['completed']) == appraisal, 'test_checking_task False'
