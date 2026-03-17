from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/games', methods=['GET'])
def get_games():
    return jsonify({'games': []})

@app.route('/api/games', methods=['POST'])
def create_game():
    data = request.json
    # Logic to create a game goes here
    return jsonify({'game': data}), 201

if __name__ == '__main__':
    app.run(debug=True)