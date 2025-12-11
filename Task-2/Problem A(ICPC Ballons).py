t = int(input())
output = 0
x = 0
for _ in range(t):
    n = int(input())
    s = input()
    lst = [char for char in s]
    unique = set(lst)
    
    for l in range(n):
        output += 1 
    for u in unique:
        x += 1
    result = output + x 
    print(result)
    result = 0
    output = 0
    x = 0


        
            


    
    