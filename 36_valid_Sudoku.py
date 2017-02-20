class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            tem=[]
            for j in range(len(board)):
                if board[i][j]==".":
                    continue
                else:
                    if board[i][j] not in tem:
                        tem.append(board[i][j])
                    else:
                        return False
        for i in range(9):
            tem=[]
            for j in range(9):
                if board[j][i]=='.':
                    continue
                else:
                    if board[j][i] not in tem:
                        tem.append(board[j][i])
                    else:
                        return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                tem=[]
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if board[row][col]==".":
                            continue
                        else:
                            if board[row][col] not in tem:
                                tem.append(board[row][col])
                            else:
                                return False
        return True
