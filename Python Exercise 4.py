# # Testing Git and Git push through git bash terminal! result: successful!
# print("yow")
# age = input("Enter your age: ")
# print(f"Your age is {age}!")
# print("something")

#  # Exercise 1
# list_1 = input("Enter numbers in comma within brackets[]"
#                "(or enter nothing at all),\n"
#                "the numbers you have entered "
#                "will change into a list.\n"
#                "The program wil then check if the "
#                "list is empty or not: ")
# if len(list_1) == 0:
#     print("This list IS empty!")
# elif list_1 == "[]":
#     print("This list IS empty!")
# else:
#     print("This list is NOT empty!")

# # Exercise 2
# data_lst = []
#
# while True:
#     number = input("Enter a whole number to make a list: ")
#     data_lst.append(number)
#
#     choice = input("Enter another number? (y/n): ")
#     if choice.casefold() == "n":
#         break
# data_lst.sort()
#
# lst_max_numb = max(data_lst)
# lst_min_numb = min(data_lst)
#
# data_lst.remove(lst_max_numb)
# data_lst.remove(lst_min_numb)
#
# print(data_lst)

# # Exercise 3
# user_input = list(input("Enter a list, and i wil convert to a string: "))
#
# # lst_1 = list(user_input)
# # lst_1 = ['h', 'e', 'l', 'l', 'o']
# # print(lst_1)
# lst_2 = "".join([str(i) for i in user_input])
# lst_2 = "".join([str(i) for a, i in enumerate(user_input)])
# print(lst_2)
# ['h', 'e', 'l', 'l', 'o']
# print(finito)
#
# # print("oowwh my godddd, This listu doesntu have the rightu sizuuuuu!\n"
# # "You have to Enter 5 characters, pls try again!\n"
# # "Enteru 5 characteru, oge-saimasu: ")

# # Exercise 4.1
# sick_days = [10, 4, 5, 19]
# sum_of_it = sum(sick_days)
# days_dancing = 365 - sum_of_it
# print(f"Frank was sick for {sum_of_it} days. \n"
#       f"He went dancing for {days_dancing} days.")
