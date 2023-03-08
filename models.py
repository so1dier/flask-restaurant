from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.image_file}', '{self.password}')"

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"MenuItem('{self.id}', '{self.name}', '{self.price}', '{self.description}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Order('{self.id}', '{self.user_id}', '{self.date_time}')"

class OrderWithMenuItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)

    def __repr__(self):
        return f"OrderWithMenuItem('{self.id}', '{self.order_id}', '{self.menu_item_id}')"
    