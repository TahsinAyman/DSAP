class Node:
  def __init__(self, val, next=None):
    self.val, self.next = val, next

data = {
  "A": ["B", "C"],
  "B": ['A', 'D', 'E'],
  "C": ['A', 'F'],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}
gr_dic = {}
for k in data.keys():
  gr_dic[k] = Node(k)

for k, v in data.items():
  gr_dic[k].next = list(map(lambda x: gr_dic[x], v))
