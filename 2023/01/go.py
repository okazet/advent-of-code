result = 0

with open('input.txt') as f:
  lines = f.read().splitlines()

  for l in lines:

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


