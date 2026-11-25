"""Lógica de negocio del inventario."""


class Inventario:
    """Inventario en memoria: nombre -> {cantidad, precio}."""

    def __init__(self):
        self._productos = {}

    def agregar(self, nombre, cantidad, precio=0.0):
        """Agrega unidades de un producto (lo crea si no existe)."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if nombre in self._productos:
            self._productos[nombre]["cantidad"] += cantidad
        else:
            self._productos[nombre] = {"cantidad": cantidad, "precio": precio}

    def retirar(self, nombre, cantidad):
        """Retira unidades de un producto existente."""
        if nombre not in self._productos:
            raise KeyError(f"El producto '{nombre}' no existe")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if cantidad > self._productos[nombre]["cantidad"]:
            raise ValueError("Stock insuficiente")
        self._productos[nombre]["cantidad"] -= cantidad

    def cantidad(self, nombre):
        """Unidades disponibles de un producto (0 si no existe)."""
        return self._productos.get(nombre, {}).get("cantidad", 0)

    def valor_total(self):
        """Valor total del inventario (cantidad x precio)."""
        return sum(p["cantidad"] * p["precio"] for p in self._productos.values())
