f = open(r'6638B.txt')

n = int(f.readline())

s = []

for i in range(n):
    a, b = map(int, f.readline().split())

    s.append([a, (b - 1) // 100 + 1])

summa = 0

for i in range(len(s)):
    summa += s[i][0] * s[i][1]

left_sum = 0
left_sum_one = 0
right_sum = summa - s[0][1] * s[0][0]
right_sum_one = 0

for i in range(1, len(s)):
    right_sum_one += s[i][1]

min_sum = left_sum + right_sum
min_number = s[0][0]

for i in range(1, len(s)):
    left_sum_one += s[i - 1][1]
    right_sum_one -= s[i][1]

    left_sum += left_sum_one * (s[i][0] - s[i - 1][0])
    right_sum -= right_sum_one * (s[i][0] - s[i - 1][0])

    if left_sum + right_sum < min_sum:
        min_sum = left_sum + right_sum
        min_number = s[i][0]

print(min_number)