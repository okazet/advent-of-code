from ast import literal_eval
from functools import cmp_to_key

def compare(a, b):
  a = literal_eval(str(a))
  b = literal_eval(str(b))

  if type(a) is int and type(b) is int: 
    return a - b

  if type(a) is list and type(b) is list:
    result = [compare(za, zb) for za, zb in zip(a, b)]
    return next((r for r in result if r), len(a) - len(b))    
  
  if type(a) is int and type(b) is list:
    return compare([a], b if b else [0])
    
  if type(a) is list and type(b) is int:
    return compare(a if a else [0], [b])
  
  return 0

with open('input.txt') as f:
  signals = list(filter(len, f.read().splitlines()))
 
  result = 0

  for i in range(len(signals) // 2):
    a, b = signals[i*2:i*2+2]
    if compare(a, b) < 0: result += (i + 1)
      
  print('part 1:', result)

  dividers = ['[[2]]', '[[6]]']
  signals.extend(dividers)
  asc = sorted(signals, key=cmp_to_key(compare))

  result = 1

  for i, signal in enumerate(asc):
    if signal in dividers: result *= i + 1

  print('part 2', result)