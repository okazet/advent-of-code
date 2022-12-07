with open('input.txt') as f:
  commands = f.read().splitlines()

  def getPath(p,f):
    if len(p) == 1: return '/' + f
    return p[:1][0] + str.join('/',p[1:]) + '/' + f; 

  path = []
  files = {}
  dirs = set()
  for c in commands:
    if c.startswith('$ cd'):
      cd_name = c.split(' ')[-1]
      if cd_name == '/':
        path = ['/']
      elif cd_name == '..':
        path.pop()
      else:
        path.append(cd_name)
      dirs.add(getPath(path,''))
    elif c == '$ ls' or c.startswith('dir'): continue
    else: 
      size, filename = c.split(' ')
      abspath = getPath(path, filename)
      files[abspath] = int(size)
  
  smallest_folders_total = 0
  for fold in dirs:
    fold_total = sum([files[f] for f in files if f.startswith(fold)])
    if fold_total < 100000:
      smallest_folders_total += fold_total
  
  disk_usage = sum(files[f] for f in files)
  total_space = 70000000
  free_space = total_space - disk_usage
  require_space = 30000000
  need_to_free = require_space - free_space

  candidates = []
  for fold in dirs:
    total = sum([files[f] for f in files if f.startswith(fold)])
    if total > need_to_free: candidates.append(total)
  
  print('total of folders at most 100000:', smallest_folders_total)
  print('smallest folder to delete:', min(candidates))
