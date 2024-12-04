import requests

def validate_html(html_content):
    url = "https://validator.w3.org/nu/"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    params = {"out": "json"}

    response = requests.post(url, headers=headers, params=params, data=html_content)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al validar HTML: {response.status_code} - {response.text}")

def validate_url(url):
    api_url = "https://validator.w3.org/nu/"
    params = {"doc": url, "out": "json"}

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al validar URL: {response.status_code} - {response.text}")
