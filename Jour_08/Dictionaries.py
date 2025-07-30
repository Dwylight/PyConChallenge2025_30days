#1
dog = {}

#2
dog["Name"] = "Nathan"
dog["Color"] = "Purple"
dog["breed"] = "Black"
dog["legs"] = 2
dog["Age"] = 18
print(dog)

#3
student_dictionary = {
    "first_name": "Alice",
    "last_name": "Batch",
    "gender": "Female",
    "age": 18,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis", "Project Management"],
    "country": "Togo",
    "city": "Lomé",
    "address": "Agoè Telessou"
}
print(student_dictionary)

#4
print("the length of the student dictionary is :", len(student_dictionary))

#5
print("The value of skills is:", student_dictionary["skills"])
print(type(student_dictionary["skills"]))

#6
student_dictionary["skills"].append("Dance")
print(student_dictionary["skills"])

#7
print(list(student_dictionary.keys()))

#8
print(list(student_dictionary.values()))

#9
print(student_dictionary.items())

#10
del student_dictionary["gender"]
print(student_dictionary)

#11
del dog



