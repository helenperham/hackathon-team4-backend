from app import app
from models import db, Staff, Order, Reciept_Item, Menu_Item, Table

print('Seeding database ... 🌱')
# Add your seed data here
with app.app_context():
    server1 = Staff('Keenan', '12345')
    server2 = Staff('Kel', '12345')
    manager = Staff('Bob', '12345', True)
    db.session.add_all([server1, server2, manager])
    db.session.commit()

with app.app_context():
    menu_item1 = Menu_Item('Classic Ramen', '1','entree', '100', 8.00)
    menu_item2 = Menu_Item('Negi-Goma Ramen', '1', 'entree', '50', 12.00)
    menu_item3 = Menu_Item('Miso Ramen', '1', 'entree', '50', 10.00)
    menu_item4 = Menu_Item('Shio Ramen', '1', 'entree', '50', 10.00)
    menu_item5 = Menu_Item('Curry Ramen', '1', 'entree', '50', 12.00)

    menu_item6 = Menu_Item('Pork Bun', '1', 'app', '50', 4.50)
    menu_item7 = Menu_Item('Shrimp Bun', '1', 'app', '50', 4.50)
    menu_item8 = Menu_Item('Gyoza', '1', 'app', '100', 4.50)


    menu_item9 = Menu_Item('Hot Tea', '1', 'bev', '50', 3.00)
    menu_item10 = Menu_Item('Soda', '1', 'bev', '50', 3.00)
    menu_item11 = Menu_Item('Seltzer', '1', 'bev', '50', 3.00)
    menu_item12 = Menu_Item('Sake Cup', '1', 'bev', '50', 14.00)
    menu_item13 = Menu_Item('Sake Bottle', '1', 'bev', '50', 35.00)

    menu_item14 = Menu_Item('Green Tea Ice Cream', '1', 'dess', '50', 3.00)
    menu_item15 = Menu_Item('Red Bean Ice Cream', '1', 'dess', '50', 3.00)
    menu_item16 = Menu_Item('Mochi', '1', 'dess', '50', 3.00)
    menu_item17 = Menu_Item('Sesame Cookie', '1', 'dess', '50', 3.00)
    db.session.add_all(
        [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5, menu_item6, menu_item7, 
         menu_item8, menu_item9, menu_item10,menu_item11, menu_item12, menu_item13, menu_item14,
          menu_item15, menu_item16, menu_item17])
    db.session.commit()

with app.app_context():
    table1 = Table('1', '1', '4', 'in_progress', '2')
    table2 = Table('2', '1', '4', 'in_progress', '2')
    table3 = Table('3', '1', '6', 'in_progress', '3')
    db.session.add_all([table1, table2, table3])
    db.session.commit()

print('Done! 🌳')