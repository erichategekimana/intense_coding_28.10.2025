class Sms_raw_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    data = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False)
