t = int(input())
for i in range(t):
    n = int(input())
    a = b = c = -1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a = i
            break
    if a == -1:
        print("NO")
        continue
    rest = n // a
    for j in range(2, int(rest**0.5) + 1):
        if rest % j == 0 and j != a:
            b = j
            c = rest // j
            if c != a and c != b and c >= 2:
                break
            else:
                b = -1
    if b == -1:
        print("NO")
    else:
        print("YES")
        print(a, b, c)
 


