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

    reds = 0
    greens = 0
    blues = 0

    for set in sets:
      for turn in set:
        show = turn.strip().split(' ')
        value = int(show[0])
        if (show[1] == 'red'): reds = max(reds, value)
        if (show[1] == 'green'): greens = max(greens, value)
        if (show[1] == 'blue'): blues = max(blues, value)
      
    result = result + reds * greens * blues

  print(result)
