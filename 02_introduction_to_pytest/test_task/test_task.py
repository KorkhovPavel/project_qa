import random


def test_string_entry(function_fixture, module_fixture, session_fixture):
    """
    does the word appear on the line
    :return:
    """
    print('test_string_entry')
    assert 'book' in 'read a book', 'test_string_entry = False '


def test_number_is_greater_than_zero(function_fixture, module_fixture, session_fixture):
    """
    number is greater than zero
    :return:
    """
    num = random.randint(1, 10)
    print('test_number_is_greater_than_zero')
    assert num > 0, 'test_number_is_greater_than_zero = False'


def test_not_an_empty_list(function_fixture, module_fixture, session_fixture):
    """
    check the sheet for emptiness8
    :return:
    """
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('test_not_an_empty_list')
    assert lst, 'test_not_an_empty_list = False'


def test_get_value_from_dictionary(function_fixture, module_fixture, session_fixture):
    """
    the taken value from the dictionary is 22
    :return:
    """
    dct = {1: '22', 2: '11', 3: '00'}
    print('test_get_value_from_dictionary')
    assert dct.get(1) == '22', 'test_get_value_from_dictionary = False'


def test_list_in_set(function_fixture, module_fixture, session_fixture):
    """
    convert list to set
    :return:
    """
    lst = [3, 2, 3, 1]
    print('test_list_in_set')
    assert type(set(lst) == type(set())), 'test_list_in_set = False'


def test_concatenation(function_fixture, module_fixture, session_fixture):
    """
    concatenation
    :return:
    """
    str1 = 'qwerty'
    str2 = 'asdfgh'
    print('test_concatenation')
    assert str1 + str2 == 'qwertyasdfgh', 'test_concatenation = False'


def test_plus(function_fixture, module_fixture, session_fixture):
    """
    addition of numbers
    :return:
    """
    print('test_plus')
    assert 2 + 6 == 8, 'test_plus = False'


def test_minus(function_fixture, module_fixture, session_fixture):
    """
   subtract a number
   :return:
   """
    print('test_minus')
    assert 10 - 2 == 8, 'test_minus = False'


class TestClass:
    def test_str_num(self, function_fixture, module_fixture, session_fixture):
        """
       check is a string number
       :return:
       """
        strk = '1234'
        print('test_str_num')
        assert strk.isdigit(), 'test_str_num = False'

    def test_exponentiation(self, function_fixture, module_fixture, session_fixture):
        """
        exponentiation
        :return:
        """
        print('test_exponentiation')
        assert 2 ** 3 == 8, 'test_exponentiation = False'
