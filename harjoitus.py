# kissa = 5
# print(kissa)
# kissa = 7
# print(kissa)
# 
# nimi = "miisu"
# print(nimi)
# 
# koira = 6
# aasi = "6"
# 
# print(koira + koira)
# print(aasi + aasi)
# 
# kokonaisluku = 1 #int
# desimaaliluku = 2.3 # float, double



# lassi = 16
# olavi = 16
# 
# if False:
#     print("ne ovat saman ikäisiä")
# 
# print(lassi == olavi)

# if lassi < olavi:
# #     print("a")
# if lassi == olavi:
#     print("b")
#
    
    
    
    
    
    
    
    
    
    
    
    
    # == yhtäsuurikuin
# != erisuurikuin



# asiakas = 19
# if asiakas >= 18:
#     print("Täysi-ikäistä tervehditään")
# else:
#     print("Äläikäinen keskitään poistumaan ")
    
#Toisto lause - loop
    


# 
# for i in range(1, 11):
#     print(3 *i)
 
# silakka = 10
# while silakka > 0:
#     print(silakka)
#     silakka -=1
# if silakka == 0:
#     print("pitää ostaa lisää silakoita")
# 
# 
# if False:
#     print("true")
#     print("Miisu")
# print("false")
# 
# 
# 
# 
# # def Tiikkeri():
# #     print("Tiikkeri")
# #     print("Bengaliniikkeri")
# #     print("Tiikkerintaistelu")
# # Tiikkeri()  #funktion kutsu
# # 
# # def YhdenIsompi(luku):
# #     print(luku + 1)
# #     
# # YhdenIsompi(5)
# # 
# # 
# # 
# # 
# # def YhdenPienempi(luku):
# #     return luku - 1
# # YhdenPienempi(15)
# # hevonen = YhdenPienempi(15)
# # print(hevonen)
# # muuli = YhdenPienempi(-100)
# # print(muuli)
# 
# # x = int(input("X = "))
# # def numero(luku):
# #     if luku > 100:
# #         return luku - 100
# #     if luku < 100:
# #         return 100 - luku
# #     if luku == 100:
# #         return 0
# #     
# # y = numero(101)
# # print(y)
# # y = numero(200)
# # print(y)
# # 
# # 
# # 
# # 
# # 
# # def eta(luku):
# #     tulos = 100 - luku
# #     
# #     
# # 
# # 
# # arvosana1 = 1
# # arvosana2 = 5
# # arvosana = [1,5,4,3,5,8,5,3,2,5]
# # print(arvosana)
# # print(arvosana[1])
# # print(arvosana[0])
# # 
# # # len(arvosana) - 9
# # for i in range (len(arvosana)):
# print(arvosana[i])


# # 1
x = 0
while x < 20:
      x +=1
      print(x)
   
# 2
y = 9
while y < 20:
      y +=1
      print(y)
     
# 3
p = 101
while p > 10:
      p -=1
      print(p)
 
# 
# # 4
l = -1
while l < 9:
     l +=2
     print(l)
    
#5

lista = ["banaani", "apelsiini", "meloni", "omena", "mandariini"]
for i in range(len(lista)):
     print(lista[i])   #VÄLI

# 6

lista2 = [13, 34, 43, 12, 98, 2]
for i in range(len(lista2)):
    if lista2[i] <= 18:
        print("alaikäinen")
    else:
        print("täysi-ikäinen")
        
        
# toinen tapa 
# if lista2[0] >= 18:
#     print("alaikäinen")
# else:
#     print("täysi-ikäinen")
#     
#     if lista2[1] >= 18:
#         print("alaikäinen")
#     
#      else:
#     print("täysi-ikäinen")
#     
#     if lista2[2] >= 18:
#     print("alaikäinen")
# else:
#     print("täysi-ikäinen")
#     
#     if lista2[3] >= 18:
#     print("alaikäinen")
# else:
#     print("täysi-ikäinen")
#     if lista2[4] >= 18:
#     print("alaikäinen")
# else:
#     print("täysi-ikäinen")
#     if lista2[5] >= 18:
#     print("alaikäinen")
# else:
#     print("täysi-ikäinen")
# 
# 
# # 7
     
for i in range (5, 51, 5):
    print(i)
#8
lista3 = ["Jack", "Addie", "Chaffi", "Tom", "Spikey"]
lista3.reverse()
for q in range(len(lista3)):
    print(lista3[q])