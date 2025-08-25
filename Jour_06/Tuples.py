#Level1

#1
empty_tuple = ()

#2
brothers = ("Mike", "Andy", "Charbel")
sisters = ("Bright", "Joana", "Dorcas", "Luce")

#3
siblings = brothers + sisters
print(siblings)

#4
print(f"I have {len(siblings)} siblings")

#5
siblings = list(siblings)
siblings.append("Casimir")
siblings.append("Bienvenue")
family_members = tuple(siblings)
print(family_members)


#Level 2

#1
siblings = family_members[:-2]
print(siblings)
parents = family_members[-2:]
print(parents)

#2
fruits = ("Lemon", "Banana", "Blueberry")
vegetables = ("onion", "Tomato", "Pepper")
animal_products = ("Egg", "Milk", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
#4
middle_food = food_stuff_tp[int(len(food_stuff_tp)/2)]
print(middle_food)

#5
first_three = food_stuff_tp[:3]
print(first_three)
last_three = food_stuff_tp[-3:]
print(last_three)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Estonia is a nordic country: {"Estonia" in nordic_countries}")
print(f"Iceland is a nordic country: {"Iceland" in nordic_countries}")


