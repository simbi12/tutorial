# Use a while loop to keep asking the user for a password until they enter the correct one.
password = 'user123'

user = input('enter a password:')

while password != user:
    print('incorrect password')
    user = input('Enter a new password: ')
print('sucessful')