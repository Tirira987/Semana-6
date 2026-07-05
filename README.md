# Sistema de Gestión de Restaurante (restaurante_app)

Este proyecto corresponde a la **Semana 6** de la asignatura **Programación Orientada a Objetos**. Consiste en una aplicación modular de consola desarrollada en Python que simula la administración de un menú gastronómico mediante la implementación práctica de los pilares de la POO.

## Información del Estudiante
* **Nombre Completo:** Richard Arturo Tirira Díaz
* **Institución:** Universidad Estatal Amazónica (UEA)
* **Carrera:** Tecnologías de la Información

---

## Estructura del Proyecto
El proyecto se organiza bajo un enfoque estrictamente modular, separando las responsabilidades de definición de entidades de las de lógica de negocio y ejecución:

* **`modelos/`**: Paquete que contiene la definición de las clases del dominio.
    * `producto.py`: Contiene la clase base (padre) con propiedades genéricas.
    * `platillo.py` y `bebida.py`: Clases derivadas (hijas) con propiedades específicas.
* **`servicios/`**: Paquete de control.
    * `restaurante.py`: Administra las colecciones de objetos y gestiona la visualización.
* **`main.py`**: Script principal de arranque y orquestación.

---

## Aplicación de Principios de la POO

### 1. Herencia
Se implementó una jerarquía clara donde `Producto` actúa como clase contenedora general de atributos comunes (`nombre`, `__precio`, `disponible`). Las clases `Platillo` (con el atributo propio `tipo_platillo`) y `Bebida` (con el atributo propio `volumen_ml`) extienden a la clase padre haciendo uso explícito de la función `super().__init__()` para optimizar y reutilizar lógica constructora.

### 2. Encapsulación
El atributo `precio` dentro de la clase `Producto` se ha protegido bajo el identificador privado `__precio`. El acceso externo y manipulación de este dato se restringe y controla formalmente mediante los métodos de interfaz:
* `obtener_precio()` (Getter)
* `cambiar_precio()` (Setter), el cual incluye una validación de seguridad lógica que impide la asignación de valores numéricos menores o iguales a cero.

### 3. Polimorfismo
El polimorfismo se hace evidente al invocar el método `mostrar_informacion()`. A pesar de que la clase de servicio `Restaurante` procesa todos los elementos de manera abstracta como referencias homogéneas dentro de una misma lista (`__menu`), Python resuelve dinámicamente en tiempo de ejecución el tipo de objeto específico (`Platillo` o `Bebida`), imprimiendo los formatos y atributos particulares de cada entidad derivada.

---

## Reflexión sobre la Modularidad en POO
La separación de código en paquetes modulares (`modelos` y `servicios`) combinada con los pilares de la POO confiere un nivel de escalabilidad industrial al software en Python. Rediseñar o expandir el menú (por ejemplo, añadir una clase hija `Postre`) no interrumpe el funcionamiento del módulo de servicios actual. La encapsulación garantiza que las reglas del negocio permanezcan centralizadas y protegidas de corrupciones externas, facilitando el mantenimiento y la lectura de código de manera limpia y estandarizada.
