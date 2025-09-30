#This program calculate sales commission
# Create a variable to the loop

keep_running = 'y'
#Cal series of commission

while keep_running == 'y':
    #Get the sales and commission rate
    sales = float(input('Enter the amount sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    commission = sales * comm_rate

    print('The commission is  ', format(commission,',.2f') ,sep = '')
    keep_running = input("Do you want to calculate another commission? (Enter 'y' for yes): ")
