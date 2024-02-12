#data types 

# The major ones we have are string, interger, boolean, float

#data types can be determined using the type function and can be changed also using certain functions 

numbs = 10
detType = type(numbs) #printing this will bring out it's data type to be an interger. 

#changing it's data type 
my_string = str(numbs)
detTypes = type(my_string) #printing this wll give string to be it's data type because we have converted it

#variable 

name = "olusegun"

#for loop

numbers = [1, 2, 4, 6 ,7 ,8 , 9, 20, 3, 5, 12, 14, 95, 86, 72]

for num in numbers:
    if num % 2 == 0:
        continue
#     print("This is an odd number", num)
# print("Game is over")












#exercises 

#Exercise 1

#Suppose the cost of an item as $600. After a month, the cost is doubled due to exchange rates. About 3
# weeks later, the cost is reduced by $150. After a week, the cost is increased by $100.
# What is the new cost of the item? Write in python code.

initial_cost = 600

#Ater a month, intital cost doubled

initial_cost *= 2

# after 3 weeks, cost is reduced by $150

initial_cost -= 150

#After a week, cost has an increment of $100

initial_cost += 100

print("The new cost of the item is: $" + str(initial_cost))



