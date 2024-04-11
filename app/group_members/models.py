from datetime import datetime

from config import db


class GroupMember(db.Model):
    __tablename__ = "groupmembers"
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    group = db.Column(db.Integer, db.ForeignKey("groups.id"), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
