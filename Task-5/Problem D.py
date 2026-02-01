import math
x = int(input())
answer_a = 1
answer_b = x
for i in range(int(x**0.5), 0, -1):
    if x % i == 0:
        a = i
        b = x // i
        if math.gcd(a, b) == 1:
            answer_a, answer_b = a, b
            break

print(answer_a, answer_b)