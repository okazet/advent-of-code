def get_stacks(crate_input):
  cols_no = int(crate_input[-1][-2])
  ci = crate_input[:-1]

  stacks = []
    
  for i in range(cols_no):
    stacks.append([])
    for c in ci:
      crate_name = c[i*4+1]
      if crate_name.strip() != '': stacks[i].append(crate_name)

  for i in range(cols_no):
    stacks[i].reverse()

  return stacks

def get_program(program_input):
  program = []
  for line in program_input:
    spl = line.split(' ')
    program.append({
      'q': int(spl[1]),
      'from': int(spl[3]),
      'to': int(spl[5])
    })
  return program

def calc_result(stacks_result):
  result = ''
  for i in range(len(stacks_result)):
    result += stacks_result[i][-1:][0]
  return result

def rearrange(stacks, program, reverse):
  for i in program:
    q = i.get('q')
    o = i.get('from') - 1
    d = i.get('to') - 1
    take = stacks[o][-q:]
    if reverse: take.reverse()
    stacks[o] = stacks[o][:-q]
    stacks[d].extend(take)
  return stacks

with open('input.txt') as f:
  lines = f.read().splitlines()
  empty_index = lines.index('')
  crate_input = lines[:empty_index]
  program_input = lines[empty_index + 1:]

  program = get_program(program_input)
  
  # part one
  stacks = get_stacks(crate_input)
  stacks_result = rearrange(stacks, program, True)

  print(calc_result(stacks_result))

  # part two
  stacks = get_stacks(crate_input)
  stacks_result = rearrange(stacks, program, False)

  print(calc_result(stacks_result))  
