"""
Fichero: algebra/vectores.py
Autor: Albert Blázquez Badenas

Este módulo implementa la clase Vector con operaciones de suma, 
producto de Hadamard, producto escalar y descomposición ortogonal.

Tests unitarios:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2.0, 4.0, 6.0])
>>> v1 * v2
Vector([4.0, 10.0, 18.0])
>>> v1 @ v2
32.0
>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])
>>> v3 % v4
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    def __init__(self, componentes):
        """Construye el vector a partir de una lista de elementos."""
        self.componentes = [float(x) for x in componentes]

    def __repr__(self):
        """Representación visual del vector."""
        return f"Vector({self.componentes})"

    def __add__(self, otro):
        """Suma de dos vectores."""
        return Vector([a + b for a, b in zip(self.componentes, otro.componentes)])

    def __mul__(self, otro):
        """Producto de Hadamard (vector * vector) o Escalar (vector * número)."""
        if isinstance(otro, (int, float)):
            return Vector([a * otro for a in self.componentes])
        elif isinstance(otro, Vector):
            return Vector([a * b for a, b in zip(self.componentes, otro.componentes)])
        return NotImplemented

    def __rmul__(self, otro):
        """Permite la multiplicación por escalar a la izquierda (número * vector)."""
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """Producto escalar usando el operador @."""
        return sum(a * b for a, b in zip(self.componentes, otro.componentes))

    def __floordiv__(self, otro):
        """Componente paralela de self respecto a otro (operador //)."""
        # Fórmula: v1|| = (v1 · v2 / |v2|^2) * v2
        factor = (self @ otro) / (otro @ otro)
        return otro * factor

    def __mod__(self, otro):
        """Componente normal de self respecto a otro (operador %)."""
        # Fórmula: v1_perpendicular = v1 - v1||
        v_paralelo = self // otro
        return Vector([a - b for a, b in zip(self.componentes, v_paralelo.componentes)])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)