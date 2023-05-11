f = open(r'6529B.txt')

n, m = map(int, f.readline().split())

vmest = m

first = int(f.readline())

s = []
k = 1
summa = first
count = 1
max_count = 0

s.append(first)

for i in range(n - 1):
    a = int(f.readline())

    if summa + a <= m:
        s.append(a)
        summa += a
        count += 1
        max_count = max(max_count, count)
    else:
        while summa + a > m:
            if k == len(s):
                s = []
                first = a
                count = 0
                k = 1
                summa = 0
                break

            summa -= first
            first = s[k]
            k += 1
            count -= 1

        summa += a
        s.append(a)
        count += 1

print(max_count)