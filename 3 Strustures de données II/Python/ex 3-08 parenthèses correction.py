from TAD import Pile

def parenthese(expression):
    """
    Entrée :
        expression est une chaîne de caractères
    Sortie :
        un booléen, vrai si expression est bien parenthésées
    """
    # dictionnaire qui contient en clés toutes les parenthèses et pour valeurs
    # le complément du couple de parenthèse
    brackets = {'(':')', ')':'(', '[':']', ']':'[', '{':'}', '}':'{'}
    pile = Pile()
    # on lit tous les caractères de l'expression
    for i in range(len(expression)):
        # si c'est une parenthèse
        if expression[i] in brackets :
            # soit elle est le complément du sommet de la pile et on dépile
            if not pile.est_vide() and pile.sommet() == brackets[expression[i]] :
                pile.depiler()
            else :
                # sinon, on stocke dans la pile
                pile.empiler(expression[i])
            # pour voir la pile étape après étape
            print(pile)
    # si la pile est vide c'est que l'expression est bien parenthésée
    return pile.est_vide()

if __name__ == "__main__" :
    expression = '{ [ ( ) ( ) ] }'
    print(expression, 'est bien parenthésée', parenthese(expression), '\n')
    
    expression = '( [ ) ( ) ]'
    print(expression, 'est bien parenthésée', parenthese(expression), '\n')
    
    expression = '(3*(2-5x)+3)'
    print(expression, 'est bien parenthésée', parenthese(expression), '\n')
    
    expression = '(3*(2-5x)+3'
    print(expression, 'est bien parenthésée', parenthese(expression), '\n')