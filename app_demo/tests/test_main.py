import pytest
from src.main import suma, resta, multiplicacion, division


def test_suma_positivos():
    assert suma(2, 3) == 5


def test_suma_con_cero():
    assert suma(5, 0) == 5


def test_suma_con_negativos():
    assert suma(-2, -3) == -5


def test_resta_positivos():
    assert resta(5, 3) == 2


def test_resta_con_cero():
    assert resta(5, 0) == 5


def test_resta_resultado_negativo():
    assert resta(3, 5) == -2


def test_resta_con_negativos():
    assert resta(-5, -3) == -2


def test_multiplicacion_positivos():
    assert multiplicacion(2, 4) == 8


def test_multiplicacion_con_cero():
    assert multiplicacion(8, 0) == 0


def test_multiplicacion_con_negativos():
    assert multiplicacion(-2, 4) == -8


def test_multiplicacion_dos_negativos():
    assert multiplicacion(-2, -4) == 8


def test_division_normal():
    assert division(10, 2) == 5


def test_division_decimal():
    assert division(7, 2) == 3.5


def test_division_numerador_cero():
    assert division(0, 5) == 0


def test_division_con_negativos():
    assert division(-10, 2) == -5


def test_division_dos_negativos():
    assert division(-10, -2) == 5


def test_division_por_cero():
    with pytest.raises(ValueError):
        division(10, 0)
