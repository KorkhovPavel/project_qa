import pytest


class TestDog:
    def test_res(self, parser_api_fixture_dog):
        """
        check server response
        :param parser_api_fixture_dog:
        :return:
        """
        assert '<Response [200]>' == str(parser_api_fixture_dog), 'test_res False'

    def test_json(self, parser_api_fixture_dog):
        """
        check availability not json
        :param parser_api_fixture_dog:
        :return:
        """
        assert parser_api_fixture_dog.json(), 'test_json False'

    @pytest.mark.parametrize("test_input, test_answer", [("message", 0), ("status", 1)])
    def test_check_key(self, parser_api_fixture_dog, test_input, test_answer):
        """
        checking keys
        :param parser_api_fixture_dog:
        :param test_input:
        :param test_answer:
        :return:
        """
        dct = [*parser_api_fixture_dog.json().keys()]
        assert test_input == dct[test_answer], 'test_check_key False'

    def test_check_success(self, parser_api_fixture_dog):
        """
        check status
        :param parser_api_fixture_dog:
        :return:
        """
        dct = parser_api_fixture_dog.json()
        assert 'success' == dct["status"], 'test_check_success False'

    @pytest.mark.parametrize('keys,num', [("message", 94), ("status", 1)])
    def test_count_val(self, parser_api_fixture_dog, keys, num):
        """
        quantity val
        :param parser_api_fixture_dog:
        :param keys:
        :param num:
        :return:
        """
        len_val = len(parser_api_fixture_dog.json()[keys])
        if parser_api_fixture_dog.json()[keys] == 'success':
            len_val = 1
        assert len_val == num

    @pytest.mark.parametrize('name,sub_name', [(0, 'boston'), (1, 'english'), (2, 'french')])
    def test_check_bulldog_val(self, parser_api_fixture_dog, name, sub_name):
        """
        bulldog sub-breed check
        :param parser_api_fixture_dog:
        :param name:
        :param sub_name:
        :return:
        """
        len_val = parser_api_fixture_dog.json()["message"]
        assert len_val['bulldog'][name] == sub_name
