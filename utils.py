def readlines(filename, callback):
  with open(filename, 'r') as reader:
    line = reader.readline()
    while line:
      callback(line.strip())
      line = reader.readline()

def readfile(filename):
  with open(filename, 'r') as reader:
    # return list(map(int, reader.read().strip().split('\n')))
    return reader.read().strip().split('\n')
