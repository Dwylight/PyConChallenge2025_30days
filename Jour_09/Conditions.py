# Niveau 1

#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    missing_years = 18 - age
    print("You need", missing_years,"years to learn to drive")


#2
my_age = 25
your_age = int(input("Enter your age: "))
if my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 years older than me.")
    else:
        print("You are", difference, "years older than me")
elif my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 years older than you.")
    else:
        print("I am" ,difference, "years older than you")
else:
    print("We're the same age.")


#3
number_one = int(input('Enter number one'))
number_two = int(input('Enter number one'))
if number_one > number_two :
    print(number_one,"is greater than",number_two)
else :
    print(number_two,"is greater than",number_one)

#Level 2

#1
score = float(input("Enter the score:"))
if score >= 80 and score <= 100 :
    print("You are in grade A")
elif  score >= 70 and score <= 89 :
    print("You are in grade B")
elif  score >= 60 and score <= 69 :
    print("You are in grade C")
elif  score >= 50 and score <= 59 :
    print("You are in grade D")
elif  score >= 0 and score <= 49 :
    print("You are in grade F")
else :
    score = float(input("EEnter a valid number!!!"))


    
