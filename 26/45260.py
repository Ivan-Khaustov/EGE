f = open(r'45260.txt')

n = int(f.readline())
s = []

for i in range(n):
    a, b = map(int, f.readline().split())

    s.append([a, b])

s.sort()

print(s)

h = [0, 0]

for i in range(1, len(s)):
    if s[i - 1][0] == s[i][0]:
        if s[i][1] - s[i - 1][1] == 14:
            if s[i][0] > h[0]:
                h = [s[i][0], s[i - 1][1] + 1]

print(h)