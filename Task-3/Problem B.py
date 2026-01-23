n, k = map(int, input().split())

r = list(map(int, input().split()))

for i in range(1, 2 * n, 2):
    if k > 0:
        if r[i] - 1 > r[i-1] and r[i] - 1 > r[i+1]:
            r[i] -= 1
            k -= 1

print(*(r))
