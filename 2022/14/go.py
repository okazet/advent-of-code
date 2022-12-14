import numpy as np

'o' = 'o'
'#' = '#'
'.' = '.'

def draw(cave, cropleft = 0):
  for l in np.fliplr(np.rot90(cave, k=3)):
    print(''.join(l[cropleft:]))

def fall(cave, sand):
  for d in [[0, 1], [-1, 1], [1, 1]]:
    new_coords = tuple(np.array(list(sand)) + d)

    if cave[new_coords] == '.': return new_coords
    else: continue

  return False

with open('input.txt') as f:
  input = f.read().splitlines()

  rock_scan = []
  ysize = 0
  for line in input:
    points = [list(map(int, coords.split(','))) for coords in line.split(' -> ')]
    ysize = max(ysize, *list(map(lambda p: p[1], points)))
    rock_scan.append(points)

  ysize = ysize + 3
  xsize = 500 + ysize
  cave = np.full((xsize, ysize), '.') 
  cave[:,-1] = '#'

  for rock in rock_scan:
    for i in range(len(rock) - 1):
      start, end = rock[i:i+2]
      x1, y1, x2, y2 = start + end
      x1, x2 = sorted([x1, x2])
      y1, y2 = sorted([y1, y2])
      cave[x1:x2+1, y1:y2+1] = '#'

  origin = (500, 0)
  last_count = -1
  length = 0
  
  while last_count < length:
    sand = origin
    last_count = length
    
    while sand[1] < ysize -1:
      new = fall(cave, sand)

      if new: 
        sand = new
      else:
        cave[sand] = 'o'
        break

    length = len(list(np.where(np.ravel(cave) == 'o')[0]))    

  draw(cave, 500 - ysize + 1)
  print('part 2', length)