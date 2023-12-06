#!/usr/bin/env python3
import requests
from colorama import init, Fore

security_headers = {
    "X-XSS-Protection": "deprecated",
    "X-Frame-Options": "medium",
    "X-Content-Type-Options": "medium",
    "Strict-Transport-Security": "high",
    "Content-Security-Policy": "medium",
    "X-Permitted-Cross-Domain-Policies": "deprecated",
    "Referrer-Policy": "medium",
    "Expect-CT": "deprecated",
    "Permissions-Policy": "medium",
    "Cross-Origin-Embedder-Policy": "medium",
    "Cross-Origin-Resource-Policy": "medium",
    "Cross-Origin-Opener-Policy": "medium",
}

information_headers = {
    "X-Powered-By": "high",
    "Server": "high",
    "Access-Control-Allow-Origin": "medium",
}

cache_headers = {"Cache-Control", "Pragma", "Last-Modified", "Expires", "ETag"}


def title():
    print("\033[1;36m")
    print("╔═════════════════════════════════════════════════════════════════════╗")
    print("║                HeadersCheck - Security Audit Tool                   ║")
    print("║                          by Miguel Ubilla                           ║")
    print("╚═════════════════════════════════════════════════════════════════════╝")
    print("\033[0;0m")
    print("")


init(autoreset=True)


def categorize_header(header, value):
    severity_color = {
        "high": Fore.RED,
        "medium": Fore.YELLOW,
        "deprecated": Fore.LIGHTBLACK_EX,
        "info": Fore.WHITE,
    }

    if header in security_headers:
        if value:
            return f"{header}: {Fore.GREEN}{value}"
        else:
            color = severity_color.get(security_headers[header], Fore.WHITE)
            return f"{header}: {color}NO PRESENTE{Fore.WHITE}"

    elif header in information_headers:
        category = information_headers[header]
        if value:
            color = Fore.RED if category == "high" else Fore.YELLOW
            return f"{header}: {color}{value}"
        else:
            color = Fore.GREEN if category == "high" else Fore.YELLOW
            return f"{header}: {color}NO PRESENTE{Fore.WHITE}"

    elif header in cache_headers:
        return f"{header}: {Fore.WHITE}{value if value else 'NO PRESENTE'}"

    return f"{header}: {Fore.WHITE}{value if value else 'NO PRESENTE'}"


def check_security_headers(url, cookie=None):
    headers = {}
    if cookie:
        headers["Cookie"] = cookie

    present_count = 0
    absent_count = 0

    try:
        response = requests.head(url, headers=headers)

        print(Fore.LIGHTBLUE_EX + f"\nHeaders de seguridad para {url}:\n")
        for header in security_headers.keys():
            value = response.headers.get(header)
            print(categorize_header(header, value))
            if value:
                present_count += 1
            else:
                absent_count += 1

        print(Fore.LIGHTBLUE_EX + "\nHeaders Informativos:\n")
        for header in information_headers:
            value = response.headers.get(header)
            print(categorize_header(header, value))

        print(Fore.LIGHTBLUE_EX + "\nHeaders de cache:\n")
        for header in cache_headers:
            value = response.headers.get(header)
            print(categorize_header(header, value))

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

    print(
        Fore.WHITE
        + "\n--------------------------------------------------------------------"
    )
    print("Headers de seguridad presentes: " + Fore.GREEN + f"{present_count}")
    print("Headers de seguridad ausentes: " + Fore.RED + f"{absent_count}")


def main():
    title()
    url = input("Ingresa la URL: ")
    cookie = input("Ingresa la cookie (puede dejarlo en blanco si no es necesario): ")
    check_security_headers(url, cookie.strip() or None)


if __name__ == "__main__":
    main()
