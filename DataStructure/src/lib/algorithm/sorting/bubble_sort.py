# O(n^2)
def bubble_sort(l: list, inplace: bool = False, asc = True):
  global cnt
  lst = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  swapped = True
  while swapped:
    swapped = False
    if asc:
      for i in range(len(lst) - 1):
        if lst[i + 1] < lst[i]:
          lst[i], lst[i + 1] = lst[i + 1], lst[i]
          swapped = True
    else:
      for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
          lst[i], lst[i + 1] = lst[i + 1], lst[i]
          swapped = True
  return lst

if __name__ == "__main__":
  lst = [12,32,543,67,235,7,23,51,74,215,73,15,73,154,51,37,9]
  print(bubble_sort(lst))