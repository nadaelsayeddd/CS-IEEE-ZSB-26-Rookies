N, K = map(int, input().split())

def no_of_digits(n,k):

    counter = 0
    while n !=0:
        n = n // K
        if n >= 0:
            counter += 1
    return counter 
print(no_of_digits(N,K))



