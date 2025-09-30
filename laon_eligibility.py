#This program determine whether a bank customer is eligible to take a loan
min_salary = 30000   #minimum annual salary 
min_year = 2         #minimum year on the job

#Get the customers annual salary
salary = float(input('Enter the amount earn: '))
#The customers year on the job
yearOnJob = int(input('Enter the numbers of year on the job: '))

#Check if the customers are qualify for collect a loan

if salary >= min_salary:
    if yearOnJob >= min_year:
        print('You are qualify')
    else:
        print('You must have been employed for two years')

else:
    print('You must atleast earn ',min_salary, 'per_year to qualify')


