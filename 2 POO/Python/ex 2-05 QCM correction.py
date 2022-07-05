from random import randint

class QCM:
    def __init__(self,question,reponsesF,reponseV):
        """
        question : chaîne de caractères donnant la question
        reponsesF : tableau de réponses fausses de type string
        reponseV : la bonne réponse à la question
        place : emplacement de la bonne réponse, choisis aléatoirement
        """
        self.question = question
        self.reponsesF = reponsesF
        self.reponseV = reponseV
        self.place = randint(0,len(reponsesF))

    def affiche(self):
        """
        affiche la question et les propositions de réponses
        la réponse vraie est mise en poistion place
        """
        print("QUESTION :" , self.question)
        for i in range(len(self.reponsesF)+1) :
            if i<self.place :
                print("REPONSE",i,":",self.reponsesF[i])
            elif i==self.place :
                print("REPONSE",i,":",self.reponseV)
            else :
                print("REPONSE",i,":",self.reponsesF[i-1])

    def repondre(self):
        """
        renvoie vraie si l'élève répond juste
        """
        choix = int(input("D'après toi, petit scarabée, quelle est la bonne réponse ? \n"))
        if choix == self.place:
            print("Bravo ! Tu as gagné !")
            return True
        else :
            print("Il faudra un peu mieux m'écouter la prochaine fois !")
            return False



# pour tester la classe

if __name__ == "__main__" :
    questionUn = QCM(
        "Quelle est la propriété d'un tableau ?",
        ["il est routable", "il est moutarde", "il est jetable"],
        "il est mutable"
        )
    
    questionUn.affiche()
    questionUn.repondre()
