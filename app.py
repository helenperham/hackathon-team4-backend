import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, Staff, Order, Reciept_Item

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

@app.post('/reciept_items')
def create_item():
    data = request.form
    item = Reciept_Item(data['order_id'], data['item_name'], data['item_price'], data['instructions'])
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

@app.patch('/order_total/<int:id')
def order_total(id):
    data = request.form
    order = Order.query.get(id)
    order.total = data['total']
    db.session.add(order)
    db.session.commit()
    return jsonify({'order':order.to_dict(), 'items':[i.to_dict for i in order.reciept_items]}), 202




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))