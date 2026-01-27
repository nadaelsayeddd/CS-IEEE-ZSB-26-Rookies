n = int(input())
x = list(map(int, input().split()))


def calculation(i, summation1, summation2):
    if i == n:
        return abs(summation1 - summation2)
    
    
    return min(calculation(i+1, summation1+x[i], summation2), calculation(i+1, summation1, summation2+x[i]))


print(calculation(0, 0, 0))

