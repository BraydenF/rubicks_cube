from consts import *
from utils import splitString
from Side import Side

class Cube:
  # Could work logic to be other sizes of cubes
  totalSquares = TOTAL_SQUARES
  numberOfSides = NUMBER_OF_SIDES
  squaresPerSide = Side.squaresPerSide

  def __init__(self, squares):
    if len(squares) != Cube.totalSquares:
      raise SquaresInputLengthError('Cube', squares)

    self.squares = squares
    self.split = splitString(squares, Cube.squaresPerSide)
    self.top = Side(self.split[0], TOP)
    self.bottom = Side(self.split[1], BOTTOM)
    self.left = Side(self.split[2], LEFT)
    self.right = Side(self.split[3], RIGHT)
    self.front = Side(self.split[4], FRONT)
    self.back = Side(self.split[5], BACK)

    # validates all center positions on in input string
    if self.top.color != GREEN: raise Exception('Invalid color at position: top')
    if self.bottom.color != BLUE: raise Exception('Invalid color at position: bottom')
    if self.left.color != RED: raise Exception('Invalid color at position: left')
    if self.right.color != ORANGE: raise Exception('Invalid color at position: right')
    if self.front.color != WHITE: raise Exception('Invalid color at position: front')
    if self.back.color != YELLOW: raise Exception('Invalid color at position: back')

    # todo: do I need to validate anything else? What about the corners?

  def turnFront(clockwise = true, turns = 1):
    # todo: turnFront

  def turnRight(clockwise = true):
    # todo: turnRight

  def turnUp(clockwise = true):
    # todo: turnUp

  def turnLeft(clockwise = true):
    # todo: turnLeft

  def turnBack(clockwise = true):
    # todo: turnBack

  def turnDown(clockwise = true):
    # todo: turnDown

  def turnM(down = true):
    #  todo: turnM

  def turnE(right = true):
    #  todo: turnE

  def turnS(right = true):
    #  todo: turnS


  def __str__(self):
    return self.top.__str__() + ' ' + self.bottom.__str__() + ' ' + self.left.__str__() + ' ' + self.right.__str__() + ' ' + self.front.__str__() + ' ' + self.back.__str__()
