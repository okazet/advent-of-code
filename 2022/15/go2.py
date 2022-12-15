import re

def manhattan(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def mergeRanges(ranges):
  ranges = ranges[:]
  ranges.sort()
  stack = [ranges[0]]
  for r in ranges[1:]:
      if stack[-1][0] <= r[0] <= stack[-1][-1]:
          stack[-1][-1] = max(stack[-1][-1], r[-1])
      else:
          stack.append(r)
  return stack

def searchSignal(ranges, row):
  xpos = 0
  for s,e in ranges:
    if xpos < s:
      return xpos * 4000000 + row 
    else: xpos = e + 1


with open('input.txt') as f:

  size = 4000000
  # size = 20
  lines = [list(map(int, re.findall('-?[0-9]+', line))) for line in f.read().splitlines()]

  for row in range(size + 1):
    mark = set()
    ranges = []

    for line in lines:  
      sx, sy, bx, by = line
      md = manhattan(sx, sy, bx, by)

      collision = md - abs(row - sy)
      if  collision >= 0:
        ranges.append([sx - collision, sx + collision])
    
    ranges = mergeRanges(ranges)
    
    signal = searchSignal(ranges, row)
    if signal:
      print(signal)
      break

