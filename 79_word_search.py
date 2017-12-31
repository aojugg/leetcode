class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # time limited exceed
        def search(visit,board,word,x,y):
            if not word:
                return True
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or word[0]!=board[x][y]:
                return False
            if visit[x][y]==0:
                visit[x][y]=1
                    #print(board[x][y])
                    #print(x,y)
                res=search(visit,board,word[1:],x+1,y) \
                    or search(visit,board,word[1:],x-1,y) \
                    or search(visit,board,word[1:],x,y+1) \
                    or search(visit,board,word[1:],x,y-1) 
            else:
                return False
        # remember reset the visit matrix
            visit[x][y]=0
            return res
            
        
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            for j in range(n):
                visit=[[0]*n for i in range(m)]
                if search(visit,board,word,i,j):
                    return True
        return False


#**********************************************************************************
class Solution:
    #449ms
    #58.64%
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

# check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

############################################################################
class Solution:
    #282ms

    #91.36%
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False
                    
    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " " # indicate used cell
        # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_helper(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False
