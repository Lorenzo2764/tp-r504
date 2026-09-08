import pytest
import fonctions as f

def test_1():
    assert f.puissance(2,3) == 8
    assert f.puissance(2,2) == 4

def test_2():
    assert f.puissance(-1,2) == 1
    assert f.puissance(-1,3) == -1

def test_3():
    # 0^x = 0 pour tout x > 0
    assert f.puissance(0,1) == 0
    assert f.puissance(0,5) == 0
    assert f.puissance(0,10) == 0

def test_4():
    with pytest.raises(Exception):
        f.puissance(0,-1)
    with pytest.raises(Exception):
        f.puissance(5,-3)
    with pytest.raises(Exception):
        f.puissance(-1,-1)

def test_5():
    assert f.puissance(2,0) == 1
    assert f.puissance(-3,0) == 1

def test_6():
    with pytest.raises(TypeError):
        f.puissance(2.5, 2)
    with pytest.raises(TypeError):
        f.puissance(2, 2.5)
    with pytest.raises(TypeError):
        f.puissance("2", 3)
