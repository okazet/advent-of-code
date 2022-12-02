with open('input.txt', 'r') as input_file:
  # initialize a variable to keep track of the maximum number of Calories
  max_calories = 0

  # initialize a variable to keep track of the current Elf's Calories
  elf_calories = 0

  # read the input line by line
  for line in input_file:
    # strip leading and trailing whitespace from the line
    line = line.strip()

    # if the line is blank, then we are starting a new Elf's inventory
    if line == '':
      # update the maximum number of Calories if the current Elf has more than the previous Elf
      if elf_calories > max_calories:
        max_calories = elf_calories

      # reset the current Elf's Calories to 0
      elf_calories = 0
    else:
      # if the line is not blank, then it contains the number of Calories for a food item
      # add the Calories to the current Elf's total
      elf_calories += int(line)

  # after reading all of the lines, we need to check if the final Elf has more Calories than the previous Elves
  if elf_calories > max_calories:
    max_calories = elf_calories

  # print the maximum number of Calories carried by a single Elf
  print(max_calories)
