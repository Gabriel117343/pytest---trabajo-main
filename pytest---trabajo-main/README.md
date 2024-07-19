## Utilización de la Librería PyTest

En este documento, explicamos cómo crear pruebas unitarias para las funciones `ingresardatos()`, `modificardatos()` y una función adicional que elegiremos en conjunto, utilizando la librería PyTest. Además, trabajaremos con Jira para la gestión de tareas y Confluence para la documentación del proyecto.

### Integrantes del Equipo

- **Gabriel**
- **Emerson**
- **Luis**

### Pasos para Crear Pruebas Unitarias

1. **Instalación de PyTest**
    - para activa el entorno virtual ejecutar > .\venv\Scripts\activate
    - > pip list "mostrara las dependencias del proyecto"
    - Luego, asegúrarse de tener instalada la librería PyTest. La forma de instalarla es a través del siguiente comando:
    ```bash
    pip install pytest

    ```
    - > pip list "resultado - pytest 8.2.2 - "

2. **Estructura de los Archivos de Pruebas**
    - Crea un directorio llamado `tests` en la raíz de nuestro proyecto.
    - Dentro del directorio `tests`, vamos a crear archivos de pruebas para cada función que deseamos probar. La convención para nombrar estos archivos es `test_<nombre_funcion>.py`.

3. **Asignación de Funciones para Pruebas Unitarias**
    - **Emerson** se encargará de las pruebas para `ingresardatos()`.
    - **Luis** se encargará de las pruebas para `modificardatos()`.
    - **Gabriel** se encargará de las pruebas para una función adicional que elegiremos.

4. **Creación de las Pruebas Unitarias**
    - **Emerson: Pruebas para `ingresardatos()`**
        - Crea un archivo llamado `test_ingresardatos.py` en el directorio `tests`.
        - Dentro del archivo, importa la función y escribe las pruebas unitarias.

    - **Luis: Pruebas para `modificardatos()`**
        - Crea un archivo llamado `test_modificardatos.py` en el directorio `tests`.
        - Dentro del archivo, importa la función y escribe las pruebas unitarias.

    - **Gabriel: Pruebas para la Función Elegida por el Equipo**
        - Vamos a seleccionar una función adicional para probar.
        - Crea un archivo llamado `test_<nombre_funcion>.py` en el directorio `tests`.
        - Dentro del archivo, importa la función y escribe las pruebas unitarias.

5. **Ejecutar las Pruebas**
    - Para ejecutar las pruebas unitarias, navega hasta la raíz de nuestro proyecto y utiliza el siguiente comando:
    ```bash
    pytest
    ```

6. **Resultados de las Pruebas**
    - PyTest ejecutará todas las pruebas y mostrará un resumen de los resultados en la consola. Asegúrate de que todas las pruebas pasen correctamente.

### Herramientas de Gestión y Documentación

- **Jira**: Utilizaremos Jira para la gestión de tareas, seguimiento de incidencias y planificación del proyecto.
- **Confluence**: Utilizaremos Confluence para la documentación del proyecto, donde almacenaremos y organizaremos toda la información relevante.

Con estos pasos podemos asegurarnos de que las funciones `ingresardatos()`, `modificardatos()` y la función adicional elegida por el equipo funcionan correctamente y cumplen con los requisitos esperados. Además, con la ayuda de Jira y Confluence, mantendremos una gestión eficiente y una documentación detallada del proyecto.
