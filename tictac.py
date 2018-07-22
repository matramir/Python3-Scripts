#! python3
# tictac.py - tic tac toe game for two players
import sys
theBoard = {'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}
turn = 1
value = ''
gameContinues = True
#Method that prints the board in the console
def printBoard(board):
    print(board['top-L'] + '|'+board['top-M'] + '|'+board['top-R'])
    print('------')
    print(board['mid-L'] + '|'+board['mid-M'] + '|'+board['mid-R'])
    print('------')
    print(board['low-L'] + '|'+board['low-M'] + '|'+board['low-R'])
printBoard(theBoard)

#Method that registers a player turn
def takeTurn(turn):
    if (turn % 2) == 0:
        value = 'O'
    else:
        value = 'X'
    isTaken = True
    while isTaken == True:
        print('Turn: '+ str(turn) +'\nEnter the location for your next move by calling the top, mid or low row in the L,M or R column\n(Example: mid-M')
        place = input()
        if place not in theBoard.keys():
            print('Board place not valid.')
            isTaken = True
            printBoard(theBoard)
        else:
            if theBoard[place] != ' ':
                print('Board place already taken.')
            else:
                isTaken = False
                theBoard[place] = value
                printBoard(theBoard)
#Method that checks win condition on 3 cels
def checkWin(pA, pB, pC):
    if theBoard[pA] != ' ' and theBoard[pB] != ' ' and theBoard[pA] != ' ':
        if theBoard[pA] == theBoard[pB] and theBoard[pA]== theBoard[pC]:
            return True
        else:
            return False
    else:
        return False

#Method that checks all winning conditions
#top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '
def checkBoard():
    winCombinations = (['top-L','top-M','top-R'], ['mid-L','mid-M','mid-R'], ['low-L','low-M','low-R'],
    ['top-L','mid-L','low-L'], ['top-M','mid-M','low-M'], ['top-R','mid-R','low-R'], ['top-L','mid-M','low-R'], ['top-R','mid-M','low-L'] )
    for combination in winCombinations:
        win = checkWin(combination[0],combination[1],combination[2])
        if win == True:
            return True
            break
        else:
            continue


while gameContinues == True:
    takeTurn(turn)
    if checkBoard() == True:
        print('There is a winner!')
        gameContinues = False
        sys.exit()

    else:
        if ' ' not in (theBoard.values()) :
            print ('No more places left.')
            sys.exit()
        turn = turn + 1
