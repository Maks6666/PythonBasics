list = ["ABCD", "EFGH", "KLMO", "OPRS"]

def choose():
    choosing_book = input("Choose an element ")

    if choosing_book in list:
        print(f"Element {choosing_book} is avaliable")
    else:
        print("Element is not avaliable")


def ap():

    appended_book = input("What element do u wanna to add? ")
    list.append(appended_book)
    list1 = " ".join(list)
    print(list1)

def ap2():

    while len(list) < 8:
        appended_book = input("What element do u wanna to add? ")
        list.append(appended_book)
        list1 = " ".join(list)
        print(list1)
    print("List is full")




def delate():
    list1 = " ".join(list)
    print(list1)


    x = int(input("How many elements do u want to delate? "))
    if x == 0:
        print(f"Thank you, {list1} is perfect")
    elif x >= 4:
        print("Sorry, it's too strict :(")
    else:

        while len(list) > x:
            delated_element = input("What element do u want do delate? ")
            if delated_element in list1:
                
                list.remove(delated_element)
                list1 = " ".join(list)
                print(list1)
            
            else:
                print(f"Element is not in list, try again from {list1}")
                
            
        else:
            print("Limit")








