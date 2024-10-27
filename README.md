# StayUniqueTest
## Scraping de Hoteles en Booking.com

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

2. **Instala las dependencias**: Usa `pip` para instalar las bibliotecas necesarias
     `pip install playwright pandas`
     `playwright install`

3. **Instala los navegadores necesarios**: Ejecuta el comando correspondiente para instalar los navegadores requeridos por Playwright.

## Ejecucion del Script

Para ejecutar el script de scraping, sigue estos pasos:

1. Asegurate de que el entorno este activado y las dependencias instaladas.

2. Guarda el script en un archivo llamado `barcelona_scraping.py`.

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

  
# Análisis de Datos de Propertys y Bookings

Este proyecto realiza un análisis de datos utilizando dos conjuntos de datos: `Properties.csv` y `Bookings.csv`. El código carga, limpia, transforma y une estos datos, proporcionando un archivo CSV final listo para análisis.

## Requisitos

Asegúrate de tener las siguientes librerías instaladas:

- `pandas`

Puedes instalar `pandas` usando pip:

```bash
pip install pandas
```

## Archivos Necesarios

- `dataset/Properties.csv`
- `dataset/Bookings.csv`

Asegúrate de que los archivos estén en la ruta correcta antes de ejecutar el código.

## Descripción del Código

### 1. Importar Librerías

```python
import pandas as pd
```

### 2. Cargar los Datos

Se cargan los archivos `Properties.csv` y `Bookings.csv`.

### 3. Limpieza y Transformación de Datos

#### Properties
- Se convierte la columna `ReadyDate` a tipo `datetime`.
- Se reemplazan los valores nulos en `PropertyType` con 'Unknown'.

#### Bookings

- Se convierten las columnas de fecha a tipo `datetime`.
- Se manejan los valores nulos en columnas importantes.

### 4. Análisis Exploratorio de Datos (EDA)

Se muestran estadísticas descriptivas para ambos conjuntos de datos

### 5. Unificación de los Datasets

Los datasets se fusionan utilizando `PropertyId` como clave

### 6. Verificación de Valores Nulos

Se revisan los valores nulos en el dataset unificado

### 7. Rellenar Valores Nulos Remanentes

Se rellenan los valores nulos restantes después de la fusión

### 8. Guardar el Dataset Unificado

Finalmente, se guarda el dataset unificado en un archivo CSV

## Analisis del dataset merged_properties_bookings
En este pequeño analisis podemos encontrar las siguientes concluciones:
-en la categoria de reservas podemos encontrar 4 tipos de propiedas que se repiten las cuales son unknow, house, apartment y Apa, debido a mi falta de conocimiento en el area de hoteleria asumire que Apa hace referencia a Apartment debido a que hay ingreso de datos de diferentes paginas de hoteleria asi que el nombramiento de la data puede variar entre estas, ya mencionado esto renombramos Apa a apartment para poder visualizar graficamente cual es el tipo de propiedad que se renta con mas frencuencia tambien dandonos a entender que la data debe pasar por una mayor capa de limpieza individual por columna, lo cual originalmente no fue previsto debido a que post merged terminaron resultando 24 columnas esto no solo se presentara en este columnas tambien a la hora de hacer calculos sobre pricing cuando busquemos los menos precios tendremos precios muy bajos cercanos a 0
