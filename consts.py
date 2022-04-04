CENTER_INDEX = 4

# square colors
GREEN = G = 'g'
BLUE = B ='b'
RED = R ='r'
ORANGE = O = 'o'
WHITE = W ='w'
YELLOW = Y ='y'

# positions
FRONT = F = 'F'
BACK = B = 'B'
LEFT = L = 'L'
RIGHT = R = 'R'
UP = U = 'U'
DOWN = D = 'D'

VALID_CORNERS = [
  # top view
  ORANGE + GREEN + YELLOW,
  WHITE + GREEN + ORANGE,
  RED + GREEN + WHITE,
  YELLOW + GREEN + RED,
  # bottom view
  RED + BLUE + YELLOW,
  WHITE + BLUE + RED,
  ORANGE + BLUE + WHITE,
  YELLOW + BLUE + ORANGE,
]

NUMBER_OF_SIDES = 6

# could change depending on cube size
CUBE_EDGE_LENGTH = 3
SQUARES_PER_SIDE = CUBE_EDGE_LENGTH**2
TOTAL_SQUARES = NUMBER_OF_SIDES * SQUARES_PER_SIDE # 54