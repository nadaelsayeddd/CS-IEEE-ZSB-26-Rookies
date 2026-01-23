a, b = map(int, input().split())

def concatenation(string,digit):
    concat = str(string) * digit
    return concat
concat_a = concatenation(a,b)
concat_b = concatenation(b,a)
x = 0 

for i in range(9):
    if concat_a[x] < concat_b[x]:
        concat = concat_a
        break
    else:
        concat = concat_b
        break
    x += 1
print(concat)


