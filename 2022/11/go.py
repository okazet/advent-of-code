import re

with open('input.txt') as f:
  mi = f.read().split('\n\n')

  items = []
  operations = []
  tests = []
  decisions = []
  
  for m in mi:
    lines = [str.strip(l) for l in m.splitlines()]
    items.append([int(n) for n in re.findall('[0-9]+', lines[1])])
    operations.append(lines[2].split(' = ')[-1])
    tests.append(int(lines[3].split(' by ')[-1]))
    decisions.append([int(lines[4].split(' ')[-1]), int(lines[5].split(' ')[-1])])

  monkey_count = len(items)
  rounds = 20
  inspections = [0 for _ in range(monkey_count)]

  for r in range(rounds):
    print('round', r + 1)
    for i in range(monkey_count):
      items_no = len(items[i])
      if items_no == 0: continue

      for _ in range(items_no):
        inspections[i] += 1
        old = items[i].pop(0)
        new = eval(operations[i])
        # print(i, old, new)
        throw_index = 0 if new % tests[i] == 0 else 1
        monkey_no = decisions[i][throw_index]
        items[monkey_no].append(new)

      # print('ins', inspections)
    # for i in items:
    #   print(i)

  inspections.sort()
  inspections.reverse()
  print('monkey business:', inspections[0] * inspections[1])




      
      












