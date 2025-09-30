for cols in range(8):
    for rows in range(6):
        print('*', end='')
    print()

base_value = 8

for r in range(base_value):
    for col in range(r+1):
        print('*' ,end ='')
    print()