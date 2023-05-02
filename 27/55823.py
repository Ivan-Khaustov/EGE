f = open(r'55823B.txt')

n = int(f.readline())
k = int(f.readline())

s = []

for i in range(n):
    a = int(f.readline())

    s.append(a)

m1 = 0
m2 = 0

for i in range(k, len(s)):
    m1 = max(m1, s[i - k])
    m2 = max(m2, s[i] + m1)

print(m2)