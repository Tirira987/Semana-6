# main.py
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    # 1. Instanciar el servicio del restaurante
    mi_restaurante = Restaurante("Sabores Amazónicos")
    
    print("--- REGISTRANDO PRODUCTOS EN EL SISTEMA ---")
    # 2. Crear instancias de Platillo (2 objetos)
    platillo_1 = Platillo("Maito de Pescado", 8.50, "Fuerte")
    platillo_2 = Platillo("Volquetero", 6.00, "Entrada")
    
    # 3. Crear instancias de Bebida (2 objetos)
    bebida_1 = Bebida("Chicha de Chonta", 2.00, 500)
    bebida_2 = Bebida("Jugos Naturales", 1.50, 400)
    
    # 4. Agregar objetos al servicio
    mi_restaurante.agregar_producto(platillo_1)
    mi_restaurante.agregar_producto(platillo_2)
    mi_restaurante.agregar_producto(bebida_1)
    mi_restaurante.agregar_producto(bebida_2)
    
    # 5. Demostración de Encapsulación y Validación de reglas de negocio
    print("\n--- PRUEBA DE ENCAPSULACIÓN Y VALIDACIÓN ---")
    print(f"Precio original de {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")
    
    print("\nIntentando cambiar precio a un valor inválido (-3.50):")
    platillo_1.cambiar_precio(-3.50)  # Debería mostrar mensaje de error
    
    print("\nIntentando cambiar precio a un valor válido (9.25):")
    platillo_1.cambiar_precio(9.25)   # Debe actualizarse correctamente
    print(f"Nuevo precio de {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")
    
    # 6. Mostrar el menú final aplicando Polimorfismo
    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    ejecutar_sistema()