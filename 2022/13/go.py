import ast
from functools import cmp_to_key

def compare(left, right):

  if isinstance(left, int) and isinstance(right, int):
    if left < right: return True
    if left > right: return False
    return None

  if isinstance(left, list) and isinstance(right, list):
    size = min(len(left), len(right))
    
    for i in range(size):  
      result = compare(left[i], right[i])
      if result != None: return result
    
    if len(left) < len(right): return True
    if len(left) > len(right): return False
    return None
  
  if isinstance(left, int) and isinstance(right, list):
    if right: return compare([left], right)
    elif not right: return compare([left], [0])
    
  if isinstance(left, list) and isinstance(right, int):
    if left: return compare(left, [right])
    elif not left: return compare([0], [right])
  
  return False

with open('input.txt') as f:
  file = f.read()
  pairs = file.split('\n\n')
  pairs = [pair.split('\n') for pair in pairs]

  result = []
  for i, (left, right) in enumerate(pairs):
    index = i + 1
    l = ast.literal_eval(left)
    r = ast.literal_eval(right)

    comparison = compare(l, r)
    if comparison: result.append(index)

  print('part 1:', sum(result))

  signals = [line for line in filter(lambda l: l, file.splitlines())]
  signals.extend(['[[2]]', '[[6]]'])

  def compareList(a, b):
    a = ast.literal_eval(a)
    b = ast.literal_eval(b)

    return -1 if compare(a, b) else 1

  in_order = sorted(signals, key=cmp_to_key(compareList))

  print('part 2', (in_order.index('[[2]]') + 1) * (in_order.index('[[6]]') + 1))