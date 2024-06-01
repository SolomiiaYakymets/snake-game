from packages.game_logic import Snake


def test_snake_length():
    snake_length = 3
    game = Snake(5, "name")
    game.initialize_board()

    assert len(game.snake) == snake_length
    for segment in game.snake:
        assert 0 <= segment[0] < 5 and 0 <= segment[1] < 5


def test_snake_direction():
    game = Snake(5, "name")

    if game.change_direction('w'):
        assert game.direction == (-1, 0)
    if game.change_direction('s'):
        assert game.direction == (1, 0)
    if game.change_direction('a'):
        assert game.direction == (0, -1)
    if game.change_direction('d'):
        assert game.direction == (0, 1)


def test_snake_move():
    game = Snake(5, "name")
    game.snake = [(1, 1), (1, 2), (1, 3)]
    game.direction = (1, 0)
    game.move()

    assert game.snake[0] == (2, 1)
    assert game.snake[1] == (1, 1)
    assert game.snake[2] == (1, 2)


def test_snake_move_out_of_grid():
    expected_move_valid = False
    game = Snake(5, "name")
    game.snake = [(0, 1), (0, 2), (0, 3)]
    game.direction = (-1, 0)
    move_valid = game.move()

    assert move_valid == expected_move_valid


def test_snake_self_collision():
    expected_move_valid = False
    game = Snake(5, "name")
    game.snake = [(3, 3), (2, 3), (2, 4), (3, 4)]
    game.direction = (0, 1)
    move_valid = game.move()

    assert move_valid == expected_move_valid


def test_win_condition():
    expected_win_condition = True
    game = Snake(3, "name")
    game.snake = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)]

    assert game.check_win() == expected_win_condition


def test_snake_growth():
    game = Snake(5, "name")

    game.snake = [(1, 2), (1, 3)]
    game.food = (1, 2)

    game.move()

    assert len(game.snake) == 3


def test_display_food():
    game = Snake(5, "name")
    game.display_food()
    food_position = game.food

    assert 0 <= food_position[0] < 5
    assert 0 <= food_position[1] < 5


def test_food_consumption():
    game = Snake(5, "name")
    game.snake = [(1, 1), (1, 2)]
    game.food = (1, 2)
    game.direction = (1, 1)
    game.move()

    assert game.food != (1, 2)
    assert game.score == 1
