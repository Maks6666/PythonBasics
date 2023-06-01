def HasEnoughtMana(Manapool, cost):
    #Laskee numeroiden määrä
    NumeroSymboleita = 0
    for i in range(len(cost)):
        if cost[i].isdigit() == True:
            
            NumeroSymboleita += 1
        #print( NumeroSymboleita)
            
    #Määrittele numerollisemn hinnan ja värillisen hinnan
            
    Neutraalihinta = 0
    if Neutraalihinta > 0:
    
    
        Neutraalihinta = cost[0:NumeroSymboleita]
        Neutraalihinta = int(Neutraalihinta)
    Värihintä = list(cost[NumeroSymboleita:])
 
    
    
    
    print(Värihintä)
    #Onko hintä maksettavissa.
    
    for i in range (len(Värihintä)):
        if Värihintä[i] in Manapool:
            Manapool = Manapool.replace(Värihintä[i], "",1)
            
        else:
            return False
        #Tarkistaa neutraalin manan
        
    if len(Manapool) < Neutraalihinta:
        return False
    return True
        
        

print (HasEnoughtMana("RGUBWC", "11RG"))
print (HasEnoughtMana("WWBB", "WWW"))
print (HasEnoughtMana("RRR", "3"))
print (HasEnoughtMana("RGG", "RRG"))
