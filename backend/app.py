from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Create a flask instance
app = Flask(__name__)

# Add the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin123@localhost:5432/bizza'

# Initialize the database
db = SQLAlchemy(app)

