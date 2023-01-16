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
    return jsonify([s.to_dict() for s in staff]), 202

@app.get('/servers')
def all_servers():
    servers = Staff.query.filter_by(manager=False)
    return jsonify([s.to_dict() for s in servers])

@app.get('/managers')
def all_managers():
    managers = Staff.query.filter_by(manager=True)
    return jsonify([m.to_dict() for m in managers])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))