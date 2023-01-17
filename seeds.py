from app import app
from models import db, Staff, Order, Receipt_Item, Menu_Item, Table

print('Seeding database ... 🌱')
# Add your seed data here
# with app.app_context():
#     server1 = Staff('Keenan', '12345')
#     server2 = Staff('Kel', '12345')
#     manager = Staff('Bob', '12345', True)
#     db.session.add_all([server1, server2, manager])
#     db.session.commit()

# with app.app_context():
#     menu_item1 = Menu_Item('Classic Ramen','entree', '100', 8.00)
#     menu_item2 = Menu_Item('Negi-Goma Ramen', 'entree', '50', 12.00)
#     menu_item3 = Menu_Item('Miso Ramen', 'entree', '50', 10.00)
#     menu_item4 = Menu_Item('Shio Ramen', 'entree', '50', 10.00)
#     menu_item5 = Menu_Item('Curry Ramen', 'entree', '50', 12.00)
#     menu_item6 = Menu_Item('Vegan Ramen', 'entree', '50', 12.00)

#     menu_item7 = Menu_Item('Chicken Wings','app', '50', 4.50)
#     menu_item8 = Menu_Item('Pork Bun','app', '50', 4.50)
#     menu_item9 = Menu_Item('Shrimp Bun','app', '50', 4.50)
#     menu_item10 = Menu_Item('Gyoza','app', '100', 6.50)
#     menu_item11 = Menu_Item('Edamame','app', '100', 5.50)
#     menu_item12 = Menu_Item('Seaweed Salad','app', '50', 4.50)


#     menu_item13 = Menu_Item('House Green Hot Tea', 'bev', '50', 3.00)
#     menu_item14 = Menu_Item('Herbal Hot Tea', 'bev', '50', 3.00)
#     menu_item15 = Menu_Item('Soda', 'bev', '50', 3.00)
#     menu_item16 = Menu_Item('Seltzer', 'bev', '50', 3.00)
#     menu_item17 = Menu_Item('Sake Glass', 'bev', '50', 14.00)
#     menu_item18 = Menu_Item('1.8L Sake Bottle', 'bev', '25', 150.00)
#     menu_item19 = Menu_Item('House Sake Flight', 'bev', '25', 35.00)

#     menu_item20 = Menu_Item('Green Tea Ice Cream', 'dess', '50', 3.00)
#     menu_item21 = Menu_Item('Red Bean Ice Cream', 'dess', '50', 3.00)
#     menu_item22 = Menu_Item('Mochi', 'dess', '50', 3.00)
#     menu_item23 = Menu_Item('Sesame Cookie', 'dess', '50', 3.00)
#     menu_item24 = Menu_Item('Cheesecake', 'dess', '25', 3.00)
#     db.session.add_all(
#         [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5, menu_item6, menu_item7, 
#          menu_item8, menu_item9, menu_item10,menu_item11, menu_item12, menu_item13, menu_item14,
#           menu_item15, menu_item16, menu_item17, menu_item18, menu_item19, menu_item20, menu_item21, menu_item22, menu_item23, menu_item24])
#     db.session.commit()

# with app.app_context():
#     table1 = Table('1', none, '4', False, '1')
#     table2 = Table('2', none, '4', False, '1')
#     table3 = Table('3', none, '2', False, '2')
#     table4 = Table('4', none, '2', False, '2')
#     table5 = Table('5', none, '4', False, '3')
#     table6 = Table('6', none, '4', False, '3')
#     table7 = Table('8', none, '4', False, '4')
#     db.session.add_all([table1, table2, table3, table4, table5, table6, table7])
#     db.session.commit()

# with app.app_context():
#     add_on1 = Add_On('Soft Boiled Egg', none, '50', 2.50) 
#     add_on2 = Add_On('Bean Sprouts', none, '50', 2.50)
#     add_on3 = Add_On('Fried Tofu, none, '50', 2.50)
#     add_on4 = Add_On('Glazed Chicken', none, '50', 2.50)
#     add_on5 = Add_On('Kimchi', none, '100', 2.50)
#     add_on6 = Add_On('Nori', none, '100', 2.50)
#     add_on7 = Add_On('Extra Noodles', none, '100', 2.50)
#     db.session.add_all([add_on1, add_on2, add_on3, add_on4, add_on5, add_on6, add_on7])
#     db.session.commit()

print('Done! 🌳')