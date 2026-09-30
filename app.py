from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    text = data.get('text', '')
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    return jsonify({'status': 'ok', 'saved': text})


@app.route('/read', methods=['GET'])
def read():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = ''
    return jsonify({'content': content})


if __name__ == '__main__':
    app.run(debug=True, port=5000)