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
          stack.append(i)
          
  return stack

with open('input.txt') as f:

  row = 10
  row = 2000000

  mark = set()
  beacons = set()
  ranges = []

  for line in f.read().splitlines():
    sx, sy, bx, by = map(int, re.findall('-?[0-9]+', line))
    beacons.add((bx, by))
    md = manhattan(sx, sy, bx, by)
    collision = md - abs(row - sy)

    if  collision >= 0:
      ranges.append([sx - collision, sx + collision])

  ranges = mergeRanges(ranges)

  for s, e in ranges:
    for x in range(s, e + 1):
      mark.add(x)
  
  for x, y in beacons:
    if y == row:
      mark.remove(x)

  print(len(mark))