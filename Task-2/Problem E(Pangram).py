n = int(input())

s = input().lower()

lst = [char for char in s]

if len(set(lst)) == 26:
    print("YES")
else:
    print("NO")