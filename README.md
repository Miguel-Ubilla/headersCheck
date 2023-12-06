# **HeadersCheck**

#### Descripción

HeadersCheck es una herramienta de auditoría de seguridad diseñada para analizar y reportar sobre los encabezados HTTP de seguridad de un sitio web. Escrita en Python, esta herramienta clasifica y muestra los encabezados de seguridad, informativos y de caché, indicando su presencia y nivel de importancia.
Características

    Análisis de Encabezados de Seguridad: Evalúa encabezados comunes como X-XSS-Protection, Strict-Transport-Security, entre otros.
    Clasificación por Severidad: Los encabezados se marcan en colores según su nivel de importancia: alto, medio o desaprobado.
    Soporte para Encabezados Informativos y de Caché: Analiza encabezados como Server, Cache-Control, etc.
    Salida Colorida: Usa Colorama para una salida fácil de leer y visualmente diferenciada.

##### Requisitos

Python 3
Bibliotecas: requests, colorama

##### Instalación

Clona el repositorio o descarga los archivos.
Instala las dependencias:

bash

    pip install requests colorama

##### UsoUso

Ejecuta el script:

bash

    python headerscheck.py

Ingresa la URL del sitio web a analizar.
Opcional: Ingresa una cookie si es necesario.

El script mostrará un informe detallado de los encabezados presentes y ausentes, junto con su nivel de severidad.

##### ###### ContribucionesContribuciones

Las contribuciones son bienvenidas. Por favor, envía tus pull requests o abre issues para discutir posibles mejoras.

##### LicenciaLicencia

Este proyecto está licenciado bajo licencia MIT.

##### AutorAutor

Miguel Ubilla Rocco
