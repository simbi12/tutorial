# Program to compare the areas of two rectangles
# Get dimensions of the first rectangle
lenght1 = float(input('Enter the length of the first rectangle: '))
width1 = float(input('Enter the width of the first rectangle: ' ))
# Get dimensions of the second rectangle
lenght2 = float(input('Enter the length of the second rectangle: '))
width2 = float(input('Enter the width of the second rectangle: ' ))

area1 = lenght1 * width1
area2 = lenght2 * width2

if area1 > area2:
    print('rectangle 1 has a greater area')
elif area2 > area1:
    print('rectangle 2 has a greater area')
else:
    print('they are equal')