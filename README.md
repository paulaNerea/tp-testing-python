# Trabajo Práctico: Pruebas de Software (Testing)

**Integrantes:**
* Carretero, Miguel Ángel - 42718309
* Gutierrez, Martina del Pilar - 45669770
* Leal Villanueva, Paula Nerea - 45231642

**Tecnologías utilizadas:** Python y Pytest.

## 🛠️ Entorno Virtual

Para este proyecto configuramos un entorno virtual (`venv`). Esto funciona como una burbuja que aísla nuestro proyecto del resto de la computadora.

#### Beneficios:

1. Asegura que todos descarguemos exactamente la misma versión de `pytest` (evitando errores de compatibilidad si alguien tiene versiones viejas).
2. Las librerías se instalan solo adentro de esta carpeta y no ensucian el sistema global.

## Pasos para correr las pruebas:

1. Clonar el repositorio.
2. Crear la burbuja en su terminal: `python -m venv venv`
3. Actívela:
   - En Windows: `.\venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`
4. Instalar las dependencias exactas: `pip install -r requirements.txt`
5. Ejecutar los tests corriendo: `python -m pytest`

## Cobertura de las pruebas

Para ver qué partes del código se ejecutan durante las pruebas usamos `pytest-cov`:

```bash
python -m pytest --cov=producto --cov=tienda --cov-branch --cov-report=term-missing --cov-report=html
```

El resultado aparece en la terminal y también se genera un informe en `htmlcov/index.html`, que se puede abrir en el navegador. La medición se realiza sobre `producto.py` y `tienda.py`.

**Resultado de la verificación:** 22 pruebas aprobadas y 100% de cobertura de líneas y ramas en ambas clases.

## Organización de las pruebas

* `tests/conftest.py`: Fixtures que preparan un producto, una tienda vacía y una tienda con yogur, pan y leche. Cada prueba recibe objetos nuevos.
* `tests/test_producto.py`: Pruebas de actualización de precios y manejo de precios negativos.
* `tests/test_tienda.py`: Pruebas del inventario, descuentos, excepciones y el descuento con un mock.
* `tests/test_carrito.py`: Pruebas del total del carrito y del flujo completo después de aplicar descuentos.

El carrito se representa con una lista de nombres de productos. Si un nombre aparece dos veces, se suma su precio dos veces. Si un producto no existe, se lanza la excepción de `buscar_producto`.

---

## 📝 Respuestas Teóricas

### Punto 1: Pruebas Básicas

* **¿Se aplicaron pruebas de unidad o de integración?**

Identificamos pruebas de unidad y de integración. Las pruebas de `actualizar_precio` son unitarias porque comprueban el comportamiento de la clase Producto. En las pruebas del inventario usamos objetos reales de Producto junto con Tienda, por lo que comprobamos la colaboración entre ambas clases. En el punto 5 también realizamos una prueba de integración que combina la carga de productos, los descuentos y el cálculo del carrito.

### Punto 2: Excepciones y TDD

* **¿Cómo ayuda escribir los tests antes que el código?**

Escribir las pruebas antes que el código (enfoque TDD) nos obliga a pensar en el diseño de las clases y en los casos límite (como precios negativos o buscar productos inexistentes) desde la perspectiva de quien va a consumir la función. Además, garantiza que el código sea testeable desde el primer momento y evita que escribamos código innecesario, ya que solo desarrollamos la lógica estrictamente obligatoria para que la prueba pase.

* **¿Cómo sería el proceso de escribir primero los tests?**

Podríamos empezar escribiendo una prueba que espere un `ValueError` al actualizar un precio a un valor negativo. Al ejecutarla antes de implementar la validación, la prueba debería fallar. Después agregaríamos el código necesario para que pase y, por último, mejoraríamos el código sin cambiar su comportamiento, volviendo a ejecutar todas las pruebas. Este ciclo se conoce como rojo, verde y refactorización.

### Punto 3: Dobles de Prueba

* **¿Podemos identificar Controladores y Resguardos?**

