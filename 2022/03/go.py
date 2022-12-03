def prio(items):
  acc = 0
  for i in items:
    if i.isupper(): acc += ord(i) - 38
    if i.islower(): acc += ord(i) - 96
  return acc

with open('input.txt') as f:
  lines = f.read().splitlines()

  repeats = []

  for sack in lines:
    rep = []
    comp1 = sack[:len(sack)//2]
    comp2 = sack[len(sack)//2:]

    for i1 in comp1:
      for i2 in comp2:
        if i1 == i2: rep.append(i2)
    
    repeats.append(rep[0])

  print(prio(repeats))

def divide_chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i + n]

with open('input.txt') as f:
  lines = f.read().splitlines()
  groups = list(divide_chunks(lines, 3))

  badges = []

  for group in groups:
    sack1 = group[0]
    sack2 = group[1]
    sack3 = group[2]
    badge = []
    for i1 in sack1:
      for i2 in sack2:
        for i3 in sack3:
          if i1 == i2 and i2 == i3: badge.append(i2)

    badges.append(badge[0])

print(prio(badges))
