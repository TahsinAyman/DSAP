class Node:
  def __init__(self, val):
    self.val, self.next = val, set([])
  def next_data(self) -> list:
    return list(self.next)

def adjacency_list(data, directed=False):
  gr_dic = {}
  for k in data.keys():
    gr_dic[k] = Node(k)

  for k, v in data.items():
    for i in v:
      if not directed:
        gr_dic[i].next.add(gr_dic[k])
      gr_dic[k].next.add(gr_dic[i])
  return list(gr_dic.values())[0]

if __name__ == "__main__":
  graph = {'A': set(['B', 'C']),
          'B': set(['D', 'E']),
          'C': set(['A', 'F']),
          'D': set(['B']),
          'E': set(['B', 'F']),
          'F': set(['C', 'E'])}
  root = adjacency_list(graph)
  get_next = lambda n: list(map(lambda x: x.val, n.next))
