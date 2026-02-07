class Customers(db.Model):
    __Tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(100), unique=False, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity = db.Column(db.DateTime, nullable=False)
