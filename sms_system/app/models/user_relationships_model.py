from ..database import db

class User_relationship(db.Model):
    __tablename__ = 'user_relationships'

    id = db.Column(db.Integer, primary_key=True)
    user_id1 = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_id2 = db.Column(db.Integer, db.ForeignKey('users.id'))
    relationship_type = db.Column(db.Enum('SENDER','RECEIVER'))
