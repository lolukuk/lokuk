from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

class User:
    def __init__(self, id, username, balance):
        self.id = id
        self.username = username
        self.balance = balance
    
    @staticmethod
    def create_table():
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, username TEXT, balance INTEGER)''')
        conn.commit()
        conn.close()
    
    @staticmethod
    def add_user(username, balance):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''INSERT INTO users (username, balance) VALUES (?, ?)''', (username, balance))
        conn.commit()
        conn.close()
    
    @staticmethod
    def update_balance(user_id, new_balance):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''UPDATE users SET balance = ? WHERE id = ?''', (new_balance, user_id))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_user_by_id(user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            return User(*user_data)
        return None

def fetch_weather(city):
    # Here you can replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if 'main' in data:
        return data['main']['temp']
    return None

@app.route('/update_balance', methods=['POST'])
def update_balance():
    data = request.json
    user_id = data.get('userId')
    city = data.get('city')
    user = User.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    temperature = fetch_weather(city)
    if temperature is None:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    new_balance = user.balance + temperature
    if new_balance < 0:
        return jsonify({'error': 'Insufficient funds'}), 400
    User.update_balance(user_id, new_balance)
    return jsonify({'message': 'Balance updated successfully', 'newBalance': new_balance})

if __name__ == '__main__':
    User.create_table()
    # Adding 5 users with random balances
    User.add_user('User1', 5000)
    User.add_user('User2', 7000)
    User.add_user('User3', 10000)
    User.add_user('User4', 12000)
    User.add_user('User5', 15000)
    app.run(debug=True)
