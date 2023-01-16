from app import app
from models import db, Staff, Order, Reciept_Item

print('Seeding database ... 🌱')
# Add your seed data here
with app.app_context():
    server1 = Staff('Keenan', '12345')
    server2 = Staff('Kel', '12345')
    manager = Staff('Bob', '12345', True)
    db.session.add_all([server1, server2, manager])
    db.session.commit()
print('Done! 🌳')