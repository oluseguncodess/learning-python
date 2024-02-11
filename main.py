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
