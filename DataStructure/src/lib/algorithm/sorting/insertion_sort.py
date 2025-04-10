
def insertion_sort(l: list, inplace: bool = False, asc = True):
  lst = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  for i in range(len(lst) - 1):
    ki = i + 1
    if asc:
      for y in range(i, -1, -1):
        if lst[ki] > lst[y]:
          break
        lst[y], lst[ki] = lst[ki], lst[y]
        ki = y
    else:
      for y in range(i, -1, -1):
        if lst[ki] < lst[y]:
          break
        lst[y], lst[ki] = lst[ki], lst[y]
        ki = y
  return lst

if __name__ == "__main__":
  lst = [1, 6, 3, 2, 5, 5]
  print(insertion_sort(lst))

  