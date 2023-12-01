result = 0

with open('input2.txt') as f:
  lines = f.read().splitlines()

  for l in lines:
    for i in range(0, len(l)):
      h = l[i]

      if h.isdigit():
        l = l[i:]
        break

      t = l[i:]
      
      if t.startswith('one'):
        l = l.replace('one', '1')
        l = l[i:]
        break

      if t.startswith('two'):
        l = l.replace('two', '2')
        l = l[i:]
        break

      if t.startswith('three'):
        l = l.replace('three', '3')
        l = l[i:]
        break

      if t.startswith('four'):
        l = l.replace('four', '4')
        l = l[i:]
        break

      if t.startswith('five'):
        l = l.replace('five', '5')
        l = l[i:]
        break

      if t.startswith('six'):
        l = l.replace('six', '6')
        l = l[i:]
        break

      if t.startswith('seven'):
        l = l.replace('seven', '7')
        l = l[i:]
        break

      if t.startswith('eight'):
        l = l.replace('eight', '8')
        l = l[i:]
        break

      if t.startswith('nine'):
        l = l.replace('nine', '9')
        l = l[i:]
        break   

    l = l[::-1]

    for i in range(0, len(l)):
      h = l[i]

      if h.isdigit():
        l = l[i:]
        break

      t = l[i:]
      
      if t.startswith('one'[::-1]):
        l = l.replace('one'[::-1], '1')
        l = l[i:]
        break

      if t.startswith('two'[::-1]):
        l = l.replace('two'[::-1], '2')
        l = l[i:]
        break

      if t.startswith('three'[::-1]):
        l = l.replace('three'[::-1], '3')
        l = l[i:]
        break

      if t.startswith('four'[::-1]):
        l = l.replace('four'[::-1], '4')
        l = l[i:]
        break

      if t.startswith('five'[::-1]):
        l = l.replace('five'[::-1], '5')
        l = l[i:]
        break

      if t.startswith('six'[::-1]):
        l = l.replace('six'[::-1], '6')
        l = l[i:]
        break

      if t.startswith('seven'[::-1]):
        l = l.replace('seven'[::-1], '7')
        l = l[i:]
        break

      if t.startswith('eight'[::-1]):
        l = l.replace('eight'[::-1], '8')
        l = l[i:]
        break

      if t.startswith('nine'[::-1]):
        l = l.replace('nine'[::-1], '9')
        l = l[i:]
        break           

    l = l[::-1]
    numberString = l[0] + l[-1]

    result = result + int(numberString)

print(result)





