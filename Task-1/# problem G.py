# problem G
# minimum no of shovels = x
# price = k
# total price = x * k

k, r = map(int, input().split())

x = 1


while True:
    total_price = x * k
    if str(total_price).endswith(f'{r}') or str(total_price).endswith('0'):
        print(x)
        break
    x += 1
    

