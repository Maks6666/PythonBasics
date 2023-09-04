# # my_tuple = (1, 2, 3)
# # print(my_tuple[1])

# for item in my_tuple:
#     print(item)
# # Вывод:
# # 1
# # 2
# 3

# cart = []

# while True:
#     product_name = input("Введите название продукта: ")
#     if product_name == "q":
#         break
#     product_price = int(input("Введите цену продукта: "))
#     product_ammount = int(input("Введите вес продукта (в граммах): "))

#     product_info = (product_name, product_price, product_ammount)
#     cart.append(product_info)

# print("\nИнформация о продуктах: ")
# for product in cart:
#     product_name, product_price, product_ammount = product
#     print(f"Название продукта: {product_name}, цена продукта: {product_price} долл. Количество продукта: {product_ammount} гр.")



# cost = []
# day_cost = []
# while True:
#     try:
#         hotel_cost = int(input("Сколько стоит отель ? "))
#         day_cost.append(hotel_cost)
        

#         ticket_cost = int(input("Сколько стоит билет? "))
#         day_cost.append(ticket_cost)

#         food_cost = int(input("Cколько стоит еда? "))
#         day_cost.append(food_cost)

#         total_cost = sum(day_cost)
        
#         cost_info = (hotel_cost, ticket_cost, food_cost, total_cost)
#         cost.append(cost_info)
#     except ValueError:
#         break

# print("\nЦена отдыха: ")
# for cost_fin_inf in cost: #создаем новую переменную cost_fin_inf, которая является составляющей наполненного списка "cost"
#     hotel_cost, ticket_cost, food_cost, ticket_cost = cost_fin_inf
#     print(f"Цена отеля: {hotel_cost}, Цена билетов: {ticket_cost}, Цена питания: {food_cost}, Oбщая цена: {total_cost}")


# students_info = []
# subjects = ["Math", "History", "P.E.", "Language"]

# while True:
#     try:
#         student_name = input(("Введите имя студента: "))

#         mark_list = []
       
#         for i in range(len(subjects)):
#                 sudent_mark = int(input(f"Введите оценки студента за {subjects[i]}: "))
#                 mark_list.append(sudent_mark)

#         average_mark = sum(mark_list) / len(mark_list)
        
        
#         personal_info = (student_name, mark_list, average_mark)
#         students_info.append(personal_info)
#     except ValueError:
#         break

# print("\n Информация о студентах: ")
# for person in students_info:
#     student_name, mark_list, average_mark = person
#     print(f"Имя студента: {student_name}, Оценки студента: {mark_list}, Средняя оценка: {average_mark}")


#transactions = [
#     ("расход", 500, "Покупка продуктов в магазине"),
#     ("доход", 1000, "Зарплата"),
#     ("расход", 200, "Ужин в ресторане"),
#     ("доход", 800, "Подработка"),
#     ("расход", 50, "Кино"),
# ]



# def balance():
#     summa = 0
#     for transaction in transactions:
#         if transaction[0] == "расход":
#             summa -= transaction[1]
#         elif transaction[0] == "доход":
#             summa += transaction[1]
#     print(summa)



# def expence():
#     expence_list = []
#     for transaction in transactions:
#         if transaction[0] == "расход":
#             expence_list.append(transaction)

    
#     print(expence_list)
    

# def limit():
    
#     limit_number = int(input("Input the limit"))
#     limit_list = []
#     for transaction in transactions:
#         if transaction[1] > limit_number:
#             limit_list.append(transaction)
#     print(limit_list)

# limit()

