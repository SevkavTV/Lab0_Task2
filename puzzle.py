'''
Lab 0, Task 2. Archakov Vsevolod
'''


def validate_lst(element: list) -> bool:
    '''
    Return True if element is valid and False in other case
    >>> validate_lst([1, 1])
    False
    '''
    for item in range(1, 10):
        if element.count(item) > 1:
            return False

    return True


def valid_row_column(board: list) -> bool:
    '''
    Return True if all rows and columns are valid and False in other case
    >>> valid_row_column([ \
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****" \
])
    False
    '''
    for row in range(9):
        row_lst = []
        column_lst = []

        # iterate both through all columns and rows
        for column in range(9):
            if board[row][column] != '*' and board[row][column] != ' ':
                row_lst.append(int(board[row][column]))

            if board[column][row] != '*' and board[column][row] != ' ':
                column_lst.append(int(board[column][row]))

        # validate lists (column, row) with values
        if not validate_lst(row_lst) or not validate_lst(column_lst):
            return False

    return True


def valid_angle(board: list) -> bool:
    '''
    Return True if all colors are valid and False in other case
    >>> valid_angle([ \
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****" \
])
    True
    >>> valid_angle([ \
"**** ****", \
"***11****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****" \
])
    False
    '''
    for row in range(4, -1, -1):
        angle = []

        # iterate through each color in a column
        for column in range(4 - row, 9 - row):
            if board[column][row] != '*' and board[column][row] != ' ':
                angle.append(int(board[column][row]))

        # iterate through each color in a row
        for column in range(row + 1, row + 5):
            if board[8 - row][column] != '*' and board[8 - row][column] != ' ':
                angle.append(int(board[8 - row][column]))

        if not validate_lst(angle):
            return False

    return True


def validate_board(board: list) -> bool:
    '''
    Return True if board is valid and False in other case
    >>> validate_board([ \
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****" \
])
    False
    '''
    if not valid_row_column(board) or not valid_angle(board):
        return False

    return True
