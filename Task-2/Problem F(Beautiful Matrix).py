for row in range(5):
    line = input().split()
    
    for col in range(5):
        if line[col] == "1":
            r = row
            c = col

steps = abs(r - 2) + abs(c - 2)
print(steps)
