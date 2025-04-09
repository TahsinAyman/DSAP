import numpy as np
from lib.data_struct.linked_list.linkedlist import Node

class Hash:
  def __init__(self, val):
    self.val = val

  def hash(self):
    if type(self.val) == type(str()):
      return int("".join([str(ord(i)) for i in self.val]))
    else:
      return self.val
    # expecting only integer and string.
    # use hashing algorithm for other data structure

class HashTable:
  def __init__(self, load_factor = 10):
    self.arr = [0] * load_factor
    self.load_factor = load_factor

  def add(self, key: Hash, value):
    i = key.hash() % self.load_factor
    if self.arr[i] == 0:
      self.arr[i] = Node((key.val, value))
    else:
      tmp = self.arr[i]
      n = Node((key.val, value))
      n.next = tmp
      self.arr[i] = n
  
  def get(self, key: Hash):
    i = key.hash() % self.load_factor
    curr = self.arr[i]
    while curr:
      if key.val == curr.val[0]:
        return curr.val[1]
      curr = curr.next
    return None

if __name__ == "__main__":
  hashTable = HashTable()
  hashTable.add(Hash("tahsin"), 2)
  print(hashTable.get(Hash("tahsin")))