lst = [5, 1, 3, 6]
sorted = True
while sorted:
  for i in range(len(lst) - 1):
    if lst[i + 1] < lst[i]:
      lst[i], lst[i + 1] = lst[i + 1], lst[i]
      sorted = False
print(lst)