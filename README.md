# StayUniqueTest

# Extracción de Datos de Hoteles en Booking.com

Este proyecto utiliza **Python** y la biblioteca **Playwright** para extraer datos de hoteles de Booking.com. Los datos incluyen nombre del hotel, precio, puntaje promedio y cantidad de reseñas. A continuación, se detalla el proceso de configuración, ejecución y limpieza de datos, así como el pipeline ETL y los desafíos enfrentados.

## Tabla de Contenidos
1. [Configuración del Entorno](#configuración-del-entorno)
2. [Ejecución de Scripts](#ejecución-de-scripts)
3. [Decisiones de Limpieza de Datos](#decisiones-de-limpieza-de-datos)
4. [Pipeline ETL](#pipeline-etl)
5. [Retos y Soluciones](#retos-y-soluciones)

### Configuración del Entorno

1. **Instalacion de python y dependencias**:
   Asegurece de tener Python 3.7+ instalado.
   Instala las dependencias enumeradas en requirements.txt
   ```bash
  pip install -r requirements.txt
  
Instala la ultima version de **Playwright** y sus navegadores:
   ```bash
  pip install playwright
   playwright install```
