class MaxHeap:
  def __init__(self):
    self.heap = []
    self.m = None

  def add_many(self, lst):
    for i in lst:
      self.add(i)

  def define_min(self, i):
    if not self.m:
      self.m = i
    if self.heap[i] < self.heap[self.m]:
      self.m = i

  def add(self, val):
    self.heap.append(val)
    i = len(self.heap) - 1
    while i != 0:
      parent_index = (i - 1) // 2
      if val > self.heap[parent_index]:
        self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
        i = parent_index
      else:
        break
  
  def remove(self, i):
    self.heap[i] = self.heap[-1]
    li, ri = 0, 0
    while True:
      li = 2 * i + 1
      ri = li + 1
      if (li > len(self.heap) - 1 or ri > len(self.heap) - 1):
        break
      if self.heap[li] > self.heap[ri]:
        self.heap[li], self.heap[i] = self.heap[i], self.heap[li]
        i = li
      else:
        self.heap[ri], self.heap[i] = self.heap[i], self.heap[ri]
        i = ri
      
    self.heap.pop(-1)
  
  def pop(self):
    if len(self.heap) == 0:
      return None
    tmp = self.heap[0]
    self.remove(0)
    return tmp

if __name__ == "__main__":
  heap = MaxHeap()
  heap.add_many([6, 7, 5, 4, 3, 2, 1])
  heap.pop()
  print(heap.heap)