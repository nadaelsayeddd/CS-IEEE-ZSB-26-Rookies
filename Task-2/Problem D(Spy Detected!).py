t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

  
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            print(lst.index(lst[i]) + 1)
            i += 1