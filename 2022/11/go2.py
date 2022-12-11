import re

class Item:
  def __init__(self, number, tests):
    self.number = number
    self.tests = tests
    self.modulos = [(number % t) for t in tests]

  def add(self, x):
    for i, modulo in enumerate(self.modulos):
      self.modulos[i] = (modulo + x) % tests[i]

  def multi(self, x):
    for i, modulo in enumerate(self.modulos):
      t = tests[i]
      self.modulos[i] = ((modulo) * (x % t)) % t

  def pow2(self):
    for i, modulo in enumerate(self.modulos):
      self.modulos[i] = (modulo * modulo) % tests[i]

  def get_modulo(self, i):
    return self.modulos[i]

  def get_number(self):
    return self.number

def calc_operation(oper):
  if oper == 'old * old': return ['pow2']
  a, o, b = oper.split(' ')[:]

  return ['add' if o == '+' else 'multi', int(b)]

with open('input.txt') as f:
  mi = f.read().split('\n\n')

  items = []
  monkey_stuff = []
  operations = []
  tests = []
  decisions = []
  
  for m in mi:
    lines = [str.strip(l) for l in m.splitlines()]
    monkey_stuff.append([int(n) for n in re.findall('[0-9]+', lines[1])])
    operations.append(lines[2].split(' = ')[-1])
    tests.append(int(lines[3].split(' by ')[-1]))
    decisions.append([int(lines[4].split(' ')[-1]), int(lines[5].split(' ')[-1])])

  for levels in monkey_stuff:
    items.append([Item(level, tests) for level in levels])

  monkey_count = len(items)
  rounds = 10000
  inspections = [0 for _ in range(monkey_count)]

  for r in range(rounds):
    for i in range(monkey_count):
      items_no = len(items[i])
      if items_no == 0: continue

      for _ in range(items_no):
        inspections[i] += 1
        item = items[i].pop(0)
        
        op = calc_operation(operations[i])
        if op[0] == 'pow2': item.pow2()
        if op[0] == 'multi': item.multi(op[1])
        if op[0] == 'add': item.add(op[1])
        
        throw_index = 0 if item.get_modulo(i) == 0 else 1
        monkey_no = decisions[i][throw_index]
        items[monkey_no].append(item)

  inspections.sort()
  inspections.reverse()
  print('monkey business:', inspections[0] * inspections[1])