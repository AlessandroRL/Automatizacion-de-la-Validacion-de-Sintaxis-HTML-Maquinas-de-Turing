import requests

def validate_html(url=None, html=None):

    api_url = "https://validator.w3.org/nu/"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    params = {"out": "json"}

    try:
        if url:
            response = requests.get(api_url, headers=headers, params={"doc": url, **params})
        elif html:
            response = requests.post(api_url, headers=headers, params=params, data=html.encode("utf-8"))
        else:
            return {"error": "No se proporcionó entrada para validar"}

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}: {response.reason}"}
    except Exception as e:
        return {"error": str(e)}
