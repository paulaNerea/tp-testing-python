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
5. Ejecutar los tests corriendo: `pytest`

---

## 📝 Respuestas Teóricas

### Punto 1: Pruebas Básicas
* **¿Se aplicaron pruebas de unidad o de integración?**  
Aplicamos pruebas de integración. Aunque el objetivo principal era evaluar los métodos de la clase Tienda (agregar, buscar y eliminar), para que estas pruebas funcionen tuvimos que instanciar y pasarle objetos reales de la clase Producto. Al no aislar la tienda, el test está evaluando el funcionamiento conjunto y la interacción real entre ambas clases, lo cual define a una prueba de integración.

### Punto 2: Excepciones y TDD
* **¿Cómo ayuda escribir los tests antes que el código?**  
Escribir las pruebas antes que el código (enfoque TDD) nos obliga a pensar en el diseño de las clases y en los casos límite (como precios negativos o buscar productos inexistentes) desde la perspectiva de quien va a consumir la función. Además, garantiza que el código sea testeable desde el primer momento y evita que escribamos código innecesario, ya que solo desarrollamos la lógica estrictamente obligatoria para que la prueba pase.