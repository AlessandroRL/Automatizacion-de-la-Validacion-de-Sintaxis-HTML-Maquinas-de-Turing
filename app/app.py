import os
import requests
from flask import Flask, request, render_template, redirect, url_for
from waitress import serve

from validation.url_validation import is_valid_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        html = request.form.get("html")

        if url and is_valid_url(url):
            return redirect(url_for("validate_syntax", input_type="url", value=url))
        elif html:
            validation_results = validate_html(html=html)
            if "error" in validation_results:
                return render_template("index.html", error=f"Error en la validación: {validation_results['error']}")

            # Procesar los mensajes para determinar validez
            messages = validation_results.get("messages", [])
            is_valid_html = all(message["type"] == "info" for message in messages)

            formatted_messages = [
                {
                    "type": message.get("type", "N/A").capitalize(),
                    "line": message.get("lastLine", "N/A"),
                    "message": message.get("message", "N/A")
                }
                for message in messages
            ]

            return render_template("result.html", results=formatted_messages, is_valid_html=is_valid_html)
        else:
            return render_template("index.html", error="Debe proporcionar una URL o código HTML válido.")

    return render_template("index.html")



@app.route("/validate-syntax/<input_type>/<path:value>", methods=["GET"])
def validate_syntax(input_type, value):
    validation_results = validate_html(url=value if input_type == "url" else None)

    if "error" in validation_results:
        return render_template("index.html", error=f"Error en la validación: {validation_results['error']}")

    # Procesar los mensajes para determinar validez
    messages = validation_results.get("messages", [])
    is_valid_html = all(message["type"] == "info" for message in messages)

    formatted_messages = [
        {
            "type": message.get("type", "N/A").capitalize(),
            "line": message.get("lastLine", "N/A"),
            "message": message.get("message", "N/A")
        }
        for message in messages
    ]

    return render_template("result.html", results=formatted_messages, is_valid_html=is_valid_html)


@app.route("/validate-syntax-html", methods=["POST"])
def validate_syntax_html():
    html = request.form.get("html")
    validation_results = validate_html(html=html)

    if "error" in validation_results:
        return render_template("index.html", error=f"Error en la validación: {validation_results['error']}")

    # Procesar los mensajes para determinar validez
    messages = validation_results.get("messages", [])
    is_valid_html = all(message["type"] == "info" for message in messages)

    formatted_messages = [
        {
            "type": message.get("type", "N/A").capitalize(),
            "line": message.get("lastLine", "N/A"),
            "message": message.get("message", "N/A")
        }
        for message in messages
    ]

    return render_template("result.html", results=formatted_messages, is_valid_html=is_valid_html)


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
            return {"error": "No input provided"}

        if response.status_code != 200:
            return {"error": f"Error de red: {response.status_code}"}

        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
