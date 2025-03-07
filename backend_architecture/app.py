from flask import Flask
from database.db import db
from routes.routes import user_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)


