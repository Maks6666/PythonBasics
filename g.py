#Mana-game 
# def HasEnoughtMana(Manapool, cost):
#     #Program counts amount of numbers 
#     NumeroSymboleita = 0
#     for i in range(len(cost)):
#         if cost[i].isdigit() == True:
            
#             NumeroSymboleita += 1
#         #print( NumeroSymboleita)
            
#     #Define a more numerical price and a colored price 
            
#     Neutraalihinta = 0
#     if Neutraalihinta > 0:
    
    
#         Neutraalihinta = cost[0:NumeroSymboleita]
#         Neutraalihinta = int(Neutraalihinta)
#     Värihintä = list(cost[NumeroSymboleita:])
 
    
    
    
#     print(Värihintä)
#     #Program checks does price payable
    
#     for i in range (len(Värihintä)):
#         if Värihintä[i] in Manapool:
#             Manapool = Manapool.replace(Värihintä[i], "",1)
            
#         else:
#             return False
#         #Program checks neutrals "Mana"s
        
#     if len(Manapool) < Neutraalihinta:
#         return False
#     return True
        
    #Program gives a game result    

# print (HasEnoughtMana("RGUBWC", "11RG"))
# print (HasEnoughtMana("WWBB", "WWW"))
# print (HasEnoughtMana("RRR", "3"))
# print (HasEnoughtMana("RGG", "RRG"))
