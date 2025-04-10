# O(n^2)
def selection_sort(l: list, inplace = False, asc = True):
  lst = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  for i in range(len(lst)):
    m = i
    if asc:
      for y in range(i, len(lst)):
        if lst[y] < lst[m]:
          m = y
    else:
      for y in range(i, len(lst)):
        if lst[y] > lst[m]:
          m = y
    lst[i], lst[m] = lst[m], lst[i]
  return lst

if __name__ == "__main__":
  lst = [64, 25, 12, 22, 11]
  print(selection_sort(lst, ascending=False))
