import sys
input = sys.stdin.readline
max_n = 10**6
divsisors = [0] * (max_n + 1)

for i in range(1, max_n + 1):
    for j in range(i, max_n + 1, i):
        divsisors[j] += 1

n = int(input())
for i in range(n):
    x = int(input())
    print(divsisors[x])
