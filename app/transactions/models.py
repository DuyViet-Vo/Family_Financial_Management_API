from datetime import datetime

from config import db


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    transaction_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    update_at = db.Column(db.DateTime, nullable=False)
    group = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
