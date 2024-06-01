# Snake Game

## Overview

ProjectSnake is a classic snake game application where users can experience the thrill of guiding a snake through a maze, collecting points, and avoiding collisions. This repository contains the codebase for the application, along with essential features such as customizable map size, user input for their name, and persistent storage of game data.

## Features

- **Customizable User Name:** Users have the flexibility to input their name, adding a personalized touch to their gaming experience.
  
- **Collision Detection:** The game prevents the snake from passing through walls, ensuring that players must navigate strategically to avoid collisions and progress through the maze successfully.
  
- **Database Integration:** ProjectSnake incorporates a database to store essential user information, including their name, chosen map size, and points earned. Each lengthening of the snake awards the player 1 point, which is stored for future reference.

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

3. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```
   
## Run

1. After configuring the game-init.json file, run the Flask application:

   ```
   python app.py
   ```
2. Open a web browser and navigate to http://127.0.0.1:5001 to play the game.


3. Follow the on-screen instructions to take turns making moves and enjoy the game!
