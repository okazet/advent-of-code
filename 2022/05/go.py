import copy

def get_stacks(crate_input):
  cols_no = int(crate_input[-1][-2])
  ci = crate_input[:-1]
  stacks = []
    
  for i in range(cols_no):
    stacks.append([])
    for c in ci:
      crate_name = c[i*4+1]
      if crate_name.strip(): stacks[i].append(crate_name)

  return [i[::-1] for i in stacks]

def get_program(program_input):
  program = []
  for line in program_input:
    spl = line.split(' ')
    program.append([int(spl[1]), int(spl[3]) - 1, int(spl[5]) - 1])
  return program

def calc_result(stacks_result):
  return str.join('', [i[-1] for i in stacks_result])

def rearrange(stacks, program, reverse):
  for q, o, d in program:
    take = stacks[o][-q:]
    if reverse: take.reverse()
    del stacks[o][-q:]
    stacks[d].extend(take)
  return stacks

with open('input.txt') as f:
  crate_input, program_input = f.read().split('\n\n')

  stacks = get_stacks(crate_input.splitlines())
  program = get_program(program_input.splitlines())
  
  stacks_result_one = rearrange(copy.deepcopy(stacks), program, True)
  stacks_result_two = rearrange(copy.deepcopy(stacks), program, False)
  
  print(calc_result(stacks_result_one))
  print(calc_result(stacks_result_two))  

