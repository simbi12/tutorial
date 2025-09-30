#Amount of purchase
amount=float(input('enter the amount of purchase: '))
#rtax rates
state_tax_rate = 0.05
country_tax_rate = 0.025

#compute the state, country and total sale tax
state_tax = amount * state_tax_rate
country_tax = amount * country_tax_rate
total_sale_tax = state_tax + country_tax 
total_sale = amount + total_sale_tax  

 # display the results print
print('Amount of purchase  \u20A6', amount)
 
print('State sales tax  \u20A6',format(state_tax, '.2f'))
print('Country sales tax \u20A6', format(country_tax, '.2f'))
print('Total sales tax \u20A6',  format(total_sale_tax, '.2f'))
print('Total sales \u20A6',  format(total_sale, '.2f'))