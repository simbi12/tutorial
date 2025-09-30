# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score

high_score = 95
firstScore = float(input('Enter the first  test score: '))
secondScore = float(input('Enter the second test score: '))
thirdScore = float(input('Enter the third test score: '))

#calculate the average of the three scores 
average = (firstScore + secondScore + thirdScore)/3

#Display the results
print('The first test score is ', firstScore)
print('The second test score is ', secondScore)
print('The third test score is ', thirdScore)
print('The average score is ' ,average)

if average >= high_score:
    print('Congratulation!, That is a great score')