from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Получаем переменные из окружения
NAME = os.getenv("APP_NAME", "TEST-APP")
SECRET_KEY = os.getenv("SECRET_KEY", "not-set")
SECRET_MULTI = os.getenv("SECRET_MULTI", "not-set")
CONFIG_KEY = os.getenv("CONFIG_KEY", "not-set")
CONFIG_MULTI = os.getenv("CONFIG_MULTI", "not-set")

# HTML-шаблон с отображением всех переменных
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello App</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .section { margin: 20px 0; padding: 15px; border: 1px solid #ccc; border-radius: 5px; }
        .key-value { margin: 5px 0; font-family: monospace; }
    </style>
</head>
<body>
    <h1>{{ greeting }}</h1>

    <div class="section">
        <h2> Environment Variables</h2>
        <div class="key-value"><strong>APP_NAME:</strong> {{ name }}</div>
        <div class="key-value"><strong>SECRET_KEY:</strong> {{ secret_key }}</div>
        <div class="key-value"><strong>SECRET_MULTI:</strong><br>{{ secret_multi }}</div>
        <div class="key-value"><strong>CONFIG_KEY:</strong> {{ config_key }}</div>
        <div class="key-value"><strong>CONFIG_MULTI:</strong><br>{{ config_multi }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def hello():
    return render_template_string(
        HTML_TEMPLATE,
        greeting=f"{NAME}",
        name=NAME,
        secret_key=SECRET_KEY,
        secret_multi=SECRET_MULTI,
        config_key=CONFIG_KEY,
        config_multi=CONFIG_MULTI
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
