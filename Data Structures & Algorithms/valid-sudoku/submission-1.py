class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(0 //3)
        seen_row = set()
        seen_column = set()
        seen_subbox  = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue # no sudoku char
                
                if (r, board[r][c]) in seen_row:
                    return False
                seen_row.add((r, board[r][c]))

                if (c, board[r][c]) in seen_column:
                    return False
                seen_column.add((c, board[r][c]))

                if((board[r][c], (r // 3, c // 3))) in seen_subbox:
                    print((board[r][c], (r // 3, c // 3)), r, c)
                    return False
                seen_subbox.add((board[r][c], (r // 3, c // 3)))


        return True