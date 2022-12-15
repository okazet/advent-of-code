import numpy as np

def draw(image):
  for line in image:
    print(''.join(line))

def pad(arr, width = 2, sym = '.'):
  pad_with_zero = np.pad(arr, width)
  shape = pad_with_zero.shape
  flat = np.ravel(pad_with_zero)
  return np.array([(el if el != '0' else sym) for el in flat]).reshape(shape)

def process(image, algo):
  xsize = len(image[0])
  ysize = len(image)

  result = np.empty(shape=[xsize - 2, ysize - 2], dtype=str)

  for y in range(ysize - 2):
    for x in range(xsize - 2):
      slice3x3 = image[y:y+3,x:x+3]
      control = list(map(lambda x: '0' if x == '.' else '1', np.ravel(slice3x3)))
      algo_index = int(''.join(control), 2)
      decode = algo[algo_index]
      result[y,x] = decode

  return result

with open('input.txt') as f:
  algo, image = f.read().split('\n\n')
  image = np.array(list(map(list, image.split('\n'))))
  
  result = np.array(image)

  for i in range(2):
    result = process(pad(result, 2, '.' if i % 2 == 0 else '#'), algo)

  print('part 1:', sum(map(lambda x: 1 if x == '#' else 0, np.ravel(result))))

  result = np.array(image)

  for i in range(50):
    result = process(pad(result, 2, '.' if i % 2 == 0 else '#'), algo)

  print('part 2:', sum(map(lambda x: 1 if x == '#' else 0, np.ravel(result))))