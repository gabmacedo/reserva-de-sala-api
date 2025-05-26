from flask import Flask
from database import db
from routes.reserva_route import routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # <- carrega as configs, incluindo a URI do banco

@routes.route("/")
def index():
    return {"mensagem": "API reserva de sala rodando com sucesso!"}

db.init_app(app)  # <- só inicializa depois que a config foi setada

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
