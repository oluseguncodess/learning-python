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



# 3. Print the first 3 elements.
# 4. Print the last 3 elements.
# 5. Ask the user for their favorite color and append it to the list.
# 6. What will be the output of the following:

# Create a list of your favorite colors.
colors = ['orange', 'green', 'blue', 'black', 'red', 'purple']

# 1. Print the second and fourth elements from the list.
print('second element:', colors[1])
print('fourth element:', colors[3])

# 2. Print the elements from the 3rd to the 7th.
print(" Element's from the 3rd to the 7th:", colors[2:6])


# 1. Create variables with appropriate identifiers for the following:
# a. Your name
# b. Your age
# c. The value of Pi (3.14)
# 2. Use assignment operators to update the following variables:
# a. `count` starts at 5, increment it by 2.
# b. `total` starts at 10, decrement it by 3.
# 3. Given `food_cost` as $900 and `light_cost` as $950. Write code to check if the following statements
# are True or False:
# a. Is the cost of food lower than the cost of light?
# b. Is the cost of light greater than $900?
# c. Is the cost of food greater than $1000 or the cost of light less than $900?

#Solution
# 1. Variables
# a. Your name
name = "Your Name"
# b. Your age
age = 30
# c. The value of Pi
pi_value = 3.14

# 2. Updating variables
# a. Increment count by 2
count = 5
count += 2
# b. Decrement total by 3
total = 10
total -= 3

# 3. Checking statements
# Given values
food_cost = 900
light_cost = 950

# a. Is the cost of food lower than the cost of light?
statement_a = food_cost < light_cost
# b. Is the cost of light greater than $900?
statement_b = light_cost > 900
# c. Is the cost of food greater than $1000 or the cost of light less than $900?
statement_c = food_cost > 1000 or light_cost < 900

# Print results
print("Statement a:", statement_a)
print("Statement b:", statement_b)
print("Statement c:", statement_c)

