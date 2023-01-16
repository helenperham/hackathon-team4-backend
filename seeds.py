from app import app
from models import db, User

print('Seeding database ... 🌱')
# Add your seed data here
menu_item1 = Menu_Item(name: 'Classic Ramen', order_id: '1', category: 'entree', stock_remaining: 100, price: 8.00)
menu_item2 = Menu_Item(name: 'Negi-Goma Ramen', order_id: '1', category: 'entree', stock_remaining: 50, price: 12.00)
menu_item3 = Menu_Item(name: 'Miso Ramen', order_id: '1', category: 'entree', stock_remaining: 50, price: 10.00)
menu_item4 = Menu_Item(name: 'Shio Ramen', order_id: '1', category: 'entree', stock_remaining: 50, price: 10.00)
menu_item5 = Menu_Item(name: 'Curry Ramen', order_id: '1', category: 'entree', stock_remaining: 50, price: 12.00)

menu_item6 = Menu_Item(name: 'Pork Bun', order_id: '1', category: 'app', stock_remaining: 50, price: 4.50)
menu_item7 = Menu_Item(name: 'Shrimp Bun', order_id: '1', category: 'app', stock_remaining: 50, price: 4.50)
menu_item8 = Menu_Item(name: 'Gyoza', order_id: '1', category: 'app', stock_remaining: 100, price: 4.50)


menu_item9 = Menu_Item(name: 'Hot Tea', order_id: '1', category: 'bev', stock_remaining: 50, price: 3.00)
menu_item10 = Menu_Item(name: 'Soda', order_id: '1', category: 'bev', stock_remaining: 50, price: 3.00)
menu_item11 = Menu_Item(name: 'Seltzer', order_id: '1', category: 'bev', stock_remaining: 50, price: 3.00)
menu_item12 = Menu_Item(name: 'Sake Cup', order_id: '1', category: 'bev', stock_remaining: 50, price: 14.00)
menu_item13 = Menu_Item(name: 'Sake Bottle', order_id: '1', category: 'bev', stock_remaining: 50, price: 35.00)

menu_item14 = Menu_Item(name: 'Green Tea Ice Cream', order_id: '1', category: 'dess', stock_remaining: 50, price: 3.00)
menu_item15 = Menu_Item(name: 'Red Bean Ice Cream', order_id: '1', category: 'dess', stock_remaining: 50, price: 3.00)
menu_item16 = Menu_Item(name: 'Mochi', order_id: '1', category: 'dess', stock_remaining: 50, price: 3.00)
menu_item17 = Menu_Item(name: 'Sesame Cookie', order_id: '1', category: 'dess', stock_remaining: 50, price: 3.00)

new branch!
print('Done! 🌳')