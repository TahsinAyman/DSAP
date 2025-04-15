from lib.data_struct.heap.min_heap import MinHeap
from lib.data_struct.heap.max_heap import MaxHeap

def heap_sort(l: list, inplace = False, asc = True):
  lst = []
  result = []
  if not inplace:
    lst = l.copy()
  else:
    lst = l
  heap = None
  if asc:
    heap = MinHeap()
  else:
    heap = MaxHeap()
  heap.add_many(lst)
  v = heap.pop()
  while v:
    result.append(v)
    v = heap.pop()
  return result


if __name__ == "__main__":
  lst = [5, 3, 4, 2, 1]
  print(heap_sort(lst, asc=False))