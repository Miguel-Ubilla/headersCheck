# **HeadersCheck**

## **Description**

HeadersCheck is a security audit tool designed to analyze and report on the security HTTP headers of a website. Written in Python, this tool classifies and displays security, informational, and cache headers, indicating their presence and level of importance.

## **Features**

- **Security Headers Analysis**: Evaluates common headers like X-XSS-Protection, Strict-Transport-Security, among others.
- **Severity Classification**: Headers are color-coded according to their level of importance: high, medium, or deprecated.
- **Support for Informational and Cache Headers**: Analyzes headers like Server, Cache-Control, etc.
- **Colorful Output**: Uses Colorama for an easy-to-read and visually differentiated output.

### **Requirements**

- Python 3
- Libraries: requests, colorama

### **Installation**

- Clone the repository or download the files.
- Install the dependencies:

  ```bash
  pip install requests colorama
  ```

##### Usage

Run the script:

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
