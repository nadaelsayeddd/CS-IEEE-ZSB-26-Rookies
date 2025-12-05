# problem F
t = int(input())

for r in range(t):
    stick = input().rsplit(" ")
    if len(set(stick)) == 1:
        print("YES")
    else:
        print("NO")




