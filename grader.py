# A simple program to test student scores and display their grades

A_score = 90
B_score = 80
C_score = 70
D_score = 60

#Get a test score from the student

score = int(input('Enter your test score: '))

if score > A_score:
    print('Your grade is A')
else:   
    if score > B_score:
        print('Your grade is B')
    else:
        if score > C_score:
            print('Your grade is C')
        else:
            if score > D_score:
                print('Your grade is D')
            else:
                print('Your grade is F')    