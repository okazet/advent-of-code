
def calc_scientic(forest, ri, ci):
  size = len(forest[0])
  tree = forest[ri][ci]
  
  # r
  count_r = 0
  th = tree
  for c in range(ci+1, size):
    th = forest[ri][c]
    if th < tree:
      count_r += 1
    else:
      count_r += 1
      break

  # l
  count_l = 0
  if ci > 0:
    th = tree
    for c in range(ci-1, -1, -1):
      th = forest[ri][c]
      if th < tree:
        count_l += 1
      else:
        count_l += 1
        break

  # d
  count_d = 0
  th = tree
  for r in range(ri+1, size):
    th = forest[r][ci]
    if th < tree:
      count_d += 1
    else:
      count_d += 1
      break

  count_t = 0
  # t
  if ri > 0:
    th = tree
    for r in range(ri-1, -1, -1):
      th = forest[r][ci]
      if th < tree:
        count_t += 1
      else:
        count_t += 1
        break

  return(count_d * count_l * count_r * count_t)

with open('input.txt') as f:
  lines = f.read().splitlines()
  size = len(lines)
  forest = [list(line) for line in lines]
  tmap = [[0] * size for i in range(size)]

  for r in range(size):
    # l-r
    h = -1
    for c in range(size):
      th = int(forest[r][c])
      if th > h:
        h = th
        tmap[r][c] = 1

    # r-l
    h = -1
    for c in range(size):
      th = int(forest[r][-c-1])
      if th > h:
        h = th
        tmap[r][-c-1] = 1

  for c in range(1,size-1):
    # t-b
    h = -1
    for r in range(size):
      th = int(forest[r][c])
      if th > h:
        h = th
        tmap[r][c] = 1

    # b-t
    h = -1
    for r in range(size):
      th = int(forest[-r-1][c])
      if th > h:
        h = th
        tmap[-r-1][c] = 1

  count = sum([sum(m) for m in tmap])
  print('part 1:', count)
  
  candidates = []
  for r in range(size):
    for c in range(size):
      if tmap[r][c] == 1:
        candidates.append(calc_scientic(forest, r, c))

  print('part 2:', max(candidates))