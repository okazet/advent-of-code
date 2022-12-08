import numpy as np

def mark(forest, sheet):
  ran = range(len(forest))
  for r in ran:
    h = -1
    for c in ran:
      th = forest[r][c]
      if th > h:
        h = th
        sheet[r][c] = 1

def one_dim_scenic(arr):
  tree = arr[0]
  count = 0
  for t in arr[1:]:
    count += 1
    if t >= tree: break
  return count

with open('input.txt') as f:
  forest = np.array([list(r) for r in f.read().splitlines()], int)
  sheet = np.zeros(forest.shape, int)

  for i in range(4):
    forest = np.rot90(forest)
    sheet = np.rot90(sheet)
    mark(forest, sheet)
    
  scenics = []
  for r, c in np.transpose(np.nonzero(sheet)):
    scenics.append(
      np.prod([
        one_dim_scenic(forest[r:r+1,c:][0]),
        one_dim_scenic(forest[r:r+1,:c+1][0][::-1]),
        one_dim_scenic(np.ravel(forest[:,c:c+1])[r:]),
        one_dim_scenic(np.ravel(forest[:,c:c+1])[:r+1][::-1])
      ])
    )

  print('part 1:', np.count_nonzero(sheet))
  print('part 2:', max(scenics))
