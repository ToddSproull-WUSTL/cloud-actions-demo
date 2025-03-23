# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
<<<<<<< HEAD
        "message": "Hello Cloud Computing",
=======
        "message": "Hello Cloud Different Message!",
>>>>>>> 1ca0a1a2edb7dabb581f299e8d9b198d08af50c6
        "status": "success"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
