import time


def step1():
    print('Step 1: Unplug the dryer and move it away from the wall.\n')

def step2():
    print('Step 2: Remove the six screws from the back of the dryer.\n')

def step3():
    print('Step 3: Remove the back panel from the dryer.\n')

def step4():
    print('Step 4: Pull the top of the dryer straight up.\n')

def main():
    print("This program tells you how to disassemble an ACME laundry dryer.\n")

    step1()
    time.sleep(3)   # wait 3 seconds before showing the next step
    step2()
    time.sleep(3)
    step3()
    time.sleep(3)
    step4()

main()