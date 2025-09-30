#program that calculates the total amount of a meal purchased at a restaurant

food_charge = int(input('enter the amount of food charge: '))

#tip 18%
tip = food_charge * 0.18

# sales tax 7%
sales_tax = food_charge * 0.07

total = food_charge + tip + sales_tax 

print('The food charge is \u20A6', food_charge)
print('The tip(18%) is \u20A6', tip)
print('The sales tax is \u20A6', sales_tax)
print('The total is \u20A6',  total)
