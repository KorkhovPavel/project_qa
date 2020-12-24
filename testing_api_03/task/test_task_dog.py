import pytest


class TestDog:
    def test_res(self, parser_api_fixture):
        """
        check server response
        :param parser_api_fixture:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture), 'test_res False'

    def test_json(self, parser_api_fixture):
        """
        check availability not json
        :param parser_api_fixture:
        :return:
        """
        assert parser_api_fixture.json(), 'test_json False'

    @pytest.mark.parametrize("test_input, test_answer", [("message", 0), ("status", 1)])
    def test_check_key(self, parser_api_fixture, test_input, test_answer):
        """
        checking keys
        :param parser_api_fixture:
        :param test_input:
        :param test_answer:
        :return:
        """
        dct = [*parser_api_fixture.json().keys()]
        assert test_input == dct[test_answer], 'test_check_key False'

    def test_check_success(self, parser_api_fixture):
        """
        check status
        :param parser_api_fixture:
        :return:
        """
        dct = parser_api_fixture.json()
        assert 'success' == dct["status"], 'test_check_success False'

    @pytest.mark.parametrize('keys,num', [("message", 94), ("status", 1)])
    def test_count_val(self, parser_api_fixture, keys, num):
        """
        quantity val
        :param parser_api_fixture:
        :param keys:
        :param num:
        :return:
        """
        len_val = len(parser_api_fixture.json()[keys])
        if parser_api_fixture.json()[keys] == 'success':
            len_val = 1
        assert len_val == num

    @pytest.mark.parametrize('name,sub_name', [(0, 'boston'), (1, 'english'), (2, 'french')])
    def test_check_bulldog_val(self, parser_api_fixture, name, sub_name):
        """
        bulldog sub-breed check
        :param parser_api_fixture:
        :param name:
        :param sub_name:
        :return:
        """
        len_val = parser_api_fixture.json()["message"]
        assert len_val['bulldog'][name] == sub_name
