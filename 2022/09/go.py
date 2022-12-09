import numpy as np

def get_coords(move):
  if move == 'R': return [1,0]
  if move == 'U': return [0,1]
  if move == 'L': return [-1,0]
  if move == 'D': return [0,-1]

def get_path(input):
  path = []
  for line in lines:
    move, times = str.split(line)
    for i in range(int(times)):
      path.append(get_coords(move))
  return np.array(path)

def tail_round(v):
  if v == 0.5: return 1
  if v == -0.5: return -1
  return int(v)

def updateTail(head, tail):
  sub = np.subtract(head, tail)
  abssub = np.absolute(sub)
  isTouching = abssub[0] < 2 and abssub[1] < 2

  if isTouching: return tail

  tail_move = list(map(tail_round, list(sub/2)))
  return np.add(tail, tail_move)

with open('input.txt') as f:
  lines = f.read().splitlines()
  head = np.array([0,0])
  tail = np.array([0,0])
  path = get_path(lines)
  result = set()
  result2 = set()

  for step in path:
    head = np.add(head, step)
    tail = updateTail(head, tail)
    result.add(np.array2string(tail))
  
  rope = [np.array([0,0]) for i in range(10)]

  for step in path:
    rope[0] = np.add(rope[0], step)
    for i in range(1,10):
      rope[i] = updateTail(rope[i-1], rope[i])
    result2.add(np.array2string(rope[-1]))

  print('part 1:', len(result))
  print('part 2:', len(result2))