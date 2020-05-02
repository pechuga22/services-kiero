from flask import Flask
import pyodbc
import json
from flask import request

conn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=172.17.0.3;DATABASE=postgres;UID=postgres;PWD=developer2020')

app = Flask(__name__)

@app.route('/get_categories')
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
     

@app.route('/')
def main():
    get_daddy = get_daddys_categories(conn)
    maria = convert_json(get_daddy)
    return json.dumps({"resultados":maria})

if __name__ == '__main__':
    app.run(debug=True)