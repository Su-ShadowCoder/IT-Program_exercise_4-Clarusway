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
# # With user input
# userinput_list = []
#
# while True:
#     character_input = input("Enter a Character from the list in order. \n"
#                             "Remember to Enter 5 characters! : ")
#     userinput_list.append(character_input)
#     if len(userinput_list) == 5:
#         break
# userinput_list = "".join(userinput_list)
# print(userinput_list)
#
# Without user input. list in code
# lst = ['h', 'e', 'l', 'l', 'o']
# string = "".join(lst)
# if len(string) == 5:
#     print(string)
# else:
#     print("Enter a list with only 5 characters!")
# -----------------

# # Exercise 4.1
#
# sick_days = [0, 10, 4, 5, 19]
# sum_of_it = sum(sick_days)
# days_dancing = 365 - sum_of_it
# if sum_of_it < 0:
#     print(f"Frank can't be sick for {sum_of_it} ")
# # else:
# #     print(f"Frank was sick for {sum_of_it} days. \n"
# #           f"He went dancing for {days_dancing} days.")
#
# # Exercise 4.2
# sick_days_2 = [0, 7, 8, 2, 12]
# finito_sick_days = sick_days + sick_days_2
# print(f"The full list of Frank's sick days is:{finito_sick_days}")
# quarter_year_1 = max(sick_days)
# quarter_year_2 = max(sick_days_2)
# index_1 = sick_days.index(max(sick_days))
# index_2 = sick_days_2.index(max(sick_days_2))
# if quarter_year_1 > quarter_year_2:
#     print(f"Frank was sick the most in quarter {index_1} of the "
#           f"first year.")
# else:
#     print(f"Frank was sick the most in quarter {index_2} of the "
#           f"second year.")
