##############################
# Version itérative
##############################
def fibo_iter(n):
    if n==0:
        terme = 0
    elif n==1:
        terme = 1
    else :
        terme_precedent = 0
        terme = 1
        for i in range(2,n+1):
            tempo = terme
            terme = terme + terme_precedent
            terme_precedent = tempo
            #mieux mais plus spécifique Python
            #terme, terme_precent = terme + terme_precedent, terme
    return terme

























##############################
# Version récursive
##############################
def fibo_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo_rec(n-1)+fibo_rec(n-2)
































##############################
# Version dynamique (méthode ascendante)
##############################
def fibo_dyn(n):
    #tableau qui va stocker les résultats
    f = [0]*(n+1)
    if n > 0:
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-2] + f[i-1]
            #print(f)
    return f[n]































##############################
# Version dynamique récursive (méthode descendante)
##############################
def fibo(n):
    #tableau qui va stocker les résultats
    f = [None]*(n+1)
    return fibo_rec_dyn(n,f)

def fibo_rec_dyn(n,f):
    '''
    si tout va bien, la taille de tab est n+1
    '''
    if n<=1 :
        f[n] = n
    elif f[n] != None:
        return f[n]
    else :
        f[n] = fibo_rec_dyn(n-1,f) + fibo_rec_dyn(n-2,f)
    return f[n]






