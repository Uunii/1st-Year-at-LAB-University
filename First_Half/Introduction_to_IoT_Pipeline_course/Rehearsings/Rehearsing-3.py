# # Lists
# # Variables store one piece of information

# Children = 3
# Hometown = "Lahti"

# #We might need to store multiple pieces of information
# TownsInFinland = ["Lahti", "Helsinki", "Lappeeranta", "Oulu", "Tampere"]

# #We ca save random types of data in the list
# RandomInformation = ["Mira", "47", "True", "Children", "hometown"]

# #Lists

# print(TownsInFinland[0])
# print(TownsInFinland[-1])

# TownsInFinland[2] = "Turku"
# print(TownsInFinland)

# TownsInFinland.append("Rovaniemi")
# print(TownsInFinland)

# NumOfTowns = len(TownsInFinland)
# print(TownsInFinland[NumOfTowns-1])

#You can even have a list inside a list.

# Municipalities = ["Asikkala", "Hollola", "Karvia", "Kampele"]
# Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampera"]
# MunicipalitiesAndTowns = [Municipalities, Towns]
# print(MunicipalitiesAndTowns[1][-2]) 

#Select elements from a lists

# Towns = ["Lahti", "Helsinki", "Turku", "Vaasa", "Mikkeli", "Lappeenranta", "Oulu", "Tampera"]
# print(Towns[2:5])
# print(Towns[2:])
# print(Towns[:5])
# print(Towns[2:5:2])
# print(Towns[::-2])

# Towns.sort()
# print(Towns)

#Dictionaries

# Student = {
#     'name': 'Unubold',
#     'age' : '25',
#     'city' : 'Ulaanbaatar'
# }

# #Retrieving items
# print(Student["name"])

# #Adding items
# Student['email'] = 'Unubold.Luvsandagva@student.lab.fi'

# Loop through a dictionary

# Student = {
#     'name' : 'Unubold'
# }
# for key in Student:
#     print(key)
#     print(Student[key])

#Nesting a dictionary in a list

# Students = [
#     {'name': 'Mikko', 'age':25, 'city':'Tampere'},
#     {'name': 'Maija', 'age':30, 'city' : 'Espoo'},
#     {'name': 'Uunii', 'age':25, 'city' : 'Ulaanbaatar'}
# ]
# print(Students)

# print(Students[2])

#List in a dictionar

# Cities = {
#     'Finland':['Tampere', 'Espoo', 'Helsinki'],
#     'Sweden':['Stockholm', 'Goteborg', 'Malmo']
# }

# print(Cities['Finland'][0])
# print(Cities['Sweden'][-1])

#How would you print 'Steak'

# Order = {
#     "starter": {1: "Salad", 2:"Soup"},
#     "main": {1: ["Burger", "Fries"], 2:["Steak"]},
#     "dessert": {1: ["Ice cream"], 2:[]}
# }
# print(Order['main'][2][0])

#How would you loop through the Python basics content and print each topic?

# Courses= {
#     'Python basics':{
#         'content':[
#             'conditions', 'loops', 'functions', 'data', 'types'
#             ],
#         'credits':4
#     },
#     'Databases':{
#         'content':[
#             'Setup', 'CRUD', 'Relation', 'Joins'
#             ],
#     'credits':5
#     }
# }
# # print(Courses['Python basics']['content'])
# # for topic in Courses['Python basics']['content']:
# #     print(topic)


# #For everything in the dictionary.
# print("Contents of Python basics:")
# for topic in Courses['Python basics']['content']:
#     print(topic)
# print("Contents of Databases:")
# for topic in Courses['Databases']['content']:
#     print(topic)

# #Miras solution

# for course, details in Courses.items():
#     print(f"Contents of {course}")
#     for content in details['content']:
#         print(content)

#For loops

# Towns = {
#     'town': [
#         'Lahti', 'Helsinki', 'Lappeenranta', 'Oulu', 'Tampera'
#     ],
# }
# for town in Towns['town']:
#     print(town)
# if(town == "Lahti"):
#     print("The town of Lahti, our hometown!")
# elif(town == "Helsinki"):
#     print("The town of Helsinki, our capital city!")
# else:
#     print("The town of", town)

#For-loops

# for i in range(1,10):
#     print(i)
# #Prints top to bottom 1 by 1

# for i in range(1,10):
#     print(i, end=' ')
# #Prints continously with space between becuase of sep= command

# for i in range(1, 10, 3):
#     print(i)
# #Prints every 3rd number in range of 1-10

# Total = 0
# for i in range(1,101):
#     Total += i

# print(Total)

#Make a program, which adds even numbers together until the number which the user inputs to the program.

# num = input("Enter number: ")

# Total = num
# for i in range(1,100):
#     Total 
# print(Total)

#skipping the action
# for i in range(9):
#     if i ==3:
#         continue
#     print(i)

#While -loops
#while loop iterates while the condition is true
#infinite loop
# while 1<10:
#     print("Do not try me XD")

# i = 0
# while i <10:
#     print(f"The ileration number is {i}")
#     i += 1

# ContinueLoop = True
# while ContinueLoop == True:
#     if input("Do you want to continue? ") != "yes":
#         ContinueLoop = False

while True:
    if input("Do you want to continue another loop? ") != "yes":
        break
    else:
        continue




