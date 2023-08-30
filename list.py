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




def delete_elements():
    my_list = ["ABCD", "EFGH", "KLMO", "OPRS"]

    while True:
        try:
            x = int(input("Сколько элементов вы хотите удалить? Введите число: "))
            if x <= 0:
                print("Введите положительное число.")
            elif x >= len(my_list):
                print("Слишком большое число. Введите число меньше или равное", len(my_list) - 1)
            else:
                for _ in range(x):
                    deleted_element = input("Введите элемент для удаления: ")
                    if deleted_element in my_list:
                        my_list.remove(deleted_element)
                    else:
                        print("Элемент не найден в списке. Попробуйте снова.")
                
                print("Новый список после удаления:", my_list)

        except ValueError:
            print("Ошибка: Введите целое число.")
        except KeyboardInterrupt:
            print("\nПрограмма завершена.")
            break

delete_elements()








