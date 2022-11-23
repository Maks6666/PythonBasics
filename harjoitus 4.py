# 1.1
# import random
# x = random.random() * 10
# print(x)
# # 1.2
# import random
# y = random.random() * 2 - 1
# print(y)
# # 1.3
# import random
# i = random.random() * 100
# print(i,"%")
# # 1.4
# 
# import random
# p = random.random() * 1
# print(p)
# x = int(input("X = "))
# if x == 0 and p < 0.5:
#     print("voitit")
# if x == 0 and p > 0.5:
#     print("hävisit")
# if x == 1 and p > 0.5:
#     print("voitit")
# if x == 1 and p < 0.5:
#     print("hävisit")
# 
# # 2.1
# import random
# t = random.randint(0,100)
# print(t)
# # 2.2
# import random
# t = random.randint(1,6)
# if t == 6:
#     print("voitit")
# else:
#     print("hävisit")
# # print(t)
# # 2.3
# import random
# x = int(input("X = "))
# a = random.randint(1,6)
# b = 0
# # print(a)
# w = a * x
# while w < 100:
#     print(w)
#     print("Kerta:", b)
#     w += random.randint(1,6)
# #     w *= random.randint(1,6)
#     b += 1
# if w == 100:
#     print("Stop")
#     
# 2.4
# import random
# x = 0
# b = 0
# # if input == "a":
# #     x += (-6,6)
# # if input == "b":
# #     x += (-6,6)
# while x < 10 and x > -10: 
#     print(x)
#     x += random.randint(-6,6)
# #     w *= random.randint(1,6)
# if x >= 10:
#     print("Peläjä 2 voitti")
# if x <=-10:
#     print("Peläjä 1 voitti")
# 3.1
# import random
# lista = ["Hello Biden", "its Zelenskij", "we need five million rockets", "to bobm Donetsk children", "Slava Ukraine"]
# x = random.choice(lista)
# print(x)
# 3.2
# import random
# lista = ["Hello Biden", "its Zelenskij", "we need five million rockets", "to bobm Donetsk children", "Slava Ukraine"]
# while len(lista) >= 1:
#     lista.remove(random.choice(lista))
#     print(lista)
# 3.3
import random
lista1 = []
lista2 = []
y = 0
for i in range(1,101):
    lista1.append(i)
print(lista1)
while 7 not in lista2:
    num = random.choice(lista1)
    lista1.append(num)
    lista2.append(num)
    y +=1
print(lista2)
print("Määrä on ", y)
# for i in range(1,101)
# while lista2 != 7:
#     lista1.append for i in range(1,101)
# 
#     print(lista1)
#    
# if lista2 == 7:
#     print("stop")
# while lista2 != "7":
#     lista1 += lista1.append(x)
#     lista2 += lista2.append(x)
# if lista2 == "7":
#     print("stop")