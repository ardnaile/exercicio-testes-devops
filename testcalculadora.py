import pytest
from calculadora import soma

def testsomapositivos():
    assert soma(2, 3) == 5

def testsomanegativos():
    assert soma(-1, -1) == -2

def testsomazero():
    assert soma(0, 5) == 5

def testsomainvalida():
    with pytest.raises(ValueError):
        soma("a", 2)
