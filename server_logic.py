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
def dont_hit_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:

    up = {'x' :my_head['x'], 'y': my_head['y'] + 1}
    left = {'x': my_head['x'] - 1, 'y': my_head['y']}
    down = {'x': my_head['x'], 'y': my_head['y'] - 1}
    right = {'x': my_head['x'] + 1, 'y': my_head['y']}

    for coord in my_body:
      # print(coord, up)
      # print(coord, left)
      # print(coord, down)
      # print(coord, right)
      if up == coord:
        remove_move("up")
      if left == coord:
        remove_move("left")
      if down == coord:
        remove_move("down")
      if right == coord:
        remove_move("right")

    return possible_moves

# Prevent moving into another snakes body
def avoid_snake_bodies(my_head: Dict[str, int], other_snakes: List[dict], possible_moves: List[str]) -> List[str]:

  up = {'x' :my_head['x'], 'y': my_head['y'] + 1}
  left = {'x': my_head['x'] - 1, 'y': my_head['y']}
  down = {'x': my_head['x'], 'y': my_head['y'] - 1}
  right = {'x': my_head['x'] + 1, 'y': my_head['y']}

  for snake in other_snakes:
    print(snake["body"])

    for coord in snake["body"]:

      if up == coord:
        remove_move("up")
      if left == coord:
        remove_move("left")
      if down == coord:
        remove_move("down")
      if right == coord:
        remove_move("right")


  return possible_moves


def avoid_snake_heads(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
  # IF TIE, GO TO BIGGER SNAKE (FOOD IS ADDED BEFORE COLLISION)


  return possible_moves 

# Stops snake from putting itself in a position to have no possible moves next turn
def dont_get_trapped(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:




  return possible_moves







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
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    # All other snake objects
    other_snakes = data["board"]["snakes"]

    print(other_snakes)
    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    #print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}\n")
    print(f"My Battlesnakes body this turn is: {my_body}\n")

    # Sets global list of move possibilities
    global possible_moves
    possible_moves = ["up", "down", "left", "right"]


    # ----- VARIABLES FROM DATA -----

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data['board']['height']
    board_width = data['board']['width']

    # ----- END VARIABLES FROM DATA -----



    possible_moves = stay_in_bounds(my_head, board_height, board_width, possible_moves)

    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    possible_moves = dont_hit_body(my_head, my_body, possible_moves)

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    possible_moves = avoid_snake_bodies(my_head, other_snakes, possible_moves)

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

# ----- END MAIN FUNCTIONS TO CALL OTHER FUNCTIONS -----


# EXAMPLE DATA
# {'game': {'id': '694cfabe-22d0-4eb5-b466-c21cb5ae63a8', 'ruleset': {'name': 'solo', 'version': 'v1.0.17'}, 'timeout': 500}, 'turn': 11, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_J6gKPMMrVRfXP8tjBDG66G4P', 'name': 'Snekky snek', 'latency': '256', 'health': 99, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 4, 'shout': ''}], 'food': [{'x': 6, 'y': 2}, {'x': 5, 'y': 5}, {'x': 9, 'y': 6}, {'x': 10, 'y': 1}, {'x': 3, 'y': 9}, {'x': 2, 'y': 3}, {'x': 3, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_J6gKPMMrVRfXP8tjBDG66G4P', 'name': 'Snekky snek', 'latency': '256', 'health': 99, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 4, 'shout': ''}}

# Snakes:
#  Snake1:
   # {
#   "id": "totally-unique-snake-id",
#   "name": "Sneky McSnek Face",
#   "health": 54,
#   "body": [
#     {"x": 0, "y": 0}, 
#     {"x": 1, "y": 0}, 
#     {"x": 2, "y": 0}
#   ],
#   "latency": "123",
#   "head": {"x": 0, "y": 0},
#   "length": 3,
#   "shout": "why are we shouting??",
#   "squad": "1"
