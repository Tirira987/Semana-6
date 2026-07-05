# servicios/restaurante.py
from modelos.producto import Producto

class Restaurante:
    """Clase de servicio encargada de gestionar el menú de productos."""

    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento = nombre_establecimiento
        # Lista interna que almacenará objetos de tipo Producto (Platillos y Bebidas)
        self.__menu = []

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto al menú."""
        self.__menu.append(producto)
        print(f"[Sistema]: '{producto.nombre}' ha sido agregado al menú con éxito.")

    def mostrar_menu_completo(self) -> None:
        """Recorre la lista aplicando Polimorfismo al invocar 'mostrar_informacion()'."""
        print(f"\n======================================================================")
        print(f"               MENÚ DEL RESTAURANTE: {self.nombre_establecimiento.upper()}      ")
        print(f"======================================================================")
        
        if not self.__menu:
            print("El menú se encuentra vacío actualmente.")
            return

        for producto in self.__menu:
            # Aquí ocurre el Polimorfismo: Python detecta en tiempo de ejecución 
            # si debe llamar al método de Platillo o de Bebida de forma dinámica.
            print(producto.mostrar_informacion())
            
        print(f"======================================================================\n")