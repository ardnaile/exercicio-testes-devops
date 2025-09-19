import pytest
from servico import cadastrarusuario

def testcadastrousuario():
    resultado = cadastrarusuario("João")
    assert resultado[1] == "João"

def testcadastroinvalido():
    with pytest.raises(ValueError):
        cadastrarusuario(None)
