def puissance(x,n):
    if n == 1 :
        return x
    elif n%2 == 0:
        return puissance(x*x, n//2)
    else :
        return x*puissance(x*x, (n-1)//2)

def fermat(n):
    return puissance(2,puissance(2,n))+1