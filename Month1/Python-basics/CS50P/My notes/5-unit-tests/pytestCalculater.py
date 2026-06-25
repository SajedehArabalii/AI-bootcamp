#IT is possible to do pytest on a folder of tests

from calculater import square
import pytest

def test_pos():
    assert square(2) == 4
    assert square(3) == 9

def test_neg():    
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")