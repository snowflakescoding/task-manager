from flask import Flask, render_template, request, jsonify, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# --- IN-MEMORY STORAGE (Replaces SQLite for Vercel Demo) ---
# Data will reset when the server restarts!
users_db = {}  # Format: {'username': {'id': 1, 'password': 'hashed_pw'}}
tasks_db = []  # Format: {'id': 1, 'user_id': 1, 'content': 'Do laundry'}
user_id_counter = 1
task_id_counter = 1

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global user_id_counter # Declared at top
    
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    
    if username in users_db:
        return jsonify({"error": "Username already exists"}), 400
    
    users_db[username] = {
        'id': user_id_counter,
        'password': password
    }
    user_id_counter += 1
    return jsonify({"message": "User created!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    
    user = users_db.get(username)
    
    if user and user['password'] == password:
        session['user_id'] = user['id']
        return jsonify({"message": "Logged in successfully"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/tasks', methods=['GET', 'POST', 'DELETE'])
def tasks():
    # FIX: These must be at the very top of the function
    global tasks_db 
    global task_id_counter

    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    user_id = session['user_id']

    if request.method == 'GET':
        user_tasks = [t for t in tasks_db if t['user_id'] == user_id]
        return jsonify(user_tasks)

    if request.method == 'POST':
        content = request.json.get('content')
        tasks_db.append({
            'id': task_id_counter,
            'user_id': user_id,
            'content': content
        })
        task_id_counter += 1
        return jsonify({"message": "Task added"})
        
    if request.method == 'DELETE':
        task_id = request.json.get('id')
        # Filter out the task with the matching ID and User ID
        tasks_db = [t for t in tasks_db if not (t['id'] == task_id and t['user_id'] == user_id)]
        return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)