from flask import Flask
import pyodbc
import json
from flask import request

conn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=10.4.28.183;DATABASE=postgres;UID=postgres;PWD=qwe1234*')

app = Flask(__name__)

def get_daddys_categories(conn):
    cnxn = conn.cursor()
    cnxn.execute('select categoryid, name, banner  from categories c  where parentid isnull and categoryid != 50689')
    categories = cnxn.fetchall()
    cnxn.commit()
    return categories

def get_children_categories(conn, id):
    cnxn = conn.cursor()
    cnxn.execute('select * from categories c where parentid  = {}'.format(id))
    children = cnxn.fetchall()
    cnxn.commit()
    data_children = []
    for i in children:
        __json = {
            'id' : i[0],
            'name' : i[1]
        }
        data_children.append(__json)    
    return data_children



def convert_json(categories):
    data = []
    for i in categories:
        _json = {
            'id' : i[0],
            'name': i[1],
            'banner': i[2] if i[2] else 'no tiene banner',
            'childrens': get_children_categories(conn,i[0])
        }
        print(_json)
        data.append(_json)
    return data

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'hola'
    


@app.route('/user/<username>')
def show_user(username):
    return 'user: %s' % username

@app.route('/products/<int:id>')
def get_products(id):
    return str(id)
       

@app.route('/')
def main():
    get_daddy = get_daddys_categories(conn)
    maria = convert_json(get_daddy)
    return json.dumps({"resultados":maria})

if __name__ == '__main__':
    app.run(debug=True)