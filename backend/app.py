from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a flask instance
app = Flask(__name__)

# Add the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin123@localhost:5432/bizza'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bizza.db'


# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model definition
class User(db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    roles = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    is_superuser = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow())

    def __repr__(self):
        return '<User %r>' % self.username
    

# Speaker Model Definition
class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    bio = db.Column(db.String(240))
    photo = db.Column(db.String(120))
    contact_info = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('User',backref=db.backref('speaker', uselist=False))

    def __repr__(self):
        return f"Speaker('{self.name}', '{self.bio}', '{self.photo}', '{self.contact_info}')"
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
