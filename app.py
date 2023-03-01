from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)

@app.route('/menu')
def menu():
    #item_id = 'id_pizza'
    #item_name = 'name_pizza'
    items = [{'id': 'id_pizza', 'name': 'name_pizza', 'price' :12.50}, 
            {'id': 'id_soup', 'name': 'name_soup', 'price': 19.50},
            {'id': 'id_ravioli', 'name': 'name_ravioli', 'price': 11.11},
    ]
    return render_template('menu.html', items=items)