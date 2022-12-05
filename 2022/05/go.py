def get_stacks(cratepart):
  cols_no = int(cratepart[-1][-2])
  cr = cratepart[:-1]

  stacks = []
  for i in range(cols_no):
    stacks.append([])

  for i in range(cols_no):
    for c in cr:
      crate_name = c[i*4+1]
      if crate_name.strip() != '': stacks[i].append(crate_name)

  for i in range(cols_no):
    stacks[i].reverse()

  return stacks

def get_program(instructionpart):
  program = []
  for line in instructionpart:
    spl = line.split(' ')
    program.append({
      'q': int(spl[1]),
      'from': int(spl[3]),
      'to': int(spl[5])
    })
  return program

with open('input.txt') as f:
  lines = f.read().splitlines()
  empty = lines.index('')
  cratepart = lines[:empty]
  instructionpart = lines[empty + 1:]

  stacks = get_stacks(cratepart)
  program = get_program(instructionpart)

  for i in program:
    q = i.get('q')
    o = i.get('from') - 1
    d = i.get('to') - 1
    take = stacks[o][-q:]
    take.reverse()
    stacks[o] = stacks[o][:-q]
    stacks[d].extend(take)

  result = ''
  for i in range(len(stacks)):
    result += stacks[i][-1:][0]
  print(result)

  # part two
  stacks = get_stacks(cratepart)

  for i in program:
    q = i.get('q')
    o = i.get('from') - 1
    d = i.get('to') - 1
    take = stacks[o][-q:]
    stacks[o] = stacks[o][:-q]
    stacks[d].extend(take)

  result = ''
  for i in range(len(stacks)):
    result += stacks[i][-1:][0]
  print(result)
  