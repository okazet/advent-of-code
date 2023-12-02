with open('input.txt') as f:
  lines = f.read().splitlines()

  result = 0

  for l in lines:
    g = l.split(':')

    gNo = g[0][5:]

    setsInput = g[1].split(';')
    setsNo = len(setsInput)

    sets = []

    for i in range(setsNo):
      sets.append(setsInput[i].split(', '))

    gameOk = True

    for set in sets:
      reds = 0
      greens = 0
      blues = 0

      for turn in set:
        show = turn.strip().split(' ')
        value = int(show[0])
        if (show[1] == 'red'): reds = reds + value
        if (show[1] == 'green'): greens = greens + value
        if (show[1] == 'blue'): blues = blues + value

      if (reds > 12 or greens > 13 or blues > 14):
        gameOk = False
    
    if gameOk: 
      result = result + int(gNo)

  print(result)
