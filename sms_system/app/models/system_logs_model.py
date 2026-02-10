from ..database import db

class System_logs(db.Model):
    __tablename__ = 'system_logs'

    id = db.Column(db.Integer, primary_key=True)
    log_time = db.Column(db.DateTime, default=datetime.utcnow)
    log_type = db.Column(db.Enum('INFO','WARNING','ERROR','DEBUG'))
    log_source = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
