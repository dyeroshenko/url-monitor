from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp() -> 'app':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.sqlite3'
    db.init_app(app)
    

    from app import home_blueprint, home_post_blueprint, dashboard_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(home_post_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app


if __name__ == '__main__':
    createApp().run(host='0.0.0.0', debug=False)