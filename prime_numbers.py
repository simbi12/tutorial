for primeNumber in range(2, 31):
    count = 0
    for multiple in range(2, 31):
        if primeNumber % multiple == 0:
            count  += 1
            # print(primeNumber, '<<<<<<>>>>>>>>', multiple)
            if count > 1:
                count = 0
                break
    
    if count == 1:
         print(primeNumber)



