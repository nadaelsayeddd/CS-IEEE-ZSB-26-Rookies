q = int(input())
for _ in range(q):
    n = int(input())
    s, t = input().split()
    if ''.join(sorted(s)) == ''.join(sorted(t)):
        print("YES")
    else:
        print("NO")



    

    