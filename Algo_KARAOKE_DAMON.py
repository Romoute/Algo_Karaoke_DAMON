################################# PARTIE A #################################
### Class Player ###

class Player:

    def __init__(self, pseudo, scores):
        self.pseudo = pseudo
        self.scores = scores

  
    # Méthode qui renvoit au nouveau score du joueur
    def NouveauScore(self,newscore,songname):                 
        self.newscore=newscore
        self.song=songname
        
        
        if self.newscore>=self.scores[self.song]:                # Vérifie que le score qu'on veut ajouter n'est pas inférieur au score précédent      
            self.scores[self.song]=newscore
            print("Votre score est de ", self.scores[self.song])
        else:
            print("Vous n'avez pas battu votre score !")



    # Méthode qui renvoit au meilleur score du joueur
    def MeilleurScore(self):                                   
        BestScore=self.scores
        BestScoreSong=0
        
        
        for i in range(1,5):
            if self.scores[i-1]>=self.scores[i]:                       
                if self.scores[i-1]>BestScore:                
                    BestScore=self.scores[i-1]   
                                                       
            else:
                if self.scores[i]>BestScore:                                  
                    BestScore=self.scores[i]             
                    BestScoreSong=i
        print("Votre meilleur score est sur la chanson", BestScoreSong, " est ", BestScore) 
        
        
        
    # Méthode qui renvoit au pire score du joueur    
    def PireScore (self):                                
        WorstScore=self.scores
        WorstScoreSong=0
        
        
        for i in range(1,5):
            if self.scores[i-1]<=self.scores[i]:                           
                if self.scores[i-1]<WorstScore:                       
                    WorstScore=self.scores[i-1]  
                                                  
            else:
                if self.scores[i]<WorstScore:                     
                    WorstScore=self.scores[i]
                    WorstScoreSong=i                                    
        print("Votre meilleur score est sur la chanson", WorstScoreSong, " est " , WorstScore) 
     
    
    
    
    
    
### Getters ###

    def getPseudo(self):
        return self.pseudo
    
    def getScores(self):
        return self.scores
    
        

      
### PROGRAMME PRINCIPAL ###

# Ici j'initialise mes valeurs 


joueur1= Player ("JY", 60)
joueur2= Player ("Isabelle", 95)


joueur1.MeilleurScore() 
joueur2.MeilleurScore() 



################################# PARTIE B #################################
     
        
class Player:
    
    def __init__(self, pseudo, scores):    
        self.pseudo = pseudo 
        self.scores = scores
        
class Karaoke:
    
    def __init__(self, songs):            
        self.nbrechansons = songs
        
         
    def NomChanson(self, nom):
        self.nomChanson = nom
         
        print(self.nomChanson)     
        
          
          
### PROGRAMME PRINCIPAL ###

# Ici j'initialise mes valeurs 


   