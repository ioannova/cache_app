# app.register_blueprint(api, url_prefix='/api')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.settings import Development

db = SQLAlchemy()

# logger = LocalProxy(lambda: current_app.logger)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    print('\n>>>>>>>>>> Loaging CacheApp...')
    print('[create_app] register config: {}'.format(config.ENV))
    app.config.from_object(config)
    print('[register_extension] SQLAlchemy')
    db.init_app(app)
    print('[create_app] configure_database')
    # configure_database(app)
    print('[time] %s\n>>>>>>>>>> CacheApp Online!!!\n' % datetime.now().astimezone())
    return app

app = create_app(Development)

from app import views
