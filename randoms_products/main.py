from flask import Flask, json
import pyodbc

conn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=10.4.28.183;DATABASE=postgres;UID=postgres;PWD=developer2020')

app = Flask(__name__)

def random_products(conn):
    cnxn = conn.cursor()
    cnxn.execute('select categoryid, name from categories c where parentid  is null')
    rows = cnxn.fetchall()
    cnxn.commit()
    return rows

 
@app.route('/')
def hello():
    show_data = random_products(conn)
    return str(show_data)
    
    

if __name__ == '__main__':
    app.run()
