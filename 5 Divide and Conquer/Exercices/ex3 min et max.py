#####################################################
# méthode classique
#####################################################

def min_et_max(T):
    taille = len(T)
    mini = T[0]
    maxi = T[0]
    for i in range(1,taille):
        if T[i] < mini :
            mini = T[i]
        if T[i] > maxi :
            maxi = T[i]
    return mini, maxi


#####################################################
# méthode diviser pour régner
####################################################

def min_et_max2(T):
    if len(T) == 1:
        mini, maxi = T[0], T[0]
    elif len(T) == 2:
        if T[0] < T[1]:
            mini, maxi = T[0], T[1]
        else :
            mini, maxi = T[1], T[0]
    else :
        med = len(T)//2
        mini1, maxi1 = min_et_max2(T[:med])
        mini2, maxi2 = min_et_max2(T[med:])
        mini, maxi = min(mini1,mini2), max(maxi1,maxi2)
    return mini, maxi


L = [9, 1, 6, 5, 15, 11, 12, 14, 13, 4, 3, 8, 7, 10, 2]
print(min_et_max(L))
print(min_et_max2(L))
