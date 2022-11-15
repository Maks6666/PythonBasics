# #1
# y = int(input("y = "))
# x = int(input("x = "))
# def wehrmacht(x, y):
#     print(x + y)
# wehrmacht(x, y)
# 
# #2
# y = int(input("y = "))
# x = int(input("x = "))
# i = int(input("i = "))
# def Churchill(x, y, i):
#     print((x + y + i)/3)
# Churchill(x,y,i)

#3
# def ussr(x):
#     for i in x:
#         if i % 2 == 0:
#             print(i)
# lista = [2, 3, 4, 5, 6, 7]
# ussr(lista)
# 
# #4
# def reich(x):
#     for i in x:
#         if i % 2 > 0:
#             print(i)
# lista = [2, 3, 4, 5, 6, 7]
# reich(lista)
# 
# #5
# y = int(input("y = "))
# def usa(y):
#       print(y + 1)
# usa(y)

#6
# y = int(input("y = "))
# def stalin(y):
#      print(y + y * -2)
# stalin(y)

# 7
def btr(a):

    res1 = a[0]
    for i in a:
        if res1 < i:
            res1 = i
    return res1

lista1 = (1, 2, 3, 4, 5, 6)

print(btr(lista1))

def bmp(b):

    res2 = b[0]
    for p in b:
        if res2 > p:
            res2 = p
    return res2

lista2 = (1, 2, 3, 4, 5, 6)

print(bmp(lista2))


def mussolini(x):
    sum_x = 0
    for i in x:
        sum_x = sum_x + i           

    k = sum_x / len(x)
    return k

print("Keskiarvo on", mussolini([1, 2, 3, 4, 5, 6]))

# 8

def x(n):
    if n <= 1:
        return n
    else:
        return(x(n-1) + x(n - 2))
    
nterms = 20
for i in range(nterms):
    print(x(i))