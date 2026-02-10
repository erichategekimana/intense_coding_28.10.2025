from ..database import db

class Transaction_categories(db.Model):
    __tablename__ = 'transaction_categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)
    category_code = db.Column(db.String(50), nullable=False)
    category_fee = db.Column(db.Integer(1), nullable=False)
