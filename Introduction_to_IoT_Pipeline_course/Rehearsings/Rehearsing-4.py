# # print("Hello")
# # char =len("Hello")
# # print(char)

# # DEF function
# # def greeting():
# #     print("How do you do?")

# # hi = input("How are yaa: ")
# # if hi == "1":
# #     greeting()

# # def greeting_airport(person, age):
# #     print(f"How do you do {person}")
# #     if age >= 18:
# #         print("Welcome on your flight")
# #     else:
# #         print("I'm sorry, you are not allowed to fly on your own")
# #         print(f"You need to wait for {18- age} years")
# # greeting_airport("Uunii", 25)

# # name = input("name:")
# # age = input("age:")
# # if
# # print("How do you do", name)
# # print("WElcome to your flight")




# # #variables and parameters only works inside the function but you can call it again defining even in different order like below

# # greeting_airport(age=15, person="Uunii")

# # def prime_number(Num):
# #     Num = int(input("Enter any number: "))
# #     remainder1 = (Num/1)
# #     remainder2 = (Num/Num)
# #     remainder3 = (Num % 2)
# #     while(remainder1 == Num and remainder2 == 1 and remainder3 == 1):
# #         print("The number you have entered is a 'Prime Number'")
# #         break
# #     else:
# #         print("The number you have entered is 'not a Prime number'")
    
# # prime_number(Num =())
# # while True:
# #     Answer =input("Do you want to test another number: ")
# #     if (Answer == "yes"):
# #         prime_number(Num =())
# #     elif(Answer == "no"):
# #         break
 
# def name():
#     fname = input("Enter your first name: ")
#     lname = input("Enter your last name: ")
#     print(fname.capitalize())
#     print(lname.capitalize())
#     while fname == "":
#         print("You didn't provide valid inputs for 'first name'")
#     if lname == "":
#         print("You didn't provide valid inputs for 'last name'")

# name()

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result": {formated_f_name} {formated_l_name}

# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)


# def add(n1, n2):
#     return n1+n2

# def subtract(n1,n2):
#     return n1-n2

# def multiply(n1,n2):
#     return n1*n2

# def divide(n1,n2):
#     return n1/n2

# print(add(2,multiply(5,divide(5,4))))

# def outer_function(a,b):
#     def inner_function(c,d):
#         return c+d
#     return inner_function(a,b)
# result = outer_function(5,10)
# print(result)

# def initialize():
#     print("Initializing resources...")
# def process_data(data):
#     return data.upper()
# def save_result(results):
#     print(f"saving results:{results}")


