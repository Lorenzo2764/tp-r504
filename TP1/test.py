import pytest
import fonctions as f

def test_1():
    assert f.puissance(2,3) == 8
    assert f.puissance(2,2) == 4

def test_2():
    assert f.puissance(-1,2) == 1
    assert f.puissance(-1,3) == -1

def test_zero_puissance_positive():
    assert f.puissance(0,1) == 0
    assert f.puissance(0,5) == 0
    assert f.puissance(0,10) == 0

def test_exposant_negatif_leve_exception():
    with pytest.raises(Exception):
        f.puissance(0,-1)
    with pytest.raises(Exception):
        f.puissance(5,-3)
    with pytest.raises(Exception):
        f.puissance(-1,-1)
