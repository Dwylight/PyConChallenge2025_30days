#Level 1

#1
for i in range (11):
    print(i)

i = 0

print("")

while i < 11:
    print(i)
    i += 1

#2
for i in range (11, 0, -1):
    print(i)

i = 10

print("")

while i > 0 :
    print(i)
    i -= 1
else :
    print(i)

#3
i = 1
for i in range (8):
    print(i * "#")

print("")

#4
for i in range (9):
    for j in range (9):
        print("# ", end = "")
    print("#")

#5
for i in range (11):
    print(f"{i} x {i} = {i * i}")

#6
list_1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in list_1 :
    print(language)

#7
for i in range (0, 102, 2):
    print(i)

#8
for i in range (0, 100):
    if i % 2 == 0:
        continue
    print(i)

#Level 2

#1
somme = 0
for i in range (101):
    print(i)
    somme += i
else :
    print(f"The sum of all number is {somme}")

#1
sum_even = 0
sum_odd = 0
for i in range (101):
    print(i)
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
else:
    print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}")



    

