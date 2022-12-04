def get_elves(pair):
  elves = pair.split(',')
  elf1 = elves[0].split('-')
  elf2 = elves[1].split('-')

  return [
    [int(elf1[0]), int(elf1[1])],
    [int(elf2[0]), int(elf2[1])], 
  ]

def check_inclusion(elves):
  if elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]: return True
  if elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]: return True

  return False

def overlap(elves):
  x = range(elves[0][0], int(elves[0][1]) + 1)
  y = range(elves[1][0], elves[1][1] + 1)
  xs = set(x)
  return xs.intersection(set(y))

with open('input.txt') as f:
  lines = f.read().splitlines()

  total = 0

  for pair in lines:
    elves = get_elves(pair)
    if check_inclusion(elves): total += 1

  print(total)

  total = 0

  for pair in lines:
    elves = get_elves(pair)
    if len(overlap(elves)): total += 1

  print(total)
