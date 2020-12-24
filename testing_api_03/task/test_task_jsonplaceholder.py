import pytest
import requests


class TestDog:
    def test_res(self, parser_api_fixture):
        """
        check server response
        :param parser_api_fixture:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture), 'test_res False'

    def test_count_val(self, parser_api_fixture):
        """
        link check number of 100 posts
        :param parser_api_fixture:
        :return:
        """
        url = parser_api_fixture.url + 'posts'
        jsonn = requests.get(url).json()
        assert len(jsonn) == 100, 'test_count_val False'

    @pytest.mark.parametrize('num,name', [(0, 'quidem molestiae enim'), (-1, 'enim repellat iste')])
    def test_checking_name_album(self, parser_api_fixture, num, name):
        """
        checking the name of the first and last album
        :param parser_api_fixture:
        :param num:
        :param name:
        :return:
        """

        url = parser_api_fixture.url + 'albums'
        jsonn = requests.get(url).json()
        assert jsonn[num]['title'] == name, 'test_checking_name_album False'

    @pytest.mark.parametrize('num', [0, 1, 2, 4997, 4998, 4999])
    def test_checking_url_photo(self, parser_api_fixture, num):
        """
        check url photo
        :param parser_api_fixture:
        :param num:
        :return:
        """
        url = parser_api_fixture.url + 'photos'
        jsonn = requests.get(url).json()
        assert 'https://via.placeholder.com/600/' in jsonn[num]['url'], 'test_checking_name_album False'

    @pytest.mark.parametrize('num, appraisal',
                             [(0, 'False'), (1, 'False'), (2, 'False'), (197, 'True'), (198, 'True'), (199, 'False')])
    def test_checking_task(self, parser_api_fixture, num, appraisal):
        """
        check task
        :param parser_api_fixture:
        :param num:
        :return:
        """
        url = parser_api_fixture.url + 'todos'
        jsonn = requests.get(url).json()
        assert str(jsonn[num]['completed']) == appraisal, 'test_checking_task False'
