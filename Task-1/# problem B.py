# problem B
w = int(input())
def is_even(weight):
    return 'YES' if weight%2 == 0 and weight > 2 else 'NO'
print(is_even(w))
