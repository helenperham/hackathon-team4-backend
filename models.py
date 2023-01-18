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

    def __init__(self, name, password, manager=False, clocked_in=False):
        self.name = name
        self.clocked_in = clocked_in
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

    def tables(self):
        return Table.query.filter_by(server_id = self.id)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    order_status = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, table_id):
        self.table_id = table_id
        self.total = 0
        self.order_status = True
        
    def to_dict(self):
        return {
            'id': self.id,
            'table_id': self.table_id,
            'total': self.total
        }

    def receipt_items(self):
        items = []
        for item in Receipt_Item.query.filter_by(order_id = self.id):
            items.append(item)
            return items

    def table(self):
        return Table.query.get(self.id)

    def print_receipt(self):
        receipt = []
        for item in self.receipt_items():
            receipt.append({'name':f'{item.name}', 'price':f'{item.price}', 'instructions':f'{item.instructions}'})
        return receipt

class Receipt_Item(db.Model):
    __tablename__ = 'receipt_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(25), nullable=False)
    item_price = db.Column(db.Float, nullable=False)
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


class Menu_Item(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    stock_remaining = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, category, stock_remaining, price):
        self.name = name
        self.category = category
        self.stock_remaining = stock_remaining
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'stock_remaining': self.stock_remaining,
            'price': self.price
        }


class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    server_id = db.Column(db.Integer)
    max_num_guests = db.Column(db.Integer, nullable=False)
    table_status = db.Column(db.Boolean)
    section = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, max_num_guests, section):
        self.name = name
        self.server_id = None
        self.max_num_guests = max_num_guests
        self.table_status = False
        self.section = section

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'server_id': self.server_id,
            'max_num_guests': self.max_num_guests,
            'table_status': self.table_status,
            'section': self.section
        }

    def orders(self):
        return Order.query.filter_by(table_id=self.id)

    def current_orders(self):
        return Order.query.filter_by(table_id=self.id, order_status=True)

    def server(self):
        return Staff.query.get(self.server_id)


class Add_On(db.Model):
    __tablename__ = 'add_ons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    receipt_item_id = db.Column(db.Integer, nullable=False)
    stock_remaining = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, receipt_item_id, stock_remaining, price):
        self.name = name
        self.receipt_item_id = receipt_item_id
        self.stock_remaining = stock_remaining
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'receipt_item_id': self.receipt_item_id,
            'stock_remaining': self.stock_remaining,
            'price': self.price
        }
