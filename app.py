import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

from models import db, Staff, Order, Receipt_Item, Menu_Item, Table

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.get('/test')
def test_route():
    table = Table.query.first()
    print(table.server())
    return jsonify({})

@app.get('/staff')
def all_staff():
    staff = Staff.query.all()
    return jsonify([s.to_dict() for s in staff]), 201

@app.get('/servers')
def all_servers():
    servers = Staff.query.filter_by(manager=False)
    return jsonify([s.to_dict() for s in servers]), 201

#this is the route for the staff page
@app.get('/staff/<int:id>/tables')
def server(id):
    staff = Staff.query.get(id)
    if staff:
        tables = staff.tables()
        print(tables)
        return jsonify({'tables': [t.to_dict() for t in tables] }), 201
    else:
        return {'error': 'Staff not found'}, 404

# this is going to be the route for the managerpage. 
@app.get('/staff/<int:id>')
def show(id):
    staff = Staff.query.get(id)
    if staff:
        return jsonify(staff.to_dict()), 201
    else:
        return {'error': 'Staff not found'}, 404

@app.get('/managers')
def all_managers():
    managers = Staff.query.filter_by(manager=True)
    return jsonify([m.to_dict() for m in managers]), 201

@app.patch('/assign_section/<int:id>')
def assign_section(id):
    data=request.json
    server = Staff.query.get(id)
    sections = ['1', '2', '3', '4']
    if data['section'] in sections:
        server.section = data['section']
        table = Table.query.filter_by(section= data['section'], table_status = True)
        if table.count() > 0:
            table[0].server_id = server.id
        db.session.commit()
        return jsonify(server.to_dict()), 202
    else:
        return {'error': 'section not found'}, 404

@app.post('/receipt_items')
def create_item():
    data = request.json
    item = Receipt_Item(data['order_id'], data['item_name'], data['item_price'], data['instructions'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 202

@app.delete('/receipt_items/<int:id>')
def delete_item(id):
    item = Receipt_Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify(item), 200

@app.post('/orders')
def create_order():
    data = request.json
    order = Order(data['table'])
    db.session.add(order)
    db.session.commit()
    for item in data['items']:
        rec_item = Receipt_Item(order.id, item['name'], item['price'])
        db.session.add(rec_item)
        db.session.commit()
    
    return jsonify([i.to_dict() for i in order.receipt_items()]), 202

@app.patch('/order_total/<int:id>')
def order_total(id):
    data = request.json
    order = Order.query.get(id)
    order.total = data['total']
    order.order_status = False
    db.session.commit()
    return jsonify({'order':order.to_dict(), 'items':order.print_receipt(), 'server': order.table().server().to_dict()}), 202

@app.get('/table/<int:id>/currentorder')
def order_in_progress(id):
    table = Table.query.get(id)
    current_orders = Order.query.filter_by(table_id=table.id).limit(1) 
    if current_orders.count() > 0: 
        print([order.to_dict() for order in current_orders])
        items = current_orders[0].receipt_items()
        print([item.to_dict() for item in items])
        return jsonify([item.to_dict() for item in items]), 202
    else: 
        return jsonify([])

@app.get('/order/<int:id>/reciept_items')
def receipt_items(id):
    order = Order.query.get(id)
    items = order.reciept_items()
    return jsonify([i.to_dict() for i in items]), 202

@app.patch('/staff/<int:id>/clock_in')
def clock_in(id):
    staff = Staff.query.get(id)
    if staff:
        staff.clocked_in = True
        db.session.commit()
        return jsonify(staff.to_dict()), 202
    else:
        return {'error': 'Staff not found'}, 404

@app.patch('/staff/<int:id>/clock_out')
def clock_out(id):
    staff = Staff.query.get(id)
    if staff:
        staff.clocked_in = False
        staff.section = None
        db.session.commit()
        return jsonify(staff.to_dict()), 202
    else:
        return {'error': 'Staff not found'}, 404

@app.patch('/table/<int:id>/activate')
def activate_table(id):
    table = Table.query.get(id)
    table.table_status = True
    staff_list = Staff.query.filter_by(section=table.section).order_by(len(Staff.tables()).desc())
    if len(staff_list) > 0:
        staff = staff_list[0]
        table.server_id = staff.id
        db.session.commit()
        return jsonify({'table':table.to_dict(), 'message':f'{staff.name} was assigned to this table'}), 202
    else:
        return {'error': 'No servers assigned to that section'}, 404

@app.patch('/table/<int:id>/deactivate')
def deactivate_table(id):
    table = Table.query.get(id)
    table.table_status = False
    table.server.id = None
    db.session.commit()
    return jsonify(table.to_dict()), 202

@app.get('/menu_items')
def index():
    items = Menu_Item.query.all()
    return jsonify([item.to_dict() for item in items])

@app.get('/menu_items/<int:id>')
def show_menu_item(id):
    item = Menu_Item.query.get(id)
    return jsonify(item.to_dict())

@app.get('/menu_items/Beverage')
def Beverage():
    Beverage = Menu_Item.query.filter_by(category = 'Beverage')
    return jsonify([bev.to_dict() for bev in Beverage])

@app.get('/menu_items/Appetizer')
def Appetizer():
    Appetizer = Menu_Item.query.filter_by(category = 'Appetizer')
    return jsonify([app.to_dict() for app in Appetizer])

@app.get('/menu_items/Entree')
def Entree():
    Entree = Menu_Item.query.filter_by(category = 'Entree')
    return jsonify([entree.to_dict() for entree in Entree])

@app.get('/menu_items/Dessert')
def Dessert():
    Dessert = Menu_Item.query.filter_by(category = 'Dessert')
    return jsonify([dess.to_dict() for dess in Dessert])

@app.get('/categories')
def categories():
    categories = set()
    for item in Menu_Item.query.all():
        categories.add(item.category)
    new_list = list(categories)
    return jsonify({'categories': new_list})

@app.post('/staff')
def create_staff():
    data=request.json
    staff = Staff(data['name'], data['password'], data['manager'])
    db.session.add(staff)
    db.session.commit()
    return jsonify(staff.to_dict())

@app.get('/clocked_in_staff')
def get_clocked_in_staff():
    staff = Staff.query.filter_by(clocked_in = True, manager = False)
    return jsonify([s.to_dict() for s in staff]), 202 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))