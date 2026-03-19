from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Initial Game State (This resets when you restart the server)
# Later, we can save this to a database!
game_state = {
    "player_name": "Farmer Eron",
    "money": 100,
    "inventory": {"seeds": 5, "crops": 0},
    "farm_tiles": [
        {"id": 1, "status": "empty", "crop": None},
        {"id": 2, "status": "planted", "crop": "Corn"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

# API to get the current status of the farm
@app.route('/api/game-state', methods=['GET'])
def get_status():
    return jsonify(game_state)

# API to handle "Planting" a seed
@app.route('/api/plant', methods=['POST'])
def plant_crop():
    data = request.json
    tile_id = data.get('tile_id')
    
    # Logic: Check if player has seeds
    if game_state["inventory"]["seeds"] > 0:
        game_state["inventory"]["seeds"] -= 1
        # Find the tile and update it
        for tile in game_state["farm_tiles"]:
            if tile["id"] == tile_id:
                tile["status"] = "planted"
                tile["crop"] = "Corn"
        return jsonify({"message": "Planted successfully!", "new_state": game_state}), 200
    
    return jsonify({"error": "No seeds left!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
