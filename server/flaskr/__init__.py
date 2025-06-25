import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DB=os.path.join(app.instance_path,"flaskr.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile("config.py",silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from blueprints import linux
    app.register_blueprint(linux.bp)

    return app