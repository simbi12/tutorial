def main():
    te = texas()
    ca = california()
    return te + ca

def texas():
    birds = 5000
    print('texas has', birds, 'birds.')
    return birds

def california():
    birds = 1000
    print('california has', birds ,'birds')
    return birds

result=main()
print(result)
