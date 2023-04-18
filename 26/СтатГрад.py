import re

f = open('СтатГрад.txt')
f.readline()
matrix = ["0" * 100001 for i in range(100001)]

for line in f:
    x, y = map(int, line.split())
    # Поменять в строке символ в позиции y
    matrix[x] = matrix[x][:y] + '1' + matrix[x][y + 1:]

max_lines = 0
pos = 0
for i in range(100001):
    items = re.split(r"[0]+", matrix[i])
    count = 0
    for s in items:
        if len(s) > 2:
            count += 1
    if count >= max_lines:
        max_lines = count
        pos = i
print(max_lines, pos)