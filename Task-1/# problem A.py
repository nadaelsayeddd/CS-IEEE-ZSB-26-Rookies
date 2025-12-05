# problem A
n = int(input())
count = 0
no_of_solutions = 0
for sol in range(n):
    solution = input()
    for char in list(solution):
        if char == "1":
            count += 1
    if count >= 2 :
        no_of_solutions += 1
    count = 0
print(no_of_solutions)






            
