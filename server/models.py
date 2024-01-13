from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, default=datetime.utcnow().isoformat())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow().isoformat(), onupdate=datetime.utcnow())

    def __repr__(self):
        return f"<Message {self.id}>"

