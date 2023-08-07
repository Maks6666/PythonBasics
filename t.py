

#ID number check programm
# def tarkista_tilinumero(tilinumero): #Function creating     
    
#     tilinumero = tilinumero.replace(" ", "") #Programm deletes all enters
#     if len(tilinumero) != 18: #If ID number contains less than 18 numbers, programm returns false value
#         return False

    
#     tilinumero = tilinumero[4:] + tilinumero[:4] #Programm arranges numbers in correct order 

    
#     tilinumero = "".join(str(ord(c) - 55) if c.isalpha() else c for c in tilinumero) #Programm turns laters into numbers 

    
#     jakojäännös = int(tilinumero) % 97
#     return jakojäännös == 1 #Programm checks is modified ID number devide to 97



# tilinumero = input("Anna tilinumerosi") #User input some numbers in random way 
# print(tilinumero)
# if tarkista_tilinumero(tilinumero):
#     print("Tilinumerosi on aito.") #If ID number exists, programm gives such text
# else:
#     print("Tilinumerosi ei ole aito.")  #If ID number doesnt exist, programm gives such text

