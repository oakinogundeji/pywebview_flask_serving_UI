from flask import (
    Flask,
    send_from_directory,
    render_template,
)
from flask_cors import CORS

chat_history = {}


def startUp():
    print("Starting backend initialization...")


def create_app():
    static_dir = "ui/assets"
    app = Flask(__name__, static_folder=static_dir)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    CORS(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/<path:path>")
    def static_file(path):
        return send_from_directory(static_dir, path)

    return app


if __name__ == "__main__":
    startUp()
    app = create_app()
    app.run(host="localhost", port=8080)
