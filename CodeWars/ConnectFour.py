#https://www.codewars.com/kata/connect-four-1/train/python

import numpy as np

def who_is_winner(pieces_position_list):

    board=np.zeros((6,7))

    for x in pieces_position_list:
        column=letterToNumber(x[0])
        board=checkColumnInsertPiece(board,column,x[2])

        isWinner, winner=checkWinner(board)

        if isWinner:
            if winner=='Y':
                return 'Yellow'
            elif winner=='R':
                return 'Red'
            else:
                return 'There seems to be a problem'

    return "Draw"

def checkColumnInsertPiece(board,column,team):
    piece=[]
    for x in range(len(board)-1,-1,-1):
        if board[x][column]!=0:
            piece.append(board[x][column])
        else:
            if team=='R':
                board[x][column]=2
                break
            else:
                board[x][column]=5
                break

    return board

def letterToNumber(let):
    if let=='A':
        return 0
    elif let=='B':
        return 1
    elif let=='C':
        return 2
    elif let=='D':
        return 3
    elif let=='E':
        return 4
    elif let=='F':
        return 5
    elif let=='G':
        return 6

def checkWinner(board):
    returner=False
    team='D'
    #checks Horizontal
    for x in range(len(board)-1,-1,-1):
        if np.sum(board[x])==0:
            continue
        #checking horizontals
        sequence=1
        for y in range(len(board[x])):
            try:
                if y>=5 and sequence<2:
                    break
                if board[x][y]!=0 and board[x][y] == board[x][y+1]:
                    sequence+=1
                    if sequence==4:
                        return sendItBack(board[x][y])
                else:
                    sequence=1
            except IndexError as error:
                sequence=1
                pass
    #checks the verticals for 4 in a row
    for i in range(len(board)):
        vertical=board[:,i]
        sequence=1
        diagnal=1

        for b in range(len(vertical)-1,-1,-1):
            #checks diagnal up-right (same as down-left)
            try:
                if board[b][i]!=0 and board[b-1][i+1]==board[b][i]:
                    diagnal+=1
                    if board[b-2][i+2]==board[b][i]:
                        diagnal+=1
                        if board[b-3][i+3]==board[b][i]:
                            diagnal+=1
                            return sendItBack(board[b][i])
            except IndexError as error:
                diagnal=1
                pass
            #checks diagnal down-right (same as up-left)
            try:
                if board[b][i]!=0 and board[b+1][i+1]==board[b][i]:
                    diagnal+=1
                    if board[b+2][i+2]==board[b][i]:
                        diagnal+=1
                        if board[b+3][i+3]==board[b][i]:
                            diagnal+=1
                            return sendItBack(board[b][i])
            except IndexError as error:
                diagnal=1
                pass

            if vertical[b]!=0 and vertical[b]==vertical[b-1]:
                sequence+=1
                if sequence==4:
                    return sendItBack(vertical[b])
                continue
            if b<2 and sequence==1:
                break
            if sequence==4:
                return sendItBack(vertical[b])

    #check Diagnal

    return returner, team

def sendItBack(team):

    if team==2:
        return True, 'R'
    else:
        return True, 'Y'

def checkTests(test,winner,expected):
    if winner==expected:
        print(str(test) + " Passed " + str(winner) + " is the winner.")
    else:
        print(str(test) + " did not pass. try again. should have got " + expected + " but we got " + str(winner))

if __name__=="__main__":

    #tests to see if the program works
    test1=who_is_winner([
            "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
            "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
            "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"])

    checkTests(1,test1, "Yellow")

    test2=who_is_winner([
            "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
            "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
            "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
            "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
            "E_Yellow", "E_Red"
        ])

    checkTests(2,test2,"Yellow")

    test3=who_is_winner([
            "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
            "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
            "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
            "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
            "B_Yellow", "B_Red"
        ])

    checkTests(3,test3,"Red")

    test4=who_is_winner([
            "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
            "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
        ])

    checkTests(4,test4,"Red")

    test5=who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
        ])

    checkTests(5,test5,"Yellow")

    test6=who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"])

    checkTests(6,test6,"Draw")


