import os

def simple_board():
    print("(Position 1)  |  (Position 2)  |  (position 3)")
    print("----------------------------------------------")
    print("(Position 4)  |  (Position 5)  |  (position 6)")
    print("----------------------------------------------")
    print("(Position 7)  |  (Position 8)  |  (position 9)")

def display_board():
    print(board[1],"|",board[2],"|",board[3])
    print("---------")
    print(board[4],"|",board[5],"|",board[6])
    print("---------")
    print(board[7],"|",board[8],"|",board[9])

# Checks whether any one has won or not
# Returns True if any-one wins
def condition():
    for p in range(1,4,3):
        if(board[p]=='X' and board[p+1]=='X' and board[p+2]=='X'):
            return True
            break
        if(board[p]=='O' and board[p+1]=='O' and board[p+2]=='O'):
            return True
            break
    for p in range(1,4):
        if(board[p]=='X' and board[p+3]=='X' and board[p+6]=='X'):
            return True
            break
        if(board[p]=='O' and board[p+3]=='O' and board[p+6]=='O'):
            return True
            break
    if((board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[3]=='X' and board[5]=='X' and board[7]=='X')):
        return True
    if((board[1]=='O' and board[5]=='O' and board[9]=='O') or (board[3]=='O' and board[5]=='O' and board[7]=='O')):
        return True


flag=False
print("Welcome, to Tic Tac Toe")

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
simple_board()
print()
# display_board()

i=1
while (i<=9):
    if(i%2==0):
        location=int(input("Player 2 :Enter the location, you want to put input :"))
        if(location<0):
            print("invalid location")
        elif(location>9):
            print("Invalid location")
        elif(board[location]=='X'):
            print("Location already Filled...Please Try Again")
        else:
            os.system('cls')
            board[location]='O'
            display_board()
            if (condition()==True):
                flag=True
                print("Player 2 wins")
                break
            else :
                i+=1
    else:
        location=int(input("Player 1 :Enter the location, you want to put input :"))
        if(location<0):
            print("invalid location")
        elif(location>9):
            print("Invalid location")
        elif(board[location]=='O'):
            print("Location already Filled...Please Try Again")
        else:
            os.system('cls')
            board[location]='X'
            display_board()
            if(condition()==True):
                flag=True
                print("Player 1 wins")
                break
            else:                
                i+=1

if(flag==False):
    print("Draw")

int(input("Enter any number to end"))
print("End")
