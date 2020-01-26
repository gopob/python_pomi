import random

board = list(range(1, 10))
counter = 0


def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def take_input(player_token):
    global counter
    valid = False
    while not valid:
        if player_token == 'X':
            if counter == 0:
                player_answer = 5
            else:
                player_answer = random.randint(1, 9)
        else:
            player_answer = int(input("Enter your move" + counter+" "))
        try:
            player_answer = int(player_answer)
        except:
            print("Input error. Check the value")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("The cell is already taken")
        else:
            print("Invalid input. Enter a number from 1 to 9")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    global counter
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            temp = check_win(board)
            if temp:
                print(temp, "won !")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    draw_board(board)


main(board)