from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configuration de la base de données SQLite (remplacez 'sqlite:///test.db' par le chemin de votre base de données)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def hello_world():
    # Ajouter un message à la base de données pour la démonstration
    with app.app_context():
        new_message = Message(content='This is a message from the database!')
        db.session.add(new_message)
        db.session.commit()

        # Récupérer tous les messages de la base de données
        messages = Message.query.all()
        message_content = [message.content for message in messages]

    return jsonify(message_content)

if __name__ == '__main__':
    # Créer la table dans la base de données
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
