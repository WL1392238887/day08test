import pytest


def test_eq():
    assert 2 != 1

def test_sum():
    assert (1+1) >= 2



if __name__ == '__main__':
    pytest.main(['./test_01.py'])