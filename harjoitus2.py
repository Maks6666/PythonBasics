# #1
#Summa calculator 
# y = int(input("y = ")) #User inputs fist number
# x = int(input("x = ")) #User inputs second number
# def _sum(x, y): #Function creating
#     print(x + y)
# _sum(x, y) #Function invitation 
# 
# #2
#Avarage number calculator 
# y = int(input("y = "))  #User inputs fist number
# x = int(input("x = "))  #User inputs second number
# i = int(input("i = "))  #User inputs third number
# def av(x, y, i): #Function creating
#     print((x + y + i)/3) #Calculation using avarageness formula
# av(x,y,i) #Function invitation 

#3
#Even numbers calculator from a list
# def even(x): #Function creating
#     for i in x:
#         if i % 2 == 0: #Programm calculates even numbers by division on 0
#             print(i)
# lista = [2, 3, 4, 5, 6, 7] #List, from which programm choose even numbers
# even(lista)  #Function invitation 
# 
# #4
##Odd numbers calculator from a list
# def odd(x):  #Function creating
#     for i in x:
#         if i % 2 > 0:  #Programm calculates even numbers by division on 0
#             print(i)
# lista = [2, 3, 4, 5, 6, 7]  #List, from which programm choose even numbers
# odd(lista) #Function invitation 
# 
# #5
#Programm, which increase users number by 1
# y = int(input("y = ")) #User inputs own number
# def function(y):  #Function creating
#       print(y + 1)
# function(y) #Function invitation 

#6
#Programm, which change users number value to oposite
# y = int(input("y = ")) #User inputs own number
# def oposite(y):  #Function creating
#      print(y + y * -2) #Result
# oposite(y) #Function invitation 


# # 7
#Programm, with 3 functions to calculate the smallest, the biggest and average value from a list
# def maximum(a):  #Function creating

#     res1 = a[0] #Choosing the first value from the list 
#     for i in a:
#         if res1 < i: #Comparing it to others
#             res1 = i
#     return res1 #Result returning

# lista1 = (1, 2, 3, 4, 5, 6) #The list 

# print(maximum(lista1)) #Function invitation and printing the result

# def minimum(b):  #Function creating


#     res2 = b[0] #Choosing the first value from the list 
#     for p in b:
#         if res2 > p:  #Comparing it to others
#             res2 = p
#     return res2  #Result returning 

# lista2 = (1, 2, 3, 4, 5, 6) #The list 

# print(minimum(lista2))  #Function invitation and printing the result



# def avarage(x): #Function creating
#     sum_x = 0 #Sum of numbers in list 
#     for i in x:
#         sum_x = sum_x + i   #Adding each element of the list to the sum

#     k = sum_x / len(x) #"K" is for avarage value, programm divides sum of each numbers in list by amount of numbers in list 
#     return k #Programm returns the average value 

# print("Avarage value is ", avarage([1, 2, 3, 4, 5, 6])) #Programm prints results 

# # 8
#Programm to calculate fibonacci numbers
# def x(n):  #Function creating
#     if n <= 1: #comprasion a variable to 1
#         return n #Result returning 
#     else:
#         return(x(n-1) + x(n - 2)) #Result returning if variable smaller than 1
    
# nterms = 20 #Second variable
# for i in range(nterms): 
#     print(x(i)) #Result printint
