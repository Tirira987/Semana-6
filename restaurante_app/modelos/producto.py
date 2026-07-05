# modelos/producto.py

class Producto:
    """Clase padre que representa un producto general del restaurante."""

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        # Atributo encapsulado (privado)
        self.__precio = 0.0
        
        # Usamos el método de modificación para validar el precio inicial
        self.cambiar_precio(precio)
        self.disponible = disponible

    # Método de acceso (Getter)
    def obtener_precio(self) -> float:
        """Devuelve el precio actual del producto."""
        return self.__precio

    # Método de modificación (Setter) con validación
    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Modifica el precio del producto validando que sea mayor a cero."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[Error]: El precio para '{self.nombre}' debe ser mayor que cero. No se aplicó el cambio.")

    def mostrar_informacion(self) -> str:
        """Método base para mostrar la información del producto."""
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"