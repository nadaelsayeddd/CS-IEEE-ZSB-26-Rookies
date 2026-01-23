X, Y = input().split()

def balance(x,y):
    return (y-0.5-x) if x+.5 <= y and x%5==0 else y

print(f"{balance(int(X),float(Y)):.2f}")