Las funciones de prueba cumplen el papel de controladores porque preparan los datos, llaman a los métodos de las clases y verifican los resultados; pytest se encarga de ejecutarlas. El producto simulado reemplaza al objeto real y cumple el papel de un resguardo para aislar la clase Tienda. En nuestro caso usamos un mock porque además verificamos que se llame a `actualizar_precio` una sola vez con el precio esperado.

* **¿Qué es un test double? ¿Hay otros nombres para los objetos simulados?**

Un test double es un objeto que reemplaza a otro durante una prueba para controlar sus respuestas o evitar depender de su implementación real. Hay distintos tipos: un stub devuelve respuestas preparadas, un mock permite verificar llamadas, un spy registra las llamadas y un fake ofrece una implementación simplificada. Usamos `MagicMock` como producto con un precio de 500 y comprobamos que un descuento del 20% llame a `actualizar_precio(400.0)`.

### Punto 4: Fixtures

* **¿Qué es un fixture según la práctica realizada?**

Un fixture es una función que prepara los datos o el entorno que necesitan las pruebas. En `conftest.py` usamos `@pytest.fixture` para crear un producto, una tienda vacía y una tienda con tres productos. Los tests reciben estos datos indicando el nombre del fixture como parámetro. Como usamos el alcance por defecto, cada prueba recibe una preparación nueva y los cambios de una prueba no afectan a las demás.

* **¿Qué ventajas vemos en el uso de fixtures?**

Nos permiten evitar repetir la creación de la tienda y los productos en cada test. También hacen que las pruebas sean más fáciles de leer y mantener: si necesitamos cambiar los datos iniciales, lo hacemos en un solo lugar. Además, cada prueba empieza con un estado conocido.

* **¿Qué enfoque de diseño de pruebas aplicamos: caja negra o blanca?**

El uso de fixtures por sí solo no define el enfoque. Diseñamos principalmente los casos a partir del comportamiento esperado: buscar un producto devuelve el producto, un precio negativo lanza una excepción y el carrito devuelve la suma correcta. Esto corresponde a caja negra. También comprobamos el inventario interno en algunos tests y medimos las ramas del código para evaluar la cobertura, incorporando aspectos de caja blanca.

* **¿Qué son Setup y Teardown?**

Setup es la preparación que se realiza antes de una prueba, como crear la tienda y cargar sus productos. Teardown es la limpieza posterior, como cerrar archivos o conexiones que se hayan abierto. En este proyecto trabajamos con objetos en memoria y no abrimos recursos que necesiten un cierre explícito. Los fixtures crean objetos nuevos para cada prueba, así que no necesitamos agregar una limpieza manual del inventario.

### Punto 5: Integración y Cobertura

* **¿Cómo probamos el flujo completo?**

Usamos el fixture con un yogur de 1500, un pan de 1000 y una leche de 2000. Aplicamos un descuento del 10% al yogur y del 20% al pan, que quedan en 1350 y 800. Después calculamos el total del carrito con los tres productos y verificamos que sea 4150. En esta prueba usamos objetos reales de Producto y Tienda, para comprobar que los descuentos se reflejen en el total. También probamos un carrito vacío, un solo producto, productos repetidos y un producto inexistente.

* **¿Realizamos una prueba de cobertura completa? ¿Qué tipo de cobertura utilizamos?**

Medimos la cobertura con `pytest-cov` y la opción `--cov-branch`. Obtuvimos 100% de cobertura de líneas y ramas en `producto.py` y `tienda.py`: se ejecutaron las 40 sentencias y las 14 ramas que informó la herramienta. Probamos resultados válidos, excepciones y valores límite, como precio cero y descuentos de 0% y 100%. Esta cobertura no significa que hayamos probado todas las combinaciones posibles de entradas o todos los caminos, ni garantiza que el programa no tenga errores.

* **¿Cómo sería una situación de integración ascendente en este caso?**

Podríamos comenzar probando Producto de forma independiente, verificando sus precios y excepciones. Después integraríamos esa clase real con Tienda para probar el inventario y los descuentos. Por último, probaríamos el flujo del carrito usando ambas clases ya verificadas. Así avanzaríamos desde el componente más independiente hacia las funciones que dependen de él. En orientación a objetos, este orden también se relaciona con la integración basada en uso que vimos en los apuntes. Las funciones de prueba actuarían como controladores para ejecutar cada etapa.
