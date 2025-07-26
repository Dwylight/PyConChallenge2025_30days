#1
print("Thirty "+"Days "+"Of "+"Python ")

#2
print("Coding "+"For "+" All")

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[:6])

#10
print(company.find("Coding"))

#11
print(company.replace("Coding", "Python"))

#13
print(company.split())

#14
string1 =  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string1.split(","))

#15
print("The character at index 0 in the string Coding For All is:", company[0])

#16
print("The last index of the string Coding For All is :", company[-1])

#17 
answer = company[10]
print(f"The character at index 10 in Coding For All is :'{answer}'")

#18
string = "Python For Everyone"

#19 

#20
print(company.find("C"))

#21
print(company.find("F"))

#22
print(company.rfind("l"))

#23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))

#24
print(sentence.rfind("because"))

#25
print(sentence[31:54])

#26
print(sentence.find("because"))

#27
print(sentence[31:54])

#28
print(company.startswith("Coding"))

#29
print(company.endswith("coding"))

#30 
string2 = '   Coding For All      '
print(''.join(string2))

#31
variable_1 = "30DaysOfPython"
variable_2 = "thirty_days_of_python"
print(variable_1.isidentifier())
print(variable_2.isidentifier())

#32
print('#'.join(['Django','Flask','Bottle', 'Pyramid', 'Falcon']))

#33
print('I am enjoying this challenge.\nI just wonder what is next.')

#34
print("Name\tAge\tCountry\tCity")
print("Asabeneth\t250\tFinland\tHelsinki")

#35
radius = 10 
area = 3.14 * radius ** 2
print(f"radius = {radius}")
print(f"area = {area}")
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

#36
num1 = 8
num2 = 6
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")


