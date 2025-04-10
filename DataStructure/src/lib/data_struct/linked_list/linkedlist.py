class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.root = None

  # O(N), Ω(1), Θ(n)
  def add(self, v):
    if not self.root:
      self.root = Node(v)
      return
    curr = self.root
    while curr.next:
      curr = curr.next
    curr.next = Node(v)

  # O(N), Ω(1), Θ(n)
  def get(self, index):
    if not self.root:
      return None
    i = 0
    curr = self.root
    while curr:
      if i == index:
        return curr.val
      curr = curr.next
      i += 1
    return None
  
  # O(1), Ω(1), Θ(1)
  def appendLeft(self, v):
    n = Node(v)
    n.next = self.root
    self.root = n

if __name__ == "__main__":
  lst = LinkedList()
  lst.add(1)
  lst.add(2)
  lst.add(3)
  lst.appendLeft(0)
  