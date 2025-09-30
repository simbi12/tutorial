
for i in range(2,101):   # Loop through numbers 2 to 100
    for j in range(2,101):   # Loop through numbers 2 to 100 again
        if i % j == 0:   # If i is divisible by j
            break        # Stop the inner loop
    if i == j:           # If i is equal to j (means only divisible by itself)
        print(i, end=",")  # Print the number (prime number)
