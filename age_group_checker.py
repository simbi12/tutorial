# age group checker
age = int(input('Enter you your age: '))

if age >= 18:
    if age >= 60:
        print('You are a senior citizen')
    else:
        print('You are an adult')
elif age >= 13 and age < 18:
    print('You are a teenager')

else:
    print('You are a child')