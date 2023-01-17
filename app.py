import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, Staff, Order, Receipt_Item, Table

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.get('/staff')
def all_staff():
    staff = Staff.query.all()
    return jsonify([s.to_dict() for s in staff]), 201

@app.get('/servers')
def all_servers():
    servers = Staff.query.filter_by(manager=False)
    return jsonify([s.to_dict() for s in servers]), 201

@app.get('/managers')
def all_managers():
    managers = Staff.query.filter_by(manager=True)
    return jsonify([m.to_dict() for m in managers]), 201

@app.patch('/assign_section/<int:id>')
def assign_section(id):
    data=request.form
    server = Staff.query.get(id)
    server.section = data['section']
    return jsonify(server.to_dict()), 202

@app.post('/receipt_items')
def create_item():
    data = request.form
    item = Receipt_Item(data['order_id'], data['item_name'], data['item_price'], data['instructions'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 202

@app.post('/orders')
def create_order():
    data = request.form
    order = Order(data['table_id'])
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 202

@app.patch('/order_total/<int:id>')
def order_total(id):
    data = request.form
    order = Order.query.get(id)
    order.total = data['total']
    order.order_status = False
    db.session.add(order)
    db.session.commit()
    return jsonify({'order':order.to_dict(), 'items':[i.to_dict() for i in order.receipt_items]}), 202

@app.get('/table/<int:id>/currentorder')
def order_in_progress(id):
    table = Table.query.get(id)
    current_orders = table.current_orders()
    return jsonify(current_orders[0].to_dict()), 202

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
        db.session.add(staff)
        db.session.commit()
        return jsonify(staff.to_dict()), 202
    else:
        return {'error': 'Staff not found'}, 404

@app.patch('/table/<int:id>/activate')
def activate_table(id):
    table = Table.query.get(id)
    table.table_status = True
    staff_list = Staff.query.filter_by(section=table.section).order_by(len(Staff.tables()).desc)
    if len(staff_list) > 0:
        staff = staff_list[0]
        table.server_id = staff.id
        db.session.add(table)
        db.commit()
        return {'table':jsonify(table.to_dict), 'message':f'{staff.name} was assigned to this table'}, 202
    else:
        return {'error': 'No servers assigned to that section'}, 404





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))