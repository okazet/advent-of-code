with open('input.txt') as f:
  lines = f.read().splitlines()

  score = 0
  acc = 0

  for line in lines:
    if line == '': break
    opp = line.split(' ')[0]
    my = line.split(' ')[1]

    if my == 'X': score += 1
    if my == 'Y': score += 2
    if my == 'Z': score += 3

    if opp == 'A' and my == 'X': score += 3
    if opp == 'B' and my == 'Y': score += 3
    if opp == 'C' and my == 'Z': score += 3

    if opp == 'A' and my == 'Y': score += 6
    if opp == 'B' and my == 'Z': score += 6
    if opp == 'C' and my == 'X': score += 6

  for line in lines:
    if line == '': break
    opp = line.split(' ')[0]
    result = line.split(' ')[1]

    # X lose 0
    # Y draw 3
    # Z win 6

    # rock
    if opp == 'A' and result == 'X': acc += (0 + 3)
    if opp == 'A' and result == 'Y': acc += (3 + 1)
    if opp == 'A' and result == 'Z': acc += (6 + 2)

    # paper
    if opp == 'B' and result == 'X': acc += (0 + 1)
    if opp == 'B' and result == 'Y': acc += (3 + 2)
    if opp == 'B' and result == 'Z': acc += (6 + 3)
    
    # scissors
    if opp == 'C' and result == 'X': acc += (0 + 2)
    if opp == 'C' and result == 'Y': acc += (3 + 3)
    if opp == 'C' and result == 'Z': acc += (6 + 1)

  print(score)
  print(acc)




