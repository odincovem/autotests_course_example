#Задание №3

string1 = "Hello, world!"

string2 = "Good job, guys."

print(
    (string1.replace('He', 'Go')),
    (string2.replace("Go", 'He'))
)

print(string1[:2] + string2[2:] + " " + string2[:2] + string1[2:])   #Вариант 1

print(len(string1))   #считаем символы в строках для удобства

print(len(string2))

print((string2[:-13] + string1[2:13]) + " " + (string1[:-11] + string2[2:15]))   #вариант 2
