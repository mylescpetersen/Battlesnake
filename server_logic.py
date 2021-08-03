import random
from typing import List, Dict

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""

# ----- BASIC MOVE DECISION: ILLEGAL MOVES -----

#
def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        remove_move("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        remove_move("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        remove_move("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        remove_move("up")

    return possible_moves

# Don't go out of bounds
def stay_in_bounds(my_head: Dict[str, int], board_height, board_width , possible_moves: List[str]) -> List[str]:

    if my_head["x"] == 0:
        remove_move("left")
    if my_head["y"] == 0:
        remove_move("down")
    if my_head["x"] == board_width - 1:
        remove_move("right")
    if my_head["y"] == board_height - 1:
        remove_move("up")

    return possible_moves

# Don't hit your own body
def dont_hit_body(my_body: List[dict], possible_moves: List[str]) -> List[str]:

    for coord in my_body:
      # Only 4 elements
      for direction, space in my_adj_spaces.items():
        if space == coord:
          remove_move(direction)

    return possible_moves

# Prevent moving into another snakes body
def avoid_snake_bodies(other_snakes: List[dict], possible_moves: List[str]) -> List[str]:

  for snake in other_snakes:
    for coord in snake["body"]:
      # Only 4 elements
      for direction, space in my_adj_spaces.items():
        if space == coord:
          remove_move(direction)


  return possible_moves


def avoid_snake_heads(my_head: Dict[str, int], other_snakes: List[dict], possible_moves: List[str]) -> List[str]:
  # IF TIE, GO TO BIGGER SNAKE (FOOD IS ADDED BEFORE COLLISION)

  # up = {'x' :my_head['x'], 'y': my_head['y'] + 1}
  # left = {'x': my_head['x'] - 1, 'y': my_head['y']}
  # down = {'x': my_head['x'], 'y': my_head['y'] - 1}
  # right = {'x': my_head['x'] + 1, 'y': my_head['y']}

  for snake in other_snakes:
    #print(snake["body"])
    if my_length <= snake["length"]:
      for coord in snake["body"]:
      # Only 4 elements
        for direction, space in my_adj_spaces.items():
          # if space in oth
            remove_move(direction)
            # TODO GET OTHER SNAKE HEAD'S ADJ SQUARES

  
    # if up == snake["head"]:
    #   remove_move("up")
    # if left == snake["head"]:
    #   remove_move("left")
    # if down == snake["head"]:
    #   remove_move("down")
    # if right == snake["head"]:
    #   remove_move("right")

  #  for snake in other_snakes:
  #    if (snake)
  #   for coord in snake["body"]:
  #     # Only 4 elements
  #     for direction, space in adj_spaces.items():
  #       if space == coord:
  #         remove_move(direction)


  return possible_moves 

# Stops snake from putting itself in a position to have no possible moves next turn
def dont_get_trapped(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:





  return possible_moves



# Gets adjacent squares given a square:
# Returns list in order: up, down, left, right
def get_adj_spaces(cur_space: Dict[str, int]):
  
  adj_up = {'x' :cur_space['x'], 'y': cur_space['y'] + 1}
  adj_down = {'x': cur_space['x'], 'y': cur_space['y'] - 1}
  adj_left = {'x': cur_space['x'] - 1, 'y': cur_space['y']}
  adj_right = {'x': cur_space['x'] + 1, 'y': cur_space['y']}
  
  adj_squares = [adj_up, adj_down, adj_left, adj_right]

  return adj_squares


# ----- END BASIC MOVE DECISION: ILLEGAL MOVES -----

# ----- MAIN FUNCTIONS TO CALL OTHER FUNCTIONS -----

# Removes move if it is still valid
def remove_move(move: str):
  global possible_moves
  if move in possible_moves:
    possible_moves.remove(move)

def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    
    """

    # My snake variables
    my_health = data["you"]["health"]
    my_length = data["you"]["length"]


  # Create Snake object
  # (self, health, body, head, length, shout, squad)
  my_snake = Snake()



    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    # All other snake objects
    other_snakes = data["board"]["snakes"]

    # Sets global list of move possibilities
    global possible_moves
    possible_moves = ["up", "down", "left", "right"]


    # ----- VARIABLES FROM DATA -----

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data['board']['height']
    board_width = data['board']['width']

    
    # Next move locations

    # adj_up = {'x' :my_head['x'], 'y': my_head['y'] + 1}
    # adj_left = {'x': my_head['x'] - 1, 'y': my_head['y']}
    # adj_down = {'x': my_head['x'], 'y': my_head['y'] - 1}
    # adj_right = {'x': my_head['x'] + 1, 'y': my_head['y']}

    move_locations = get_adj_spaces(my_head)
    print(move_locations)

    #  ----- DATA CONSTANTS (Won't be modified) ----- 

    # Adjacent spaces

    # global adj_spaces
    # adj_spaces = {'up':adj_up, 'left':adj_left, 'down':adj_down, 'right': adj_right}
    # global my_adj_spaces
    # my_adj_spaces = get_adj_squares("my_head")
    # print(my_adj_spaces)

    # My snake length
    global my_length
    my_length = data["you"]["length"]

    # ----- END DATA CONSTANTS ------

    # ----- END VARIABLES FROM DATA -----



    possible_moves = stay_in_bounds(my_head, board_height, board_width, possible_moves)

    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    possible_moves = dont_hit_body(my_body, possible_moves)

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    possible_moves = avoid_snake_bodies(other_snakes, possible_moves)

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    #print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

# ----- END MAIN FUNCTIONS TO CALL OTHER FUNCTIONS -----


example_data = {
  "game": {
    "id": "game-00fe20da-94ad-11ea-bb37",
    "ruleset": {
      "name": "standard",
      "version": "v.1.2.3"
    },
    "timeout": 500
  },
  "turn": 14,
  "board": {
    "height": 11,
    "width": 11,
    "food": [
      {"x": 5, "y": 5}, 
      {"x": 9, "y": 0}, 
      {"x": 2, "y": 6}
    ],
    "hazards": [
      {"x": 3, "y": 2}
    ],
    "snakes": [
      {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": ""
      }, 
      {
        "id": "snake-b67f4906-94ae-11ea-bb37",
        "name": "Another Snake",
        "health": 16,
        "body": [
          {"x": 5, "y": 4}, 
          {"x": 5, "y": 3}, 
          {"x": 6, "y": 3},
          {"x": 6, "y": 2}
        ],
        "latency": "222",
        "head": {"x": 5, "y": 4},
        "length": 4,
        "shout": "I'm not really sure...",
        "squad": ""
      }
    ]
  },
  "you": {
    "id": "snake-508e96ac-94ad-11ea-bb37",
    "name": "My Snake",
    "health": 54,
    "body": [
      {"x": 0, "y": 0}, 
      {"x": 1, "y": 0}, 
      {"x": 2, "y": 0}
    ],
    "latency": "111",
    "head": {"x": 0, "y": 0},
    "length": 3,
    "shout": "why are we shouting??",
    "squad": ""
  }
}