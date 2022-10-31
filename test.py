
from project import readfile
import pytest
tests = [('harry_potter.txt', 1, 'Harry Potter and the Sorcerers Stone\n')]
@pytest.mark.parametrize('test_inp, numofstr, result', tests)
def test_calculation(test_inp, numofstr, result):
    assert readfile(test_inp, numofstr) == result