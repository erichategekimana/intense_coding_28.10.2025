from app.database import db


class SMS_raw_data(db.Model):
    __tablename__ = 'sms_raw_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    data = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False)
