print("\n AI zaczyna.")
def printOX(plansza):
    print(plansza[1] + '|' + plansza[2] + '|' + plansza[3])
    print('-+-+-')
    print(plansza[4] + '|' + plansza[5] + '|' + plansza[6])
    print('-+-+-')
    print(plansza[7] + '|' + plansza[8] + '|' + plansza[9])
    print("\n")


def spaceIsFree(position):
    if plansza[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        plansza[position] = letter
        printOX(plansza)
        if (checkDraw()):
            print("Remis!")
            input("Wciśnij cokolwiek, żeby zakończyć")
            exit()
        if checkForWin():
            if letter == 'X':
                print("AI wygrywa!")
                input("Wciśnij cokolwiek, żeby zakończyć")
                exit()
            else:
                print("Gracz wygrywa!")
                input("Wciśnij cokolwiek, żeby zakończyć")
                exit()

        return


    else:
        print("Nie możesz tutaj!")
        position = int(input("Podaj nową pozycję:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if (plansza[1] == plansza[2] and plansza[1] == plansza[3] and plansza[1] != ' '):
        return True
    elif (plansza[4] == plansza[5] and plansza[4] == plansza[6] and plansza[4] != ' '):
        return True
    elif (plansza[7] == plansza[8] and plansza[7] == plansza[9] and plansza[7] != ' '):
        return True
    elif (plansza[1] == plansza[4] and plansza[1] == plansza[7] and plansza[1] != ' '):
        return True
    elif (plansza[2] == plansza[5] and plansza[2] == plansza[8] and plansza[2] != ' '):
        return True
    elif (plansza[3] == plansza[6] and plansza[3] == plansza[9] and plansza[3] != ' '):
        return True
    elif (plansza[1] == plansza[5] and plansza[1] == plansza[9] and plansza[1] != ' '):
        return True
    elif (plansza[7] == plansza[5] and plansza[7] == plansza[3] and plansza[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if plansza[1] == plansza[2] and plansza[1] == plansza[3] and plansza[1] == mark:
        return True
    elif (plansza[4] == plansza[5] and plansza[4] == plansza[6] and plansza[4] == mark):
        return True
    elif (plansza[7] == plansza[8] and plansza[7] == plansza[9] and plansza[7] == mark):
        return True
    elif (plansza[1] == plansza[4] and plansza[1] == plansza[7] and plansza[1] == mark):
        return True
    elif (plansza[2] == plansza[5] and plansza[2] == plansza[8] and plansza[2] == mark):
        return True
    elif (plansza[3] == plansza[6] and plansza[3] == plansza[9] and plansza[3] == mark):
        return True
    elif (plansza[1] == plansza[5] and plansza[1] == plansza[9] and plansza[1] == mark):
        return True
    elif (plansza[7] == plansza[5] and plansza[7] == plansza[3] and plansza[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in plansza.keys():
        if (plansza[key] == ' '):
            return False
    return True


def playerMove():
    print("Pozycje do wyboru jak poniżej:")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")
    position = int(input("Podaj pozycję dla kółka:  "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    for key in plansza.keys():
        if (plansza[key] == ' '):
            plansza[key] = bot
            score = minimax(plansza, 0, False)
            plansza[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(plansza, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in plansza.keys():
            if (plansza[key] == ' '):
                plansza[key] = bot
                score = minimax(plansza, depth + 1, False)
                plansza[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in plansza.keys():
            if (plansza[key] == ' '):
                plansza[key] = player
                score = minimax(plansza, depth + 1, True)
                plansza[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


plansza = {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printOX(plansza)
print("Pozycje do wyboru jak poniżej:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
