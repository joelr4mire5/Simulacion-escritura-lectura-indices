import pickle


class Producto:
    def __init__(self, nombre, codigo, peso_unitario, nombre_proveedor):
        self._nombre=nombre,
        self._codigo = codigo,
        self._peso_unitario = peso_unitario,
        self._nombre_proveedor = nombre_proveedor


    def __repr__(self):
        return F"Producto(nombre={self._nombre},codigo={self._codigo},peso_unitario={self._peso_unitario},nombre_proveedor={self._nombre_proveedor})"
