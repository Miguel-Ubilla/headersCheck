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

### **Usage**

- Run the script:

  ```bash
  python headerscheck.py
  ```

- Enter the website URL to analyze.
- Optional: Enter a cookie if necessary.

The script will display a detailed report of the present and absent headers, along with their level of severity.

### **Contributions**

Contributions are welcome. Please, send your pull requests or open issues to discuss possible improvements.

### **License**

This project is licensed under the MIT license..

### **Author**

Miguel Ubilla Rocco
