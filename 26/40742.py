f = open('40742.txt')
f.readline()
start_time = 1633305600
end_time = start_time + 604800
proc = [0] * 604800
count = 0
for line in f:
    start, end = map(int, line.split())
    if start_time <= start <= end_time:
        proc[start - start_time] += 1
    if start_time <= end <= end_time:
        proc[end - start_time] -= 1
    if start < start_time and (end > start_time or end == 0):
        count += 1
max_count = 0
sum = 0

for p in proc:
    count += p
    if count > max_count:
        max_count = count
        sum = 0
    if count == max_count:
        sum += 1
print(max_count, sum)
