# StayUniqueTest
## Scrapeing de Hoteles en Booking.com

Este proyecto es un scraper que utiliza Playwright para extraer informacion de hoteles en Booking.com y almacenar los datos en un archivo CSV.

## Tabla de Contenidos
1. [Configuracion del Entorno](#configuracion-del-entorno)
2. [Ejecucion del Script](#ejecucion-del-script)
3. [Decisiones de Limpieza de Datos](#decisiones-de-limpieza-de-datos)
4. [Pipeline de ETL Implementado](#pipeline-de-etl-implementado)
5. [Retos y Soluciones](#retos-y-soluciones)

## Configuracion del Entorno

Para configurar el entorno, sigue estos pasos:

1. **Instala Python**: Asegurate de tener Python 3.7 o superior instalado en tu maquina. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. **Instala las dependencias**: Usa `pip` para instalar las bibliotecas necesarias.

3. **Instala los navegadores necesarios**: Ejecuta el comando correspondiente para instalar los navegadores requeridos por Playwright.

## Ejecucion del Script

Para ejecutar el script de scraping, sigue estos pasos:

1. Asegurate de que el entorno este activado y las dependencias instaladas.

2. Guarda el script en un archivo llamado `scraper.py`.

3. Ejecuta el script desde la linea de comandos.

4. El archivo `hoteles_barcelona.csv` se generara en el mismo directorio del script, conteniendo la informacion de los hoteles extraida.

## Decisiones de Limpieza de Datos

Durante la recopilacion de datos, se tomaron las siguientes decisiones de limpieza:

- **Manejo de Datos Faltantes**: En caso de que alguna informacion no estuviera disponible (por ejemplo, si no habia puntuacion o precio), se asigno un valor 'N/A' para indicar que la informacion no estaba disponible.
  
- **Conversion de Tipos**: Las reseñas contadas se almacenan como texto; si se requiere analisis numerico posterior, se puede convertir a tipo numerico durante la carga de datos.

## Pipeline de ETL Implementado

El proceso de extraccion, transformacion y carga (ETL) se implemento de la siguiente manera:

1. **Extraccion**: Se realiza la navegacion a la URL de busqueda de Booking.com y se obtienen los datos de los hoteles visibles en la pagina.

2. **Transformacion**: Se almacenan los datos extraidos en una lista de diccionarios y se limpian los datos para asegurar que no falten campos clave.

3. **Carga**: Se convierte la lista de diccionarios en un DataFrame de pandas y se guarda el DataFrame en un archivo CSV para su uso posterior.

## Retos y Soluciones

- **Carga Dinámica de Resultados**: Booking.com carga resultados de manera dinamica mientras se desplaza hacia abajo, lo cual dificultaba 
     la extracción de un número específico de resultados.
Esta carga lenta puede provocar que el scraping en cuestion termine antes de los previsto sin la carga de cantidad objetivo de datos a buscar(variable a deseo del usuario)
Se implemento un tiempo de espera despues de cada scroll para permitir que la pagina cargue mas resultados.
**Solución**: Se utilizó un bucle while para desplazar la página de forma iterativa hasta que se alcanzaron al menos 120 hoteles, evitando tiempos de espera innecesarios.

- **Datos Faltantes**: No todos los hoteles tienen precios o calificaciones disponibles, lo que ocasionaba errores en tiempo de ejecución.
	 **Solución:** Se aplicaron bloques try-except en cada campo para manejar los datos faltantes asignando valores None cuando sea necesario.

- **Bloqueo de IP**: Realizar multiples solicitudes en un corto periodo puede resultar en un bloqueo temporal de la IP. 
**Solución:** Para mitigar esto, el navegador se ejecuta en modo visual (headless=False) y se aplican pausas (time.sleep) para simular un comportamiento humano.



