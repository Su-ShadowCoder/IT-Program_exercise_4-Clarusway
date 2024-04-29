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
data_lst = []

while True:
    number = input("Enter a whole number to make a list: ")
    data_lst.append(number)

    choice = input("Enter another number? (y/n): ")
    if choice.casefold() == "n":
        break
data_lst.sort()

lst_max_numb = max(data_lst)
lst_min_numb = min(data_lst)

data_lst.remove(lst_max_numb)
data_lst.remove(lst_min_numb)

print(data_lst)



