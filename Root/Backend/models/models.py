from app import db  
from sqlalchemy.sql import func

association_table = db.Table('association', db.Model.metadata,
    db.Column('parent_id', db.Integer, db.ForeignKey('Parent.id')),
    db.Column('child_id', db.Integer, db.ForeignKey('Child.id'))
)

class Parent(db.Model):
    __tablename__ = 'Parent'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(254))
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, onupdate = func.now())

    children = db.relationship('Child', 
                               secondary = association_table, 
                               lazy = 'dynamic',
                               backref = db.backref('parents', lazy = 'dynamic')
    )   
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }    
    
class Child(db.Model):
    __tablename__ = 'Child'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(254))
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, onupdate = func.now())
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
db.create_all()