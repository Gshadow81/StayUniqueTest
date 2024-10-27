# StayUniqueTest

Extracción de Datos de Hoteles en Booking.com
Este proyecto utiliza Python y la biblioteca Playwright para extraer datos de hoteles de Booking.com. Los datos incluyen nombre del hotel, precio, puntaje promedio y cantidad de reseñas. A continuación, se detalla el proceso de configuración, ejecución y limpieza de datos, así como el pipeline ETL y los desafíos enfrentados.

Tabla de Contenidos
Configuración del Entorno
Ejecución de Scripts
Decisiones de Limpieza de Datos
Pipeline ETL
Retos y Soluciones
Configuración del Entorno
Clona el repositorio:

bash
Copiar código
git clone <URL_del_repositorio>
cd <nombre_del_repositorio>
Instalación de Python y dependencias:

Asegúrate de tener Python 3.7+ instalado.
Crea un entorno virtual y actívalo:
bash
Copiar código
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
Instala las dependencias enumeradas en requirements.txt:
bash
Copiar código
pip install -r requirements.txt
Nota: Asegúrate de tener la última versión de Playwright y sus navegadores:
bash
Copiar código
pip install playwright
playwright install
Ejecución de Scripts
Ejecuta el script principal:

Desde la terminal, ejecuta:
bash
Copiar código
python main.py
El script abrirá el navegador y comenzará a extraer datos de hoteles hasta alcanzar al menos 120 registros, almacenándolos en un archivo CSV llamado hoteles_barcelona.csv.
Parámetros modificables:

En el código, se pueden ajustar las fechas de check-in y check-out para obtener información de otras fechas:
python
Copiar código
checkin_date = 'YYYY-MM-DD'
checkout_date = 'YYYY-MM-DD'
Decisiones de Limpieza de Datos
El script aplica las siguientes decisiones de limpieza para asegurar la calidad de los datos obtenidos:

Valores Nulos: Dado que algunos hoteles pueden no tener precio, puntaje o cantidad de reseñas visibles, el script maneja estas ausencias y los valores nulos se establecen como None.
Formato de Precios: Los precios extraídos pueden incluir símbolos de moneda, los cuales no se eliminan en esta versión para permitir flexibilidad en el análisis de costos en diferentes monedas.
Formato de Reseñas: La cantidad de reseñas se extrae como un texto que incluye la palabra "reseñas". Se eliminan textos adicionales para dejar solo el número en el campo correspondiente.
Pipeline ETL
El pipeline ETL (Extracción, Transformación, Carga) consta de los siguientes pasos:

Extracción: Se utilizan los selectores de Playwright para capturar datos de hoteles como nombre, precio, puntaje y cantidad de reseñas desde Booking.com.
Transformación:
El script limpia los datos extraídos para eliminar texto redundante y tratar valores faltantes.
Se aplican bloques de try-except para manejar valores que no están presentes.
Carga: Finalmente, los datos transformados se guardan en un archivo CSV (hoteles_barcelona.csv) para su análisis posterior.
Retos y Soluciones
Carga Dinámica de Resultados:

Reto: Booking.com carga resultados de manera dinámica mientras se desplaza hacia abajo, lo cual dificultaba la extracción de un número específico de resultados.
Solución: Se utilizó un bucle while para desplazar la página de forma iterativa hasta que se alcanzaron al menos 120 hoteles, evitando tiempos de espera innecesarios.
Datos Faltantes:

Reto: No todos los hoteles tienen precios o calificaciones disponibles, lo que ocasionaba errores en tiempo de ejecución.
Solución: Se aplicaron bloques try-except en cada campo para manejar los datos faltantes asignando valores None cuando sea necesario.
Bloqueo por Parte de Booking:

Reto: Las páginas pueden detectar accesos automatizados y bloquear solicitudes.
Solución: Para mitigar esto, el navegador se ejecuta en modo visual (headless=False) y se aplican pausas (time.sleep) para simular un comportamiento humano.
