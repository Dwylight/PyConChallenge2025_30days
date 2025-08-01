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
liste = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in liste :
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


