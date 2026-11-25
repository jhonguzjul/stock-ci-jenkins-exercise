import pytest

from inventario import Inventario


@pytest.fixture
def inv():
    inventario = Inventario()
    inventario.agregar("tornillo", 10, precio=0.5)
    return inventario


def test_agregar_producto_nuevo():
    inventario = Inventario()
    inventario.agregar("tuerca", 5)
    assert inventario.cantidad("tuerca") == 5


def test_agregar_suma_a_existente(inv):
    inv.agregar("tornillo", 5)
    assert inv.cantidad("tornillo") == 15


def test_agregar_cantidad_invalida(inv):
    with pytest.raises(ValueError):
        inv.agregar("tornillo", 0)


def test_retirar_descuenta(inv):
    inv.retirar("tornillo", 3)
    assert inv.cantidad("tornillo") == 7


def test_retirar_mas_de_lo_disponible(inv):
    with pytest.raises(ValueError):
        inv.retirar("tornillo", 11)


def test_retirar_producto_inexistente(inv):
    with pytest.raises(KeyError):
        inv.retirar("arandela", 1)


def test_valor_total(inv):
    inv.agregar("martillo", 2, precio=10.0)
    assert inv.valor_total() == pytest.approx(25.0)
