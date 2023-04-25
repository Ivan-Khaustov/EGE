f = open(r"26_6641.txt")

N, M = map(int, f.readline().split())

s = []
spisok_W = []

for i in range(N):
    a, b = map(str, f.readline().split())

    if b == "S":
        b = 0
    else:
        b = 1

    s.append([int(a), int(b)])

s.sort()

s_count = 0
count = 0
next_S = 0

for i in range(len(s)):
    if M >= int(s[i][0]):
        M = M - int(s[i][0])
        if s[i][1] == 0:
            s_count += 1
        if s[i][1] == 1:
            spisok_W.append(int(s[i][0]))
        count += 1
    else:
        k = -1
        for j in range(i, len(s)):
            if s[j][1] == 0:
                if spisok_W[k] + M >= int(s[j][0]):
                    M = M - (int(s[j][0]) - spisok_W[k])
                    s_count += 1
                    k -= 1
                else:
                    break
        break

print(s_count, M)