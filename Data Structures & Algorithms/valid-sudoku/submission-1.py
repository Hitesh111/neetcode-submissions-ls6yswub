class Solution:
    def isValidSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                num = int(val)
                bit = 1 << (num - 1)

                box = (i // 3) * 3 + (j // 3)

                # check if bit already set
                if (rows[i] & bit) or (cols[j] & bit) or (boxes[box] & bit):
                    return False

                # set the bit
                rows[i] |= bit
                cols[j] |= bit
                boxes[box] |= bit

        return True