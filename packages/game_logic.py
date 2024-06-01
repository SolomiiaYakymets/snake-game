import random
from database.mongodb import MongoDB


class Snake:
    def __init__(self, grid_size, name):
        self.mongo = MongoDB()
        self.direction = (0, -1)
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.snake = []
        self.food = (0, 0)
        self.score = 0
        self.name = name
        self.highest_score = 0

    def initialize_board(self):
        head_row = random.randint(0, self.grid_size - 1)
        head_col = random.randint(0, self.grid_size - 3)
        self.snake = [(head_row, head_col), (head_row, head_col + 1), (head_row, head_col + 2)]
        self.food = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

    def update_board(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if (row, col) in self.snake:
                    if (row, col) == self.snake[0]:
                        self.grid[row][col] = 'H'
                    else:
                        self.grid[row][col] = 'S'
                elif (row, col) == self.food:
                    self.grid[row][col] = '*'
                else:
                    self.grid[row][col] = ' '

    def move(self):
        self.display_food()
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        if head[0] != self.grid_size and head[0] != -1 and head[1] != self.grid_size and head[1] != -1:
            for segment in self.snake[1:]:
                if segment[0] == head[0] and segment[1] == head[1]:
                    return False
            self.snake.pop()
            self.snake.insert(0, head)
        else:
            return False
        self.update_board()
        self.highest_score = self.mongo.get_highest_score(self.name)
        self.mongo.save_score(self.name, self.score, self.grid_size)
        return True

    def display_food(self):
        for segment in self.snake:
            if segment == self.food:
                self.food = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
                self.score += 1
                tail = (self.snake[-1][0] + self.direction[0], self.snake[-1][1] + self.direction[1])
                self.snake.append(tail)

    def check_win(self):
        if len(self.snake) == self.grid_size * self.grid_size:
            return True
        else:
            return False

    def change_direction(self, direction):
        if direction == 'w' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == 's' and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif direction == 'a' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'd' and self.direction != (0, -1):
            self.direction = (0, 1)
