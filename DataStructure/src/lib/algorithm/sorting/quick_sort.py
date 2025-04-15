def rec_asc(left, right, lst):
  if len(lst[left + 1: right]) <= 1:
    return lst[left + 1: right]
  start, end = left, right
  pivot = lst[left + 1]
  while True:
    while True:
      left += 1
      if lst[left] >= pivot:
        break
    while True:
      right -= 1
      if lst[right] <= pivot:
        break
    if left > right or right == start + 1 or left == end - 1:
      break
    lst[left], lst[right] = lst[right], lst[left]
  res = []
  if left == right:
    for i in rec_asc(start, left + 1, lst):
      res.append(i)
    for y in rec_asc(left, end, lst):
      res.append(y)
  else:
    for i in rec_asc(start, left, lst):
      res.append(i)
    for y in rec_asc(left - 1, end, lst):
      res.append(y)
  return res

def rec_desc(left, right, lst):
  if len(lst[left + 1: right]) <= 1:
    return lst[left + 1: right]
  start, end = left, right
  pivot = lst[left + 1]
  while True:
    while True:
      left += 1
      if lst[left] <= pivot:
        break
    while True:
      right -= 1
      if lst[right] >= pivot:
        break
    if left > right or right == start + 1 or left == end - 1:
      break
    lst[left], lst[right] = lst[right], lst[left]
  res = []
  if left == right:
    for i in rec_desc(start, left + 1, lst):
      res.append(i)
    for y in rec_desc(left, end, lst):
      res.append(y)
  else:
    for i in rec_desc(start, left, lst):
      res.append(i)
    for y in rec_desc(left - 1, end, lst):
      res.append(y)
  return res

def quick_sort(l: list, inplace = False, asc = True):
  lst = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  if asc:
    return rec_asc(-1, len(lst), lst)
  else:
    return rec_desc(-1, len(lst), lst)

if __name__ == '__main__':
  lst = [1, 2, 3, 4, 5]
  res = quick_sort(lst, asc=False)
  print(res)
