def prio(items):
  acc = 0
  for i in items:
    if i.isupper(): acc += ord(i) - 38
    if i.islower(): acc += ord(i) - 96
  return acc

with open('input.txt') as f:
  lines = f.read().splitlines()

  items = []
  for sack in lines:
    comp1 = set(sack[:len(sack)//2])
    comp2 = set(sack[len(sack)//2:])

    items.append(list(comp1 & comp2)[0])
  
  print(prio(items))

with open('input.txt') as f:
  lines = f.read().splitlines()
  badges = []
  for i in range(len(lines) // 3):
    group = lines[i*3:i*3+3]
    badges.append(list(set(group[0]) & set(group[1]) & set(group[2]))[0])
  print(prio(badges))
  