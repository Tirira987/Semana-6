# modelos/platillo.py
from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa una comida específica del restaurante."""

    def __init__(self, nombre: str, precio: float, tipo_platillo: str, disponible: bool = True):
        # Invocamos al constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo específico de la clase hija
        self.tipo_platillo = tipo_platillo

    def mostrar_informacion(self) -> str:
        """Método de la clase padre para demostrar polimorfismo."""
        estado = "Disponible" if self.disponible else "No Disponible"
        return (f"🍽️  [Platillo] {self.nombre:<18} | Tipo: {self.tipo_platillo:<10} | "
                f"Precio: ${self.obtener_precio():.2f} | {estado}")