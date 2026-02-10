from ..database import db

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.column(db.Integer, db.foreignKey('transaction_categories.id'))
    amount = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    fee_amount = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    balance_after = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
