class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    print(seen)
                    print(num)
                    return False
                else:
                    seen.add(num)
        
        for x in range(9):
            seen = set()
            for y in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in seen:
                    print(seen)
                    print(x,y)
                    return False
                else:
                    seen.add(board[y][x])

        for x in range(3):
            for y in range(3):
                seen = set()
                for z in range(9):
                    if board[(z%3)+(y*3)][(z//3)+(x*3)] == ".":
                        continue
                    if board[(z%3)+(y*3)][(z//3)+(x*3)] in seen:
                        print(seen)
                        print(x,y,z)
                        #print(((z%3)+(y*3))((z//3)+(x*3)))
                        return False
                    else:
                        seen.add(board[(z%3)+(y*3)][(z//3)+(x*3)])

        return True
