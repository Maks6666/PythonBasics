# 1.1
#Program which multiples random number by 10
# import random
# x = random.random() * 10
# print(x)


# # 1.2
#Program which multiples random number by 2 and subtracks 1 from it
# import random
# y = random.random() * 2 - 1
# print(y)

# # 1.3
#Program generates a random  number between 0 and 1 using special function and multiplies it by 100
# import random
# i = random.random() * 100
# print(i,"%")


# # 1.4
# import random
# Programm compares a number (0 or 1) given by user to random number and prints did user gues the right number or not
# p = random.random() * 1 #Choosing random number
# print(p) #Program prints it 
# x = int(input("Choose 0 or 1 ")) #Program assk user to input own number from 0 to 1
# if x == 0 and p < 0.5: #Program compares users answer to randomly generated number and prints some text 
#     print("voitit")
# if x == 0 and p > 0.5:
#     print("hävisit")
# if x == 1 and p > 0.5:
#     print("voitit")
# if x == 1 and p < 0.5:
#     print("hävisit")
# 


# # 2.1
#Program which chooses random number from 0 to 100
# import random
# t = random.randint(0,100)
# print(t)



# # 2.2
#Program which compare random number (from 1 to 6) to 6 and in dependence to was randomly generated number equal to 6 it prints some text 
# import random
# t = random.randint(1,6)
# if t == 6:
#     print("voitit")
# else:
#     print("hävisit")
# # print(t)


# # 2.3
#Program which asks user to input number, multiples it to random value from 1 to 6 and until generated number smaller than 100, program adds to it random number from 1 to 6
# import random #Program imports random library 
# x = int(input("X = ")) #User inputs any number
# a = random.randint(1,6) #Program chooses any number from 1 to 6 
# b = 0 #Variblr "b" is equal to 0. Its going to be number of each adding operation 
# # print(a) 
# w = a * x #New variable "w" created by multipling "a" to "x"
# while w < 100: #While variable "w" is smaller than 100, program will add to it random number from 1 to 6 and print it 
#     print(w)
#     print("Kerta:", b)
#     w += random.randint(1,6)
# #     w *= random.randint(1,6)
#     b += 1 #Program changes operation number from 0 to 1, from 1 to 2 and etc.
# if w == 100:
#     print("Stop") #When generated number is bigger than 100, program stops
#

#Program which generates random numbers for 2 players in turn and add to them another random values. When generated number is bigger than 10, 1st player wins, if it is smaller than -10, second player wins
# import random
# x = 0
# w = 0
# if input == "a":
#     x += (-6,6)
# if input == "b":
#         x += (-6,6)
# while x < 10 and x > -10:
#     print(x)
#     x += random.randint(-6,6)
#     w *= random.randint(1,6)
# if x >= 10:
#     print("Peläjä 2 voitti")
# if x <=-10:
#     print("Peläjä 1 voitti")





# 3.1
#Program choose random later form present list 
# import random
# lista = ["A", "B", "C", "D", "E"]
# x = random.choice(lista)
# print(x)


# 3.2
#Program removes a random later from the list until there lefts just one 1
# import random
# lista = ["A", "B", "C", "D", "E"]
# while len(lista) >= 1:
#     lista.remove(random.choice(lista))
#     print(lista)



# 3.3
#Program creates two lists and append both of them by random numbers until in the second generates number 7
import random
lista1 = [] #First list creating 
lista2 = [] #Second list creating
y = 0 #New variable 
for i in range(1,101): #Random numbers generating, appending them to the first list 
    lista1.append(i)
print(lista1)
while 7 not in lista2: #When number 7 generates in second list prosess stops
    num = random.choice(lista1)
    lista1.append(num)
    lista2.append(num)
    y +=1
print(lista2)
print("Määrä on ", y) #Program count an ammount of generated numbers 
