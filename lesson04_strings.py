
#string

name = "Bob"  # Double quotation marks example
company = 'Bob Technology'  # Single quotation marks example

information = "Bob Technology is Bob's company."
print(information)


# String concatenation (birleştirme)

name = "Bob"
company = "Bob Technology"

information2 = company + " is " + name + "'s company."
print(information2)


# Combining strings and numbers

age = 22

str_age = str(age)

name = "Berivan"

result = name + "'s age is " + str_age + "."
print(result)


#Example1:

name ="Berivan Ertuğrul"
day = 20
month = "June"
date = 2004

str_day = str(day)
str_date = str(date)

result = name + "'s birthday is " + str_day + " " + month + " " + str_date + "."
print(result)


#Example2:

name = "Berivan Company"
installation_date = 2023
str_install = str(installation_date)

print("Berivan Company was founded 2023.")

print(name + " was founded " + str(installation_date) + ".")

#f string 

name = "Berivan Company"
date = 2023

print (f"{name} was founded in {date}.")

#Example:

accuracy = 95
print(f"The accuracy of the decision tree is {accuracy}%. ")

#String indexing

word = "python"
print(word[0])
print(word[3])


#String Methods

text = "PythoN"
text_lower_case = text.lower()
print(text_lower_case)


# Finding the length of a string

text2 = "python"
text_length = len(text2)
print(text_length)


# Replacing

text3 = "python"
print(text3.replace("o" , "O"))
