import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('users.db')
    return db

class UserDataBase:
    def __init__(self, service_name):
        self.service_name = service_name
        self.cursor = get_db().cursor()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.service_name}_users
                            (id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone_number TEXT NOT NULL)''')
        get_db().commit()

    def insert_user(self, name, phone_number):
        self.cursor.execute(f"INSERT INTO {self.service_name}_users (name, phone_number) VALUES (?, ?)", (name, phone_number))
        get_db().commit()

    def get_all_users(self):
        self.cursor.execute(f"SELECT * FROM {self.service_name}_users")
        rows = self.cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'phone_number': row[2]} for row in rows]

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/add-user/<string:service_name>', methods=['POST'])
def add_user(service_name):
    data = request.get_json()
    name = data['Name']
    phone_number = data['Phone Number']
    db = UserDataBase(service_name)
    db.insert_user(name, phone_number)
    return jsonify({'message': 'User added successfully'})

@app.route('/get-users/<string:service_name>', methods=['GET'])
def get_users(service_name):
    db = UserDataBase(service_name)
    users = db.get_all_users()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
