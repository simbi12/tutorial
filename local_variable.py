def main():
    name= get_name()
    print('Hello', name)

def get_name():
    name= input('Enter your name: ')
    return name
main()