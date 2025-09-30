grades = int(input('Enter a number between 0-100: '))
 
if grades >= 70:
    print('excellent')
elif grades >= 50 and grades < 70:
    print('pass')
else:
    print('fail')