myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? maria ")
color = input("What is your favorite color? green")
animal = input("What is your favorite animal? polar bear")
print("{}, you like a {} {}!".format(name,color,animal))