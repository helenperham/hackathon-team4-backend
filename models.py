from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from random import randint

db = SQLAlchemy()
migrate = Migrate(db)

class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    clocked_in = db.Column(db.Boolean, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    manager = db.Column(db.Boolean, nullable=False)
    empl_id = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, password, manager=False):
        self.name = name
        self.password = password
        self.empl_id = randint(10000, 99999)
        self.section = None
        self.manager = manager
        self.clocked_in = False



        

    def __repr__(self):
        return '<Staff %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'manager': self.manager,
            'clocked_in': self.clocked_in,
            'section': self.section,
            'empl_id': self.empl_id
        }

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, table_id):
        self.table_id = table_id
        self.total = 0
        
    def to_dict(self):
        return {
            'id': self.id,
            'table_id': self.table_id,
            'total': self.total
        }

    def receipt_items(self):
        items = []
        for item in Reciept_Item.query.all():
            items.append(item)
            return items

    # def table(self):
    #     return Table.query.get(self.id)

class Reciept_Item(db.Model):
    __tablename__ = 'reciept_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(25), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, order_id, item_name, item_price, instructions=None):
        self.order_id = order_id
        self.item_name = item_name
        self.item_price = item_price
        self.instructions = instructions
        
    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'item_name': self.item_name,
            'item_price': self.item_price,
            'instructions': self.instructions
        }

    def order(self):
        return Order.query.get(self.order_id)