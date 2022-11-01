"""File where we test our function."""
import pytest

from project import readfile

tests = [('harry_potter.txt', 1, 'Harry Potter and the Sorcerers Stone\n')]


@pytest.mark.parametrize('test_inp, numofstr, result_of_func', tests)
def test_calculation(test_inp: str, numofstr: int, result_of_func: str):
    """Test for our function.

    Args:
        test_inp(str): name of the file that we want to open
        numofstr(int): number of string we want to see in file
        result_of_func(str): the output

    Return:
        Test passed

    """
    assert readfile(test_inp, numofstr) == result_of_func