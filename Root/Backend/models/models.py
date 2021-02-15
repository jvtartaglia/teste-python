from app import db
from datetime import datetime

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(254))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    children = db.Table('children',
                           db.Column('child_id', db.Integer,
                                     db.ForeignKey('child.id')),
                           db.Column('parent_id', db.Integer, db.ForeignKey(
                                     'parent.id'))
                           )

    children = db.relationship('Child', secondary=children,
                                  lazy='dynamic',
                                  backref=db.backref('parents', lazy='dynamic'))
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }    
    
class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(254))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
db.create_all()