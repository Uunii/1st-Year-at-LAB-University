# # Conditional

# print("Welcome to the moevement app!")
# Temperature = int(input("What is the temperature of your IoT CPU?"))

# #Notice the automatic indentation
# #The code block inside the if statement and the else statement

# if Temperature > 80:
#     print("Warning! The temperature is too high!")
# else:
#     print("Everything cool! Keep on going :)")

# # > Greater than
# # < Less than
# # >= Greater than or equal to 
# # <= Less than or equal to 
# # == Equal to - what is the difference to = ?
# # != Not equal

# # Exercise:Is it odd or even:

# num = int(input("Enter number"))
# Remainder = num % 2
# if Remainder ==0:
#     print("It is even number") 
# else:
#     print("It is odd number")

# # Elif statement

# name1 = input("Enter name 1:")
# name2 = input("Enter name 2:")

# char1 = len(name1)
# char2 = len(name2)

# if char1 > char2:
#     print("The length of the first name is longer than the second name")
# elif char1 < char2:
#     print("The length of the first name is shorter than the second name")
# else:
#     print("The length of the first name is equal to the second name") 

# # Logical operators

# x = 4

# # Returns True if both statement are True
# print(x<5 and x<10)
# # Returns True if one of the statement is true
# print(x<5 or x<4)
# # Reverses

# Town = input("Enter Town name: ")
# Street = input("Enter Street name: ")
# Building = int(input("Ender Building number: "))

# if (Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print("You are at LAB!")
# elif(Town == "Lahti" and Street == "Mukkulankatu" and Building > 19):
#     print("You went too far.")
# elif(Town == "Lahti" and Street == "Mukkulankatu" and Building < 19):
#     print("You are not there yet")
# elif(Town == "Lahti" and Street != "Mukkulankatu" or Building != 19 ):
#     print("You are in the correct town, but you ned to check your address.")
# else:
#     print("You are completely lost.")

# # Random number

# import random
# print (random.random()) 
# RandomInteger = random.randint(1, 10)
# print(RandomInteger)

# #Random letter
# import string
# string.ascii_letters
# print(random.choice(string.ascii_letters))

#  Simple menu

# print("Select from the list:")
# print("1.Login")
# print("2.Go to settings")
# print("3.Logout")
# Choose = input("Choose your option:")
# if (Choose == "1"):
#     print("Program started.")
# elif(Choose == "2"):
#     print("Settings.")
# elif(Choose == "3"):
#     print("Logged out.")
# else:
#     print("User input not recognized.")





#Rock, Paper, Scissors

import random
RandomInteger = random.randint(1,3)
move = input("What is your move?:")
print("You chose:", move )
if(RandomInteger == 1):
    print("The Computer chose: rock")
elif(RandomInteger == 2):
    print("The Computer chose: paper")
elif(RandomInteger == 3):
    print("The Computer chose: scissors")
if(RandomInteger == 1 and move == "rock"):
    print("Tie!")
elif(RandomInteger == 1 and move == "paper"):
    print("You won!")
elif(RandomInteger == 1 and move == "scissors"):
    print("You lost!")
elif(RandomInteger == 2 and move == "rock"):
    print("You lost!")
elif(RandomInteger == 2 and move == "paper"):
    print("Tie!")
elif(RandomInteger == 2 and move == "scissors"):
    print("You won!")
elif(RandomInteger == 3 and move == "rock"):
    print("You won!")    
elif(RandomInteger == 3 and move == "paper"):
    print("You lost!")
elif(RandomInteger == 3 and move == "scissors"):
    print("Tie!")
else:
    print("Please choose from Rock, Paper or Scissors")


