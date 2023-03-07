from datetime import datetime
from flask import Flask, render_template, request
from flask import flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SECRET_KEY'] = '24ba438773ab9e100d2a985fef34b506'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'

db = SQLAlchemy(app)

app.app_context().push()

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
    

menu_items = [
   
   
    {'id': 'id_ravioli', 'name': 'name_ravioli', 'price': 11.11, 'ingredients': 'ravioli, bread'},
]

@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('menu'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash(f'Login successful for {form.email.data}', 'success')
            return redirect(url_for('menu'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)