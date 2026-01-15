import argparse
import sys

#=================== BOARD SET UP AND TOOLS ==========================
def read_board(file_path):
    """
    Reads the file and converts it into a list of lists.
    e.g. input file: "0 2 0"
    e.g. output : [[0, 2, 0]]
    """
    board = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                row = [int(c) for c in line if c.isdigit()]

                if len(row) == 9:
                    board.append(row)

        return board
    
    except Exception as e:
        print(f"Error reading file {e}")
        sys.exit(1)

def print_board(board, original=None):
    """
    Prints the board nicely with grid lines.
    If 'original' is provided, new numbers are printed in BLUE.
    """
    BLUE = "\033[94m"
    RESET = "\033[0m"

    print("-" * 25)

    for i in range(9):
        row_str = "| "

        for j in range(9):
            val = board[i][j]
            
            if val == 0:
                val_str = "."
            else:
                if original and original[i][j] == 0:
                    val_str = f"{BLUE}{val}{RESET}"
                else:
                    val_str = str(val)

            row_str += val_str
            
            if (j + 1) % 3 == 0:
                row_str += " | "
            else:
                row_str += " "
        print(row_str)

        if (i + 1) % 3 == 0:
            print("-" * 25)

    print("\n")

def write_solution(board, file_path):
    """Saves the final board to a text file."""
    try:
        with open(file_path, 'w') as f:
            for row in board:
                row_str = " ".join(str(num) for num in row)
                f.write(row_str + "\n")
        print(f"✅ Solution successfully saved to {file_path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def get_candidates(board, row, col):
    """
    Returns a set of valid numbers for a specific cell.
    Example: if row has 1, col has 2, box has 3, returns {4, 5, 6, 7, 8, 9}
    It's more like pencil markers
    """
    candidates = set()

    for i in range(1, 10):
        candidates.add(i)

    for c in range(9):
        current_val = board[row][c]
        if current_val in candidates:
            candidates.remove(current_val)
    
    for r in range(9):
        current_val = board[r][col]
        if current_val in candidates:
            candidates.remove(current_val)
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            current_val = board[r][c]
            if current_val in candidates:
                candidates.remove(current_val)
    
    return candidates

#==================== THE HUMAN STRATEGIES ==============================
def find_hidden_single(board):
    """
    STRATEGY: Scanning the boxes to see which box doesn't have that number (Long press 1, then 2...)
    We check if a specific number (e.g. 7) has only one valid spot in a row.
    """
    for num in range(1 ,10):
        for r in range(9):
            if num in board[r]:
                continue

            possible_cols = []
            for c in range(9):
                if board[r][c] == 0:
                    candidates = get_candidates(board, r, c)

                    if num in candidates:
                        possible_cols.append(c)
            
            if len(possible_cols) == 1:
                col = possible_cols[0]
                board[r][col] = num
                print(f"Scanning Logic: In Row {r + 1}, The number {num} can only go in Column {col + 1}.")
                
                input("Press Enter (↩) to continue ...")

                return True
    return False

def find_naked_singles(board):
    """
    STRATEGY: Check Pencil Marks.
    We look at every empty square. If get_candidates() returns only 1 number,
    we fill it in immediately.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                candidates = get_candidates(board, r, c)
            
                if len(candidates) == 1:
                    val = list(candidates)[0]
                    board[r][c] = val
                    print(f"Pencil Mark Logic: On row {r + 1} and column {c + 1} can ONLY be {val}.")
                    
                    return True 
    return False

#=================== THE COMPUTER BACKUP ===============================
def find_empty_cell(board):
    """Helper: Finds the first empty spot (0). Returns (row, col) or None."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def backtrack_solve(board):
    """
    STRATEGY: "When I get stuck, I guess."
    """
    empty = find_empty_cell(board)
    if not empty:
        return True 
    
    row, col = empty

    for guess in range(1, 10):
        candidates = get_candidates(board, row, col)
        if guess in candidates:
            board[row][col] = guess
            
            if backtrack_solve(board):
                return True
            
            board[row][col] = 0
            
    return False

#==================== THE MAIN LOOP ================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to puzzle file")
    parser.add_argument("-o", "--output", required=True, help="Path to save solution")
    args = parser.parse_args()

    print(f"Reading from: {args.input_file}")
    board = read_board(args.input_file)
    
    original_board = [row[:] for row in board]

    print("Initial Board: ")
    print_board(board, original_board)

    stuck = False
    while not stuck:
        if find_hidden_single(board):
            print_board(board, original_board)
            continue

        if find_naked_singles(board):
            print_board(board, original_board)
            continue
    
        stuck = True

    if find_empty_cell(board) is None:
        print("Solved using ONLY Human Logic! (You are a genius!!!)")
        write_solution(board, args.output)
    else:
        print("Human logic stuck. Switching to Brute Force to finish...")
        if backtrack_solve(board):
            print("Brute Force successful.")
            print_board(board, original_board)
            write_solution(board, args.output)
        else:
            print("Error: This puzzle cannot be solved.")

if __name__ == "__main__":
    main()