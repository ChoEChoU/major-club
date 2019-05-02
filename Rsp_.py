import random
def RSP():
    print("Start Rock Scissor Paper Game with Computer.")
    while(True):
        a = random.randint(1, 3)
        b = int(input("Rock = 1\nScissor = 2\nPaper = 3\nPlease input number: "))
        if (b == 1) or (b == 2) or (b == 3):
            if (a == b):
                print("Draw")
                print("================")
            elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
                print("Lose")
                print("================")
            else:
                print("Win")
                print("================")
        else:
            break

RSP()