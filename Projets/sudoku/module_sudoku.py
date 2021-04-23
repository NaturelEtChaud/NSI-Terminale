def affiche(sud):
    for i in range(9):
        if i%3==0:
            print('-'*31)
        ligne =''
        for j in range(9):
            if j%3==0:
                ligne += '|'
            if sud[i][j]==None:
                ligne += '   '
            else :
                ligne += ' '+str(sud[i][j])+' '
        ligne += '|'
        print(ligne)
    print('-'*31)

def ligne(sud, numero):
    '''
    sud est une grille de sudoku
    numero est un entier entre 0 et 8 (on compte comme une machine)
    la fonction renvoie le nombre de case vide
    et un tableau contenant tous les chiffres manquants dans l'ordre croissant
    '''
    assert 0 <= numero <= 8, "attention, le numéro de la ligne est entre 0 et 8, comme une machine !"

    #tableau contenant toutes les valeurs présentes dans la ligne
    contient = [None]*9
    #nombre de None dans la ligne
    nb = 0
    for j in range(9):
        case = sud[numero][j]
        if case != None :
            contient[case-1]=case
        else :
            nb += 1
    #renvoie de la réponse
    if nb == 0:
        return 0, None
    else :
        reponse = []
        for i in range(9):
            if contient[i] == None:
                reponse.append(i+1)
        return nb, reponse

def colonne(sud, numero):
    '''
    sud est une grille de sudoku
    numero est un entier entre 0 et 8 (on compte comme une machine)
    la fonction renvoie le nombre de case vide
    et un tableau contenant tous les chiffres manquants dans l'ordre croissant
    '''
    assert 0 <= numero <= 8, "attention, le numéro de la colonne est entre 0 et 8, comme une machine !"

    #tableau contenant toutes les valeurs présentes dans la ligne
    contient = [None]*9
    #nombre de None dans la colonne
    nb = 0
    for i in range(9):
        case = sud[i][numero]
        if case != None :
            contient[case-1]=case
        else :
            nb += 1
    #renvoie de la réponse
    if nb == 0:
        return 0, None
    else :
        reponse = []
        for i in range(9):
            if contient[i] == None:
                reponse.append(i+1)
        return nb, reponse

def carre(sud, numero):
    '''
    sud est une grille de sudoku
    numero est un entier entre 0 et 8 (on compte comme une machine)
    la fonction renvoie le nombre de case vide
    et un tableau contenant tous les chiffres manquants dans l'ordre croissant
    '''
    assert 0 <= numero <= 8, "attention, le numéro du carré est entre 0 et 8, comme une machine !"

    #tableau contenant toutes les valeurs présentes dans la ligne
    contient = [None]*9
    #nombre de None dans la colonne
    nb = 0
    #ligne et colonne du carré
    ligne = numero//3
    colonne = numero%3

    for i in range(3):
        for j in range(3):
            case = sud[ligne*3+i][colonne*3+j]
            if case != None :
                contient[case-1]=case
            else :
                nb += 1
    #renvoie de la réponse
    if nb == 0:
        return 0, None
    else :
        reponse = []
        for i in range(9):
            if contient[i] == None:
                reponse.append(i+1)
        return nb, reponse