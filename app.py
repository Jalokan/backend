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

if __name__ == '__main__':
    app.run(debug=True, port=5000)