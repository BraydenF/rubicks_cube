from utils import splitString
from Cube import Cube

def main():
  top = 'ggggggggg'
  bottom = 'bbbbbbbbb'
  left = 'rrrrrrrrr'
  right = 'ooooooooo'
  front = 'wwwwwwwww'
  back = 'yyyyyyyyy'

  input = top + bottom + left + right + front + back 

  cube = Cube(input)

  print(cube)

main()
