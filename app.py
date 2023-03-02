from flask import Flask, render_template, request
from flask import flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '24ba438773ab9e100d2a985fef34b506'

menu_items = [
    {'id': 'id_pizza', 'name': 'name_pizza', 'price' :12.50, 'ingredients': 'mozarella, olives, dough'}, 
    {'id': 'id_soup', 'name': 'name_soup', 'price': 19.50, 'ingredients': 'water, potato'}, 
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