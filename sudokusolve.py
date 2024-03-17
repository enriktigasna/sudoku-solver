board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


# Step 1:
# Create adjacency list for board, each 
def generate_adjecency_list(board: list[list[int]]) -> dict:
    output = {}
    
    for i, j in enumerate(board):
        for h, k in enumerate(j):
            edges = []
            # Append all verticals
            for v, n in enumerate(board):
                edges.append((v, h))
            
            # Append all horizontals
            for v, n in enumerate(board[i]):
                edges.append((i, v))
            
            # Find first index of square
            first_square_index = (i-i%3, h-h%3)
            for v in range(9):
                edges.append((first_square_index[0] + v % 3, first_square_index[1] + v//3))

                pass
            # Append all squares
            output[i, h] = edges

    return output

# My own algorithm from leetcode that beats 96.7%
def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        # Check column
        for j in range(9):
            entries = []
            for i in range(9):
                if board[i][j] in entries:
                    return False
                if board[i][j] != ".":
                    entries.append(board[i][j])
        
        # Check row
        for j in range(9):
            entries = []
            for i in range(9):
                if board[j][i] in entries:
                    return False
                if board[j][i] != ".":
                    entries.append(board[j][i])
        
        # Check square
        for i in range(3):
            for j in range(3):
                entries = []
                for h in range(9):
                    if board[i*3+(h//3)][j*3+h%3] in entries:
                        return False
                    if board[i*3+(h//3)][j*3+h%3] != ".":
                        entries.append(board[i*3+(h//3)][j*3+h%3])
        return True

def print_sudoku(board):
    for i, j in enumerate(board):
        if(i%3 == 0):
            print("-------------------------")
        print('| {:1} {:1} {:1} | {:1} {:1} {:1} | {:1} {:1} {:1} |'.format(*j))
    print("-------------------------")

def find_possible_replacements(adjList, board, coords):
    output = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in adjList[coords]:
        current = board[i[0]][i[1]]
        if current in output:
            output.remove(current)
    return output

def findEasiestSolve(adjList, board):
    lowest_number = 9
    for i in range(9):
        for j in board[i]:
            print("h")


adjList = generate_adjecency_list(board)

solvedBoard = board
print_sudoku(board)

# Find . with least possible numbers to replace it
# Set to 1