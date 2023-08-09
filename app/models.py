from . import db

class tbl_zksession(db.Model):
    __tablename__ = 'tbl_zksession'
    id = db.Column(db.Integer, primary_key=True)
    accept = db.Column(db.String(50))
    content_type = db.Column(db.String(50))
    cookie = db.Column(db.String(200))
    created = db.Column(db.DateTime)