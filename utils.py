def splitString(str, numOfSplits = 9):
  return list(map(''.join, zip(*[iter(str)]*numOfSplits)))

    