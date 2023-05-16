# fungsi print board
def printBoard(board):
    '''ini adalah fungsi print board

    Args:
        board (dict) : dictionary of all slots in the board
    '''
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# fungsi play tic tac toe
def playTictactoe(val1,val2):
    '''ini adalah play tic tac toe

    Args:
        val1 (str) : assigned value from player 1
        val2 (str) : assigned value from player 2
    '''
    printBoard(board)
    for i in range(len(board)):
        while True:
            slot = input('Select blank spot: ')
            if board[slot] == ' ':
                break
            else:
                print('slot sudah ada isinya, silahkan pilih spot lain!')

        if i % 2 == 0:
            board[slot] = val1
        else:
            board[slot] = val2
        printBoard(board)

if __name__ == "__main__":
    board = {
        'top-L': ' ',
        'top-M': ' ',
        'top-R': ' ',
        'mid-L': ' ',
        'mid-M': ' ',
        'mid-R': ' ',
        'low-L': ' ',
        'low-M': ' ',
        'low-R': ' '
    }

    playTictactoe('X','O')