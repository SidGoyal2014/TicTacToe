import os 
def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])


def condition():
    for p in range(0,4):
        if(board[p]=='X' and board[p+1]=='X' and board[p+2]=='X'):
            return True
            break
        if(board[p]=='X' and board[p+3]=='X' and board[p+6]=='X'):
            return True
            break
    for p in range(0,4):
        if(board[p]=='O' and board[p+1]=='O' and board[p+2]=='O'):
            return True
            break
        
        if(board[p]=='O' and board[p+3]=='O' and board[p+6]=='O'):
            return True
            break
    if((board[0]=='X' and board[4]=='X' and board[8]=='X') or (board[2]=='X' and board[4]=='X' and board[6]=='X')):
        return True
    if((board[0]=='O' and board[4]=='O' and board[8]=='O') or (board[2]=='O' and board[4]=='O' and board[6]=='O')):
        return True


flag=False
print("Welcome, to Tic Tac Toe")

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board()

i=1
while (i<=9):
    if(i%2==0):
        location=int(input("Player 2 :Enter the location, you want to put input :"))
        if(location<0):
            print("invalid location")
        elif(location>8):
            print("Invalid location")
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
        elif(location>8):
            print("Invalid location")
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

