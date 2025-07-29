
#Level1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("The lenght is:",len(it_companies))

#2
it_companies.add("twitter")
print(it_companies)

#3
it_companies.update(["Huawei", "Infinix", "Twitter"])
print(it_companies)

#4
it_companies.remove("Huawei")
print(it_companies)

#5
print("la différence est que contrairement à discard, remove envoie un message d'erreur si l'item ne se trouve pas dans l'ensemble")

#Exercice 2

#1
C = A.union(B)
print(C)

#2
inter = A.intersection(B)
print (inter)

#3
print(" A is subset of B:", A.issubset(B))

#4
print(" A and B are disjoint sets:", A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print("The symmetric difference between A and B is:", A.symmetric_difference(B))

#7
del it_companies
del A
del B

#Level 3

#1
print(len(age))
age = set(age)
print(age)
print(len(age))
print("The lenght of the list is bigger than the lenght of set")

#2
print("The difference is that the string is one argument not a collection, the list is modifiable and we can have one argument many times, the tuple is unmodifiable and sets is a unordred collection of unique elements")

#3
sentence = "I am a teacher and I love to inspire and teach people"

list_sentence = sentence.split()
print(list_sentence)
list_sentence = set(list_sentence)
print("Number of unique word:", len(list_sentence))