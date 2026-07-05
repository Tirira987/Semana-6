# modelos/bebida.py
from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida del restaurante."""

    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponible: bool = True):
        # Invocamos al constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo específico de la clase hija
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método de la clase padre para demostrar polimorfismo."""
        estado = "Disponible" if self.disponible else "No Disponible"
        return (f"🥤 [Bebida]   {self.nombre:<18} | Vol: {self.volumen_ml:>4} ml  | "
                f"Precio: ${self.obtener_precio():.2f} | {estado}")