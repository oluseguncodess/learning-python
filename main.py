# Learning python by doing exercises!!

# #Exercise 1 - 

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

# print("The new cost of the item is: $" + str(initial_cost))


# Exercise 2

# Given that the age of Joe is 26 and the age of Lisa is 29, write code to compare these ages. Print True if
# the following statements are True and False if not:

# 1. Is Joe older than Lisa?
# 2. Is Joe older than 30 and Lisa less than 30?
# 3. Is Joe older than 30 or Lisa less than 30?
# 4. Are Joe and Lisa equal in age?
# 5. Is Lisa’s age greater or equal to 40?

#Solution

# joe = 26

# lisa = 29

# #1. is Joe older than Lisa? 
# print("It is " + str(joe > lisa) + " that Joe is older than Lisa")

# # 2. Is Joe older than 30 and Lisa less than 30?
# print((joe > 30), ", Joe is not older than 30 and", (lisa < 30), "Lisa is less than 30")

# Exercise 3 

# Create a Python script that uses escape characters to format and print the following text:

# My favorite programming languages:
# 1. Python
# 2. Java
# 3. C++

# solution
# print("My favourite programming languages: \n 1. Python \n 2. Java \n 3. C++")

# Exercise 4


# 2. Print the elements from the 3rd to the 7th.
# 3. Print the first 3 elements.
# 4. Print the last 3 elements.
# 5. Ask the user for their favorite color and append it to the list.
# 6. What will be the output of the following:

# Create a list of your favorite colors.
colors = ['orange', 'green', 'blue', 'black', 'red', 'purple']


# 1. Print the second and fourth elements from the list.
print(colors[1][4])
