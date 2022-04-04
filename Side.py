from consts import *

class Side:
  squaresPerSide = SQUARES_PER_SIDE

  def validateSide(side):
    print('todo: create function to validate a Side')

  def __init__(self, squares, position):
    if len(squares) != SQUARES_PER_SIDE:
      raise SquaresInputLengthError('Side', squares)

    self.position = position
    self.squares = squares
    self.color = squares[CENTER_INDEX]

  def __str__(self):
    return self.position + ':' + self.squares
