class Node:
  def __init__(self, val):
    self.val, self.next = val, set([])
  def next_data(self) -> list:
    return list(self.next)

def adjacency_matrix(nodes, matrix, directed=False):
  gr_dic = {}
  for k in nodes:
    gr_dic[k] = Node(k)
  for i in range(len(nodes)):
    for y in range(len(nodes)):
      if matrix[i][y] == 1:
        gr_dic[nodes[i]].next.add(gr_dic[nodes[y]])
        if not directed:
          gr_dic[nodes[y]].next.add(gr_dic[nodes[i]])
  return gr_dic


if __name__ == "__main__":
  nodes = ['A', 'B', 'C', 'D']
  adj_matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
  ]
  gr_dic = adjacency_matrix(nodes, adj_matrix)
  get_next = lambda n: list(map(lambda x: x.val, n.next))
  
