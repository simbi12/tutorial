# This program 
# calculates the total sales for a week.
total = 0

for days in range (1,7):
    sales = float(input(f'enter salesfor day {days}: '))
 
    total = total + sales 
print('Total sales for the week is' ,total)
