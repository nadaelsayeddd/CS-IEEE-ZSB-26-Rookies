# problem D 
t = int(input())
lst = []

for tst in range(t):
    description = input().rsplit(' ')
    for n in description:
        lst.append(int(n))
        lst.sort()
    if lst[-1] == lst[0] + lst[1]:
        print("Yes")
    else:
        print("NO")
    lst.clear()