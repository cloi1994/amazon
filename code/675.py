class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
        tree = []
        
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] != 0:
                    tree.append([forest[i][j],i,j])
        
        def myCmp(x,y):
            return x[0] - y[0]
            
        
        tree.sort(cmp=myCmp)
                
        start,end = 0,0
        
        steps = 0
        
        for t in tree:
            targetX, targetY = t[1],t[2]
            curStep = self.bfs(forest,start,end,targetX,targetY)
            
            if curStep == -1:
                return -1
            
            steps += curStep
            
            start = targetX
            end = targetY
        
        return steps
        
        
    def bfs(self,forest,start,end,targetX,targetY):
        
        
        
        if start == targetX and end == targetY:
            return 0
        
        q = [[start,end]]
        
        step = 0
        
        visited = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
        
        while q != []:
            
            step += 1
            
            for _ in range(len(q)):
                curX, curY = q.pop(0)
                
                for d in [[0,1],[1,0],[-1,0],[0,-1]]:
                    
                    nextX = curX + d[0]
                    nextY = curY + d[1]
                    
                    if nextX == targetX and nextY == targetY:
                        return step
                    
                    if nextX < 0 or nextY < 0 or nextX >= len(forest) or nextY >= len(forest[0]):
                        continue
                
                    if forest[nextX][nextY] == 0 or visited[nextX][nextY]:
                        continue
                        
                    visited[nextX][nextY] = 1
                    q.append([nextX,nextY])
                
                
        return -1
            
            
        
        
        
