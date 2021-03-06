
from Board import Board
from misc_functions import *
from constants import *
import random


class Snake():
  def __init__(self, id, name, health, body, head, length, shout, board):
    self.id = id
    self.name = name
    self.health = health
    self.body = body
    self.head = head
    self.length = length
    self.shout = shout
    #self.squad = squad
    self.board = board

    self.possible_moves = ["up", "down", "left", "right"]



  # ----- USEFUL VARIABLES -----
  


 # ----- END USEFUL VARIABLES -----

  # ----- CALL MOVE FUNCTIONS -----

  def remove_illegal_moves(self, other_snakes):
    self.stay_in_bounds(self.board)
    self.dont_hit_body()
    # TODO: avoid other snakes
    self.avoid_snake_bodies(other_snakes)
    self.avoid_snake_heads(other_snakes)

    return

  def determine_next_move(self, other_snakes):
    self.get_food()

    return

  # ----- END CALL MOVE FUNCTIONS -----


  # ----- LOCATION CHOICE ------
  def get_food(self):
    for direction, space in get_adj_spaces(self.head).items():
      for food_space in self.board.food:
        # print(space == food_space)
        if ( (space == food_space) ):#and (CHECK IF BIGGER SNAKE IS GONNA NOT GET IT) )
          # TODO ADD ALL GOBBLE SQUARES TO LIST THEN RANDOM THAT LIST
          print("GOBBLE", direction)
          self.make_move(direction)
    return


  # TODO def find_nearest_food(self):

  # ----- END LOCATION CHOICE -----

  # Removes move if it is still valid
  def remove_move(self, move: str):
    if move in self.possible_moves:
      self.possible_moves.remove(move)

  # Removes all possible moves except the one passed
  def make_move(self, move: str):
    if move in self.possible_moves:
      for cur_dir in DIRECTIONS:
        if cur_dir != move:
          self.remove_move(cur_dir)
    return


  # Don't go out of bounds
  def stay_in_bounds(self, board: Board):

    if self.head["x"] == 0:
        self.remove_move("left")
    if self.head["y"] == 0:
        self.remove_move("down")
    if self.head["x"] == board.width - 1:
        self.remove_move("right")
    if self.head["y"] == board.height - 1:
        self.remove_move("up")
    return

  # Don't hit your own body
  def dont_hit_body(self):
      for coord in self.body:
        # Only 4 elements
        for direction, space in get_adj_spaces(self.head).items():
          if space == coord:
            self.remove_move(direction)

      return

  # Prevent moving into another snakes body
  def avoid_snake_bodies(self, other_snakes):
    for cur_snake in other_snakes:
      # TODO: CHECK
      for body_coord in cur_snake.body:
        # Only 4 elements
        # TODO: FIX DIECTION, SPACE TO COORD
       for direction, space in get_adj_spaces(self.head).items():
          if space == body_coord:
            self.remove_move(direction)
    return


  def avoid_snake_heads(self, other_snakes):
  # IF TIE, GO TO BIGGER SNAKE (FOOD IS ADDED BEFORE COLLISION)
    for snake in other_snakes:
      if self.length < snake.length:
        my_adj_squares = get_adj_spaces(self.head)
        snakes_adj_squares = get_adj_spaces(self.head)

        for my_direction, my_space in my_adj_squares.items():
          for other_space in snakes_adj_squares.values():

            if my_space == other_space:
              self.remove_move(my_direction)

              return



  # ----- END ILLEGAL MOVES -----

  # ----- MISC METHODS -----          

  # Get adjacent spaces to the snake's head
  # Returns list in the form of [up,down,left,right]
  # With {x:_ , y:_} at each index

  # TODO CONVERT TO ANY SPACE
  # def get_adj_spaces(self):
  #   adj_up = {'x': self.head['x'], 'y': self.head['y'] + 1}
  #   adj_down = {'x': self.head['x'], 'y': self.head['y'] - 1}
  #   adj_left = {'x': self.head['x'] - 1, 'y': self.head['y']}
  #   adj_right = {'x': self.head['x'] + 1, 'y': self.head['y']}

  #   adj_squares = {"up": adj_up, "down": adj_down, "left": adj_left, "right": adj_right}

  #   return adj_squares


  

  def pick_move(self):

    print(self.possible_moves)
    move = random.choice(self.possible_moves)
    print("My move: " + move)
    print()
    return move
    
  # ----- END MISC METHODS -----   

  


  
    






# id": "snake-508e96ac-94ad-11ea-bb37",
#     "name": "My Snake",
#     "health": 54,
#     "body": [
#       {"x": 0, "y": 0}, 
#       {"x": 1, "y": 0}, 
#       {"x": 2, "y": 0}
#     ],
#     "latency": "111",
#     "head": {"x": 0, "y": 0},
#     "length": 3,
#     "shout": "why are we shouting??",
#     "squad": ""