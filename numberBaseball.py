import random

pc_1 = random.randint(0, 9)
pc_2 = random.randint(0, 9)
pc_3 = random.randint(0, 9)

while(pc_1 == pc_2 or pc_2 == pc_3 or pc_3 == pc_1):
    pc_1 = random.randint(0, 9)
    pc_2 = random.randint(0, 9)
    pc_3 = random.randint(0, 9)
else:
    stopper = 1
    while(stopper == 1):
        pc = [pc_1, pc_2, pc_3]
        print(pc)
        goStop = str(input('GO or Stop:'))
        if goStop == 'go':
            userAnswer_1 = int(input("Choice 0~9 \n:"))
            userAnswer_2 = int(input("Choice 0~9 \n:"))
            userAnswer_3 = int(input("Choice 0~9 \n:"))
            user = [userAnswer_1, userAnswer_2, userAnswer_3]
            if (userAnswer_1 == userAnswer_2 or userAnswer_1 == userAnswer_3 or userAnswer_2 == userAnswer_3):
                print("각자 다른숫자만 입력해주세요.")
            else:
                if ((userAnswer_1 in pc) and (userAnswer_2 in pc) and (userAnswer_3 in pc)):
                    if ((userAnswer_1 == pc_1) and (userAnswer_2 == pc_2) and (userAnswer_3 == pc_3)):
                        print("3S! 게임승리!")
                        stopper = 0
                    elif ((userAnswer_1 == pc_1 and userAnswer_2 == pc_2) or (userAnswer_2 == pc_2 and userAnswer_3 == pc_3) or (userAnswer_1 == pc_1 and userAnswer_3 == pc_3)):
                        print("2S! 1B!")
                    elif (userAnswer_1 == pc_1 or userAnswer_2 == pc_2 or userAnswer_3 == pc_3):
                        print("1S! 2B!")
                    else:
                        print("3B!")
                elif ((userAnswer_1 in pc and userAnswer_2 in pc) or (userAnswer_1 in pc and userAnswer_3 in pc) or (userAnswer_2 in pc and userAnswer_3 in pc)):
                    if ((userAnswer_1 == pc_1 and userAnswer_2 == pc_2) or (userAnswer_1 == pc_1 and userAnswer_3 == pc_3) or (userAnswer_2 == pc_2 and userAnswer_3 == pc_3)):
                        print("2S!")
                    elif (userAnswer_1 == pc_1 or userAnswer_2 == pc_2 or userAnswer_3 == pc_3):
                        print("1S! 1B!")
                    else:
                        print("2B!")
                elif(userAnswer_1 in pc or userAnswer_2 in pc or userAnswer_3 in pc):
                    if (userAnswer_1 == pc_1 or userAnswer_2 == pc_2 or userAnswer_3 == pc_3):
                        print("1S!")
                    else:
                        print("1B!")
                else:
                    print("OUT!!")
        elif goStop == 'stop':
            print(pc)
            stopper = 0
        else:
            print("Please insert only go or stop")