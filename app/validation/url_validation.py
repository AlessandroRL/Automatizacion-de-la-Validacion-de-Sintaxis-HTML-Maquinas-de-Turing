import requests

def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get("Content-Type", "")
        return "text/html" in content_type
    except Exception:
        return False




