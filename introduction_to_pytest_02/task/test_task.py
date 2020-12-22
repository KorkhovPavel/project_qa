import random


def test_string_entry():
    """
    does the word appear on the line
    :return:
    """
    assert 'book' in 'read a book', 'test_string_entry = False '


def test_number_is_greater_than_zero():
    """
    number is greater than zero
    :return:
    """
    num = random.randint(1, 10)
    assert num < 0, 'test_number_is_greater_than_zero = False'


def test_not_an_empty_list():
    """
    check the sheet for emptiness8
    :return:
    """
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert lst, 'test_not_an_empty_list = False'


def test_get_value_from_dictionary():
    """
    the taken value from the dictionary is 22
    :return:
    """
    dct = {1: '22', 2: '11', 3: '00'}
    assert dct.get(1) == '22', 'test_get_value_from_dictionary = False'


def test_list_in_set():
    """
    convert list to set
    :return:
    """
    lst = [3, 2, 3, 1]
    assert type(set(lst) == type(set())), 'test_list_in_set = False'
