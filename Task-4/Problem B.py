n = int(input())
lst = [n]
def calculation(k):
    
    if k%2 == 0 and k > 1 :
        result = k /2
        lst.append(int(result))
        calculation(result)
         
        
    elif k%2 != 0 and k > 1 :
        result = (k*3)+1
        lst.append(int(result))
        calculation(result)
    
    elif k == 1:
        result = 1
    return result
    
    



calculation(n)
print(*(lst))
