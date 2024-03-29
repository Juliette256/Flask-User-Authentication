from sqlalchemy import ForeignKey
from database import db

class itemModel(db.Model):

    __tablename__= "items"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30))
    price=db.Column(db.Float(precision=2))

    store_id=db.Column(db.Integer, db.ForeignKey('stores.id'))
    store=db.relationship('storeModel')

    def __init__(self, name, price, store_id):
        self.name=name
        self.price=price 
        self.store_id=store_id

    def json(self):
        return{'name': self.name, 'price': self.price}

    @classmethod   
    def find_by_name(cls,name):
      return cls.query.filter_by(name=name).first()
    
   #this method inserts and updates too
    def save_to_database(self):
       db.session.add(self)
       db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit() 