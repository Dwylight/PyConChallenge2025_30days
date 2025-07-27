#1

empty_list = []

#2
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#3
print("The lenght of days is: ",len(days))

#4
print("The first item is :", days[0])
print("The middle item is :", days[int(len(days)/2)])
print("The last item is :", days[-1])

#5
mixed_data_types = ("Damy", 18, 160, "Single", "Kara")

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print("it_companies:",it_companies)

#8
print("The number of companies in the list is:",len(it_companies))

#9
print("The first company is :", it_companies[0])
print("The middle company is :", it_companies[int(len(it_companies)/2)])
print("The last company is :", it_companies[-1])

#10
it_companies[0] = "OpenAI"
print("it_companies:",it_companies)

#11
it_companies.append("Huawei")
print("it_companies:",it_companies)

#12
it_companies.insert(int(len(it_companies)/2), "YouTube")
print("it_companies:",it_companies)

#13
it_companies[1] = it_companies[1].upper()
print("it_companies:",it_companies)

#14
print("#".join(it_companies))

#15
print(f"Toyota exists in it_companies : {"Toyota" in it_companies}")

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[:3])

#19
print(it_companies[-3:])

#20 ?????
print(it_companies)

#21
it_companies.remove(it_companies[0])
print(it_companies)

#22???

#23
it_companies.pop()
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB']
front_and_back_end = front_end + back_end
print(front_and_back_end)

#27
full_stack = front_and_back_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)


#Level2

#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minimum = ages[0]
maximum = ages[-1]
print(f"The minimum is {minimum} and the maximum is {maximum}")
ages.insert(0, minimum)
ages.append(maximum)
median_age = ages[int((len(ages)-1)/2)]
average = sum(ages)/len(ages)
range = maximum - minimum
print("The range of the ages :", range)
min_average = abs(minimum - average)
max_average = abs(maximum - average)


#1
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("The middle country is:", countries[int(len(countries)/2)])

#2
half_1 = countries[:int(len(countries)/2)]
print(half_1)
half_2 = countries[int(len(countries)/2):]
print(half_2)

#3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries
