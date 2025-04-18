def rec_asc(lst):
  if len(lst) <= 1:
    return lst
  half = len(lst) // 2
  l1 = rec_asc(lst[:half])
  l2 = rec_asc(lst[half:])
  p1, p2 = 0, 0
  res = []
  visited = [False, False]
  while True:
    if l1[p1] < l2[p2]:
      res.append(l1[p1])
      p1 += 1
    if p1 == len(l1):
      while p2 <= len(l2) - 1:
        res.append(l2[p2])
        p2 += 1
      break

    if l2[p2] < l1[p1]:
      res.append(l2[p2])
      p2 += 1
    if p2 == len(l2):
      while p1 <= len(l1) - 1:
        res.append(l1[p1])
        p1 += 1
      break
  return res
def rec_desc(lst):
  if len(lst) <= 1:
    return lst
  half = len(lst) // 2
  l1 = rec_desc(lst[:half])
  l2 = rec_desc(lst[half:])
  p1, p2 = 0, 0
  res = []
  while True:
    if l1[p1] > l2[p2]:
      res.append(l1[p1])
      p1 += 1
    if p1 == len(l1):
      while p2 <= len(l2) - 1:
        res.append(l2[p2])
        p2 += 1
      break

    if l2[p2] > l1[p1]:
      res.append(l2[p2])
      p2 += 1
    if p2 == len(l2):
      while p1 <= len(l1) - 1:
        res.append(l1[p1])
        p1 += 1
      break
  return res

def merge_sort(l: list, inplace = False, asc = True):
  lst = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  if asc:
    return rec_asc(lst) 
  return rec_desc(lst)

if __name__ == "__main__":
  lst = [10, 2, 9, 1, 8]
  print(merge_sort(lst))