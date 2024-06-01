from flask import Flask, render_template, request, jsonify
from packages.game_logic import Snake

app = Flask(__name__, template_folder='templates', static_url_path='/static')
game = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_game', methods=['POST'])
def start_game():
    global game
    data = request.get_json()
    grid_size = data['grid_size']
    name = data['name']
    game = Snake(grid_size, name)
    game.initialize_board()
    response = {
        'message': 'Game started successfully.',
        'game': {
            'snake': game.snake,
            'food': game.food,
            'score': game.score,
            'highest_score': game.highest_score,
            'grid_size': game.grid_size
        }
    }
    return jsonify(response)


@app.route('/move', methods=['POST'])
def move():
    global game
    direction = request.get_json()['direction']
    game.change_direction(direction)
    result = game.move()
    response = {
        'result': result,
        'game': {
            'snake': game.snake,
            'food': game.food,
            'score': game.score,
            'highest_score': game.highest_score,
            'grid_size': game.grid_size
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
