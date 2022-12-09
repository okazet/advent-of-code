import numpy as np

def get_coords(move):
  if move == 'R': return [1,0]
  if move == 'U': return [0,1]
  if move == 'L': return [-1,0]
  if move == 'D': return [0,-1]

def get_path(lines):
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

def update(head, tail):
  sub = np.subtract(head, tail)
  abssub = np.absolute(sub)
  
  isTouching = abssub[0] < 2 and abssub[1] < 2
  if isTouching: return tail

  tail_move = list(map(tail_round, list(sub/2)))
  return np.add(tail, tail_move)

def get_tail_positions(rope, path):
  rope_size = len(rope)
  positions = set()
  for step in path:
    rope[0] = np.add(rope[0], step)
    for i in range(1,rope_size):
      rope[i] = update(rope[i-1], rope[i])
    positions.add(np.array2string(rope[-1]))  
  return positions

with open('input.txt') as f:
  path = get_path(f.read().splitlines())
  rope2 = [np.array([0,0]) for i in range(2)]
  rope10 = [np.array([0,0]) for i in range(10)]
  
  print('part 1', len(get_tail_positions(rope2,path)))
  print('part 2', len(get_tail_positions(rope10, path)))