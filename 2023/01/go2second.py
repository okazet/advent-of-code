result = 0

with open('input.txt') as f:
  lines = f.read().splitlines()

  for l in lines:
    # print('processinźg', l)

    l = l.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')

    for i in range(0, len(l)):
      h = l[i]

      if h.isdigit():
        l = l[i:]
        break

    l = l[::-1]

    for i in range(0, len(l)):
      h = l[i]

      if h.isdigit():
        l = l[i:]
        break

    l = l[::-1]

    numberString = l[0] + l[-1]

    result = result + int(numberString)

print(result)





