class File :
    def __init__(self):
        self.data = []
        
    def est_vide(self):
        return self.data == []
    
    def enfiler(self, valeur):
        self.data.append(valeur)
    
    def defiler(self):
        assert self.data != [], "file Vide !"
        return self.data.pop(0)
        
    def tete(self):
        assert self.data != [], "file Vide !"
        return self.data[0]
    
    def __str__(self):
        if self.data == []:
            affichage = ">>"
        else :
            affichage = str(self.data[0]) +'>'
            for i in range(1,len(self.data)):
                affichage = str(self.data[i]) + '_' + affichage
            affichage = '>' + affichage
        return affichage
    
    def __len__(self):
        return len(self.data)
    
    def renverser(self):
        self.data = [self.data[-i-1] for i in range(len(self.data))]
        
        
if __name__ == "__main__" :
    ma_file = File()
    
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")
    
    ma_file.enfiler(1)
    print("on emfile 1")
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")
    
    ma_file.enfiler(2)
    print("on emfile 2")
    print(ma_file)
    ma_file.defiler()
    print("on défile")
    print(ma_file, "\n")
    
    print("on emfile 3 puis 4 puis 5")
    ma_file.enfiler(3)
    ma_file.enfiler(4)
    ma_file.enfiler(5)
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file))
    print("le premier élément de la file est ", ma_file.tete(), "\n")
    
    print("on renverse la file")
    ma_file.renverser()
    print(ma_file, "\n")
    
    print("on défile deux fois")
    ma_file.defiler()
    ma_file.defiler()
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")