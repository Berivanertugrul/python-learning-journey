
# Data Type Checking and Type Conversion

x = 10
print(type(x))

x = "10"
print(type(x))

""" print("25" + 5 )  #TypeError: can only concatenate str (not "int") to str """


# Type Conversion (Casting)

x = "25"

print(type(x))     #str
print(type(int(x)))      # Converted data type / Converted from string to integer
print(type(float(x)))


x = 35
print(type(x))
print(type(str(x)))


number = input("Enter a number: ")   # What can the input() function return? (int? str?)

print(number)  #45 int? str?
print(type(number))   #<class 'str'>

number = int (input("Enter a number: "))   # If we define the input function this way, it returns an integer.
print(type(number))
