def draw_screen(screen):
  for r in screen:
    print(''.join(list(r)))

with open('input.txt') as f:
  values = []
  registry = 1
  strength = 0
  screen = [['.' for l in range(40)][:] for r in range(6)]

  for line in f.read().splitlines():
    values.append(0)
    if line.startswith('add'):
      values.append(int(line.split()[1]))

  for i in range(len(values)):
    value = values[i]
    cycle = i + 1
    
    if (cycle + 20 ) % 40 == 0:
      strength += cycle * registry

    pixel = (i) % 40
    row = int((i) / 40)
    sprite = [registry - 1, registry, registry + 1]
    screen[row][pixel] = '#' if pixel in sprite else '.'   

    registry += value

  print('signal strength:', strength)
  draw_screen(screen)