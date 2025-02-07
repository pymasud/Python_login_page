from flask import Flask, render_template, request, jsonify
import bcrypt

app = Flask(__name__)

# Hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

# Check a password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

# Simulated database with hashed passwords
users = {
    "admin": {
        "password": hash_password("password123")  # Store hashed password
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and check_password(password, users[username]["password"]):
        return jsonify({"status": "success", "message": "Login successful!"})
    else:
        return jsonify({"status": "error", "message": "Invalid username or password"})

if __name__ == "__main__":
    app.run(debug=True)