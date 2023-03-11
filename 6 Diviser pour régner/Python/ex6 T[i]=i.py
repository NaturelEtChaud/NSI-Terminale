def indice(T):
    solutions = []
    indice_rec(T,0,len(T)-1,solutions)
    return sorted(solutions)


def indice_rec(T,premier_indice,dernier_indice,solutions):
    if premier_indice == dernier_indice:
        if T[premier_indice] == premier_indice:
            solutions.append(premier_indice)
    else :
        if T[premier_indice] <= dernier_indice :
            #il y a peut-être une solution
            med = (premier_indice + dernier_indice)//2
            if T[med] == med :
                solutions.append(med)
            indice_rec(T,premier_indice,med-1,solutions)
            indice_rec(T,med+1,dernier_indice,solutions)


T = [0, 2, 2, 5, 8, 12, 13, 15, 19, 26, 27]
print(indice(T))