from application import db
from datetime import datetime

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
