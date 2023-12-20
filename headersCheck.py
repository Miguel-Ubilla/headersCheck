#!/usr/bin/env python3
import requests
from colorama import init, Fore
import json

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


def title(texts):
    width = 69
    print("\033[1;36m")
    print("╔" + "═" * (width - 2) + "╗")

    title_text = texts["title"]
    title_length = len(title_text)
    left_padding = (width - title_length) // 2
    print(
        "║"
        + " " * left_padding
        + title_text
        + " " * (width - left_padding - title_length - 2)
        + "║"
    )

    print("║" + " " * 25 + "by Miguel Ubilla" + " " * 26 + "║")

    print("╚" + "═" * (width - 2) + "╝")
    print("\033[0;0m")
    print("")


init(autoreset=True)


def categorize_header(header, value, texts):
    severity_color = {
        "high": Fore.RED,
        "medium": Fore.YELLOW,
        "deprecated": Fore.LIGHTBLACK_EX,
        "info": Fore.WHITE,
    }

    no_present_text = texts["no_present"]

    if header in security_headers:
        if value:
            return f"{header}: {Fore.GREEN}{value}"
        else:
            color = severity_color.get(security_headers[header], Fore.WHITE)
            return f"{header}: {color}{no_present_text}{Fore.WHITE}"

    elif header in information_headers:
        category = information_headers[header]
        if value:
            color = Fore.RED if category == "high" else Fore.YELLOW
            return f"{header}: {color}{value}"
        else:
            color = Fore.GREEN if category == "high" else Fore.YELLOW
            return f"{header}: {color}{no_present_text}{Fore.WHITE}"

    elif header in cache_headers:
        return f"{header}: {Fore.WHITE}{value if value else no_present_text}"

    return f"{header}: {Fore.WHITE}{value if value else no_present_text}"


def check_security_headers(url, cookie, texts):
    headers = {}
    if cookie:
        headers["Cookie"] = cookie

    present_count = 0
    absent_count = 0

    try:
        response = requests.head(url, headers=headers)

        print(":\n" + Fore.LIGHTCYAN_EX + texts["site_check"] + url)
        print(Fore.LIGHTBLUE_EX + texts["security_headers_for"] + "\n")
        for header in security_headers.keys():
            value = response.headers.get(header)
            print(categorize_header(header, value, texts))
            if value:
                present_count += 1
            else:
                absent_count += 1

        print(Fore.LIGHTBLUE_EX + texts["informative_headers"])
        for header in information_headers:
            value = response.headers.get(header)
            print(categorize_header(header, value, texts))

        print(Fore.LIGHTBLUE_EX + texts["cache_headers"])
        for header in cache_headers:
            value = response.headers.get(header)
            print(categorize_header(header, value, texts))

    except requests.exceptions.RequestException as e:
        print(texts["error_request"] + str(e))

    print(
        Fore.WHITE
        + "\n--------------------------------------------------------------------"
    )
    print(texts["present_headers"] + Fore.GREEN + f"{present_count}")
    print(texts["absent_headers"] + Fore.RED + f"{absent_count}" + ":\n")


def get_html_structure(url, texts):
    try:
        response = requests.get(url)
        html_content = response.text

        # Encuentra el índice de inicio y fin del contenido del body
        body_start_index = html_content.find("<body")
        body_end_index = html_content.find("</body>") + len("</body>")

        # Extraer las secciones requeridas del HTML
        html_start = html_content[:body_start_index] if body_start_index != -1 else ""
        body_tags = (
            html_content[body_start_index:body_end_index]
            if body_start_index != -1 and body_end_index != -1
            else ""
        )
        html_end = html_content[body_end_index:] if body_end_index != -1 else ""

        # Imprimir el título y luego las secciones del HTML
        print(Fore.LIGHTBLUE_EX + texts["html_tags"] + "\n")
        print(Fore.LIGHTBLACK_EX + html_start + body_tags + html_end)

    except requests.exceptions.RequestException as e:
        print(texts["html_tags_error"] + ": " + str(e))


def load_texts(language_code):
    with open("languages.json", "r", encoding="utf-8") as file:
        languages = json.load(file)
        return languages.get(
            language_code, languages["en"]
        )  # Devuelve inglés por defecto si el código no existe


def main():
    language_code = input("Select language (en/es): ").lower()
    texts = load_texts(language_code)

    title(texts)
    url = input(texts["enter_url"])
    cookie = input(texts["enter_cookie"])
    check_security_headers(url, cookie.strip() or None, texts)
    # Obtener y mostrar la estructura HTML
    get_html_structure(url, texts)

    print("\n" + Fore.LIGHTCYAN_EX + texts["end_check"] + "\n")


if __name__ == "__main__":
    main()
