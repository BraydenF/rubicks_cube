from consts import *

# Custom Exceptions for ensuring validity of rubicks cube
class SquaresInputLengthError(Exception):
  def __init__(self, errorType, val):
    if errorType != 'Cube' and errorType != 'Side':
      raise Exception('Invalid type: ' + errorType)

    message = 'A {}\'s input squares string must be {} characters long; {} provided.'.format(errorType, (TOTAL_SQUARES if errorType == 'Cube' else SQUARES_PER_SIDE), len(val))
    print(message)
    super().__init__(message)