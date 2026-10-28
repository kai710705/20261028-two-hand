from __future__ import annotations

import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # 本機以 HTTPS 啟動，讓同網段手機存取時也能申請攝影機權限。
    # Render 使用 Gunicorn 與平台代理的 TLS，因此不會執行這個區塊。
    use_https = os.getenv("LOCAL_HTTPS", "true").lower() == "true"
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=False,
        ssl_context="adhoc" if use_https else None,
    )
