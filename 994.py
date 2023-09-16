from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count oranges
        # add rottens to set
        # each step, add to set if not already there, break when size = count
        FRESH = 1
        ROTTEN = 2
        def countOranges(grid,orange):
            return sum(x.count(orange) for x in grid)
        def freshNext(grid,x,y):
            res = []
            if x > 0 and grid[y][x-1] == 1:
                res.append((x-1,y))
            if x < len(grid[0])-1 and grid[y][x+1] == 1:
                res.append((x+1,y))
            if y > 0 and grid[y-1][x] == 1:
                res.append((x,y-1))
            if y < len(grid)-1 and grid[y+1][x] == 1:
                res.append((x,y+1))
            return res
        fresh_start = countOranges(grid,FRESH)
        if fresh_start == 0:
            return 0
        rotten_start = countOranges(grid,ROTTEN)
        if rotten_start == 0:
            return -1
        self.rotten = set()
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 2:
                    self.rotten.add((i,j))
        q = deque()
        q.extend((r,0) for r in self.rotten)
        t = 0
        while q and len(self.rotten)<fresh_start+rotten_start:
            cur_oranges = []
            while q and q[0][1] == t:
                cur_oranges.append(q.popleft())
            t += 1
            for tmp, time in cur_oranges:
                next_oranges = freshNext(grid,tmp[0],tmp[1])
                for n in next_oranges:
                    if n not in self.rotten:
                        self.rotten.add(n)
                        q.append((n,time+1))
                

        if len(self.rotten)<fresh_start+rotten_start:
            return -1
        return t
