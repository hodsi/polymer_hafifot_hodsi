from uuid import uuid4

from flask import Flask
from backend.blueprints import frontend, products

app = Flask(__name__, static_url_path="", static_folder="frontend")


def main():
    blueprints = [frontend.blueprint, products.blueprint]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.config.update(SEND_FILE_MAX_AGE_DEFAULT=0)
    app.secret_key = str(uuid4())


def local_run():
    app.run(debug=True, host="0.0.0.0", port=2222, threaded=True, use_reloader=True)


# always run main
main()

# if ran through the main file - run locally
if __name__ == '__main__':
    local_run()
