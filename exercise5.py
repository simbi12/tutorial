# Write a program that prints all numbers between 1 and 50 that are divisible by 3.

print("Numbers between 1 and 50 divisible by 3:")
print()
for i in range(1,51):
    if i % 3 == 0:
        print(i)