from pathlib import Path
from Board import Board

boardRows = []
boardColumns = []

##### READ FILE AND CREATE BOARDS OF ROWS
with open('InputBoards.txt', 'r') as f:
    matrix = []
    for line in f:
        if line != "":
            row = [int(num) for num in line.split()]
            if row:
                matrix.append(row)
        else:
            matrices = matrices.append(matrix)
boardRows = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

##### CREATE BOARDS OF COLUMNS
for k in range(len(boardRows)):
    columns = []
    for j in range(5):
        column = []
        for i in range(5):
            column.append(boardRows[k][i][j])
        columns.append(column)
    boardColumns.append(columns)

##### CREATE A LIST OF TYPE BOARD: EACH BOARD HAS 2 FORMS: ROW FORM, COLUMN FORM & HAS ID
boardList: list[Board] = []
for i in range(len(boardRows)):
    currentBoard = Board()
    currentBoard.listRows = boardRows[i]
    currentBoard.listColumns = boardColumns[i]
    currentBoard.ID = i
    boardList.append(currentBoard)

##### READ DRAWN NUMBERS INTO LIST
content = Path('InputDrawNumber.txt').read_text()
drawNumbers = list(map(int, content.split(",")))

##### FIND THE LAST WINNER
i = 0
while len(boardList) > 0:

    lastDrawnNumber = drawNumbers[i]
    j = 0
    while j < len(boardList):
        for k in range(5):  # always 5 rows and 5 columns
            if lastDrawnNumber in boardList[j].listRows[k]:
                boardList[j].listRows[k].remove(lastDrawnNumber)
            if lastDrawnNumber in boardList[j].listColumns[k]:
                boardList[j].listColumns[k].remove(lastDrawnNumber)

        k = 0

        while k < 5:
            deletedBoards = 0
            if len(boardList[j].listRows[k]) == 0 or len(boardList[j].listColumns[k]) == 0:
                if len(boardList) == 1:  # if one left, print winning number and id
                    print("last drawn number:", lastDrawnNumber)
                    print("last board is ", boardList[j].ID + 1)
                    print("the final score is:",
                          lastDrawnNumber * (sum(boardList[j].listRows[0]) + sum(boardList[j].listRows[1]) + sum(
                              boardList[j].listRows[2]) + sum(boardList[j].listRows[3]) + sum(
                              boardList[j].listRows[4])))

                boardList.remove(boardList[j])
                deletedBoards = 1
                k = 100  # out of while, board deleted
            else:
                k += 1
        if deletedBoards == 0:
            j += 1
    i += 1
