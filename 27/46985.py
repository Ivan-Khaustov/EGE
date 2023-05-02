f = open('46985A.txt')
f.readline()
count = 0
sum_num = 0
mods = [0] * 1000
# Читаем напрямую из файла не нагружая оперативную память
for line in f:
    num = int(line)
    sum_num += num
    if sum_num % 999 == 0:
        count += 1
    count += mods[sum_num % 999]
    mods[sum_num % 999] += 1
print(count)
