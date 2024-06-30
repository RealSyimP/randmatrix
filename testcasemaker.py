import random
import numpy as np

h = random.randint(32, 256)
w = random.randint(32, 256)
grid1 = [[0 for i in range(w)]for j in range(h)]
grid2 = [[0 for i in range(w)]for j in range(h)]

for i in range(h):
  for j in range(w):
    p = random.randint(0, 3)
    grid1[i][j] = p

list = []
for i in range(h):
  for j in range(w):
    list.append(grid1[i][j])
random.shuffle(list)

k = 0
for i in range(h):
  for j in range(w):
    grid2[i][j] = list[k]
    k += 1

print(h, w)
for i in range(h):
  for j in range(w):
    print(grid1[i][j], end=' ')
  print()

for i in range(h):
  for j in range(w):
    print(grid2[i][j], end=' ')
  print()
