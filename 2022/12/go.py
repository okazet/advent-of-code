import numpy as np

def get_height(node_type):
  if node_type == 'S': return 0
  elif node_type == 'E': return 27
  else: return ord(node_type) - 96

def get_next_coords(point_coords, x_size, y_size):
  base = np.array(point_coords)
  possibilities = [base + direction for direction in [[0,1], [1,0], [0,-1], [-1,0]]]
  validate_coords = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < y_size and p[1] < x_size
  return [tuple(p) for p in filter(validate_coords, possibilities)]

def find_path(input):
  y_ax_size = len(input)
  x_ax_size = len(input[0])

  h_map = np.array([get_height(node) for node in np.ravel(input)]).reshape((y_ax_size,x_ax_size))
  markers = np.zeros(input.shape, int)

  start_point = tuple(np.ravel(np.where(input == 'S')))
  end_point = tuple(np.ravel(np.where(input == 'E')))

  queue = [] 
  queue.append((start_point, 0, 0))

  while queue:
    point_coords, path_len, origin_height = queue.pop(0)

    # been there
    if markers[point_coords]: continue

    # too high
    if h_map[point_coords] - origin_height > 1: continue

    # mark
    markers[point_coords] = path_len

    # end
    if point_coords == end_point:
      return path_len
      break

    # try next steps
    for next_point in get_next_coords(point_coords, x_ax_size, y_ax_size):
      queue.append((next_point, path_len + 1, h_map[point_coords]))

  return 0  

def find_shortest_path(input):
  start_point = tuple(np.ravel(np.where(input == 'S')))
  a_points = list(zip(*np.where(input == 'a')))
  starting_points = [start_point] + a_points
  input[start_point] = 'a'

  result = []
  for point in starting_points:
    input_copy = np.array(input)
    input_copy[point] = 'S'
    path_len = find_path(input_copy)
    if path_len > 0: result.append(path_len)

  return min(result) - 1

with open('input.txt') as f:
  input = np.array([[*line] for line in f.read().splitlines()])

  print('part 1:', find_path(input))
  print('part 2:', find_shortest_path(input))