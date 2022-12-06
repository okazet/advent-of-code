with open('input.txt') as f:
  signal = f.read()

  for i in range(len(signal)-3):
    sample = set(signal[i:i+4])
    if len(sample) == 4: 
      print(i+4)
      break

  for i in range(len(signal)-13):
    sample = set(signal[i:i+14])
    if len(sample) == 14: 
      print(i+14)
      break