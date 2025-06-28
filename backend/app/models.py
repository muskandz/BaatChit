from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullBLE=False)
    online_status = db.Column(db.DateTime, default=datetime.utcnow)

    sent_message = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    received_message = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class ChatRoom(db.Model):
    __tablename__ = 'ChatRoom'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = ad.Column(db.DateTime, default=datetime.utcnow)

    messages = db.relationship('Message', backref='chatroom', laxy=True)

    def __repr__(self):
        return f"<ChatRoo, {self.name}>"
    
class Message(db.Model):
    __tablename__ = "Message"

    id =db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=True)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('ChatRoom.id'), nullable=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Message {self.id} from {self.sender_id}>"
                          
    