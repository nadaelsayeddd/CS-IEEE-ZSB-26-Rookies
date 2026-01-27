N = int(input())

def calculation(k):
    if k > 0 and k <= 10:
        result = k * calculation(k-1)
    elif k == 0:
        result = 1
    else:
        raise "Value Error"
    return result 

print(calculation(N))



