# 🧩 Sudoku Solver & Teaching Assistant

A command-line **Sudoku solver** written in Python that not only solves puzzles, but also **teaches you how to solve them like a human** 🧠✏️.

This program applies common human Sudoku strategies step-by-step, explains each move, and only falls back to brute force when human logic is exhausted.

---

## 📚 Background

Sudoku is a 9×9 number puzzle where the goal is to fill the grid so that:

- Each **row** contains digits **1–9**
- Each **column** contains digits **1–9**
- Each **3×3 subgrid** contains digits **1–9**

Humans solve Sudoku using logic and pattern recognition — not guessing.  
This project focuses on **human-style solving techniques**, with clear explanations printed as the puzzle is solved.

---

## 🎯 Project Goals

✔️ Read a Sudoku puzzle from a file  
✔️ Solve the puzzle correctly  
✔️ Explain each solving step in human-friendly language  
✔️ Save the solved puzzle to a new file  
✔️ Fall back to brute force **only if needed**

---

## 📁 Project Structure

```kotlin

├── solve.py
├── puzzle.txt  
├── solve_puzzle.txt
└── README.md
```

---

## 🛠️ How to Run the Program

```bash
python3 solve.py path/to/puzzle.txt -o path/to/solved_puzzle.txt
```

**Example:**
```bash
python3 solve.py puzzle.txt -o solved_puzzle.txt
```

---

## 📄 Input File Format

* The puzzle file must contain **9 lines**
* Each line has **9 digits**
* Use `0` to represent empty cells
* Whitespace is ignored

**Example Input (`puzzle.txt`)**

```
9 6 2 0 7 8 5 0 0
1 0 5 0 0 9 3 0 0
3 0 0 0 0 0 8 2 0
0 0 1 0 0 0 0 7 0
6 0 0 0 5 0 0 0 8
0 0 0 6 0 3 9 0 5
0 1 8 0 0 5 0 0 0
0 0 6 8 3 2 7 0 1
7 5 3 1 9 0 4 8 0
```

## 📤 Output File Format

The solved puzzle is written in the **same format**:

```python-repl
9 6 2 4 7 8 5 1 3
1 8 5 2 6 9 3 4 7
3 7 4 5 1 0 8 2 9
...
```

---

## 🧠 Human Solving Strategies Used

This Sudoku solver prioritizes **human-style logical techniques** before attempting any brute-force guessing. 
Each strategy mirrors how a real person would approach the puzzle and is explained step-by-step as the program runs.

### ✏️ Pencil Mark Logic (Naked Singles) 
> If a cell has only **one possible number**, it must be that number.

**Example output:**

```psql
Pencil Mark Logic: On row 4 and column 2 can ONLY be 9.
```

### 🔍 Scanning Logic (Hidden Singles)
> If a number can only go in **one place in a row**, it must go there.

**Example output:**

```psql
Scanning Logic: In Row 7, the number 6 can only go in Column 3.
```

After each step, the board is printed so you can **see the progress visually** 👀
Newly filled numbers are shown in **blue**.

---

## 🖥️ Visual Board Display

* `.` represents empty cells
* 3×3 boxes are clearly separated
* New values are highlighted in **blue**
* Makes it easy to follow along while learning

---

## 🤖 Brute Force Backup (Last Resort)

If human logic cannot finish the puzzle:
* The solver switches to **backtracking**
* This guarantees a solution if one exists
* Clearly announced in the output:

```css
Human logic stuck. Switching to Brute Force to finish...
```

---

## 🧪 Error Handling

* Invalid or unreadable files are safely handled
* The program exits cleanly with helpful messages
* Confirms when the solution is successfully saved ✅