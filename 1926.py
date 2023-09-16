from functools import cmp_to_key
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # want to store split point, number of steps to it, and directions remaining
        # can only be a shorter direction to take when there is a split point
        # so we explore all paths and return when no branches remaining
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3
        self.visited = {}
        stack = deque()
        self.count = 0
        self.lowest_exit = 100000
        def distanceFromEdge(coord):
            return min(coord[0],self.width-coord[0]-1)+min(coord[1],self.height-coord[1]-1)

        def compare(item1,item2):
            return distanceFromEdge(item1)-distanceFromEdge(item2)
        #returns incremented two-item list [x,y]
        def move(x:int,y:int,dir:int) -> (int,int):
            if dir == self.UP:
                return (x,y-1)
            elif dir == self.DOWN:
                return (x,y+1)
            elif dir == self.LEFT:
                return (x-1,y)
            else:
                return (x+1,y)
        
        # returns an array of directions to try
        def directionsAvailable(x:int,y:int) -> List[int]:
            res = []
            up = move(x,y,self.UP)
            down = move(x,y,self.DOWN)
            left = move(x,y,self.LEFT)
            right = move(x,y,self.RIGHT)
            if 0 <= up[1] <self.height:
                if self.maze[up[1]][up[0]] == ".":
                    res.append(self.UP)
            if 0 <= down[1]<self.height:
                if self.maze[down[1]][down[0]] == ".":
                    res.append(self.DOWN)
            if 0 <= left[0]<self.width:
                if self.maze[left[1]][left[0]] == ".":
                    res.append(self.LEFT)
            if 0 <= right[0]<self.width:
                if self.maze[right[1]][right[0]] == ".":
                    res.append(self.RIGHT)
            return res
           
        # returns if point is an exit
        def checkIfExit(x:int,y:int) -> bool:
            return x == 0 or x == self.width-1 or y == 0 or y == self.height-1
        
        stack.append((entrance[1],entrance[0],self.count))
        while stack:
            cur_x,cur_y, cur_count = stack.popleft()
            #print('cur x=%d, cur y=%d, count=%d'%(cur_x,cur_y,cur_count))
            if (cur_x,cur_y) not in self.visited:
                self.visited.update({(cur_x,cur_y):cur_count})
            elif self.visited[(cur_x,cur_y)] > cur_count:
                self.visited[(cur_x,cur_y)] = cur_count
            else:
                continue
            if [cur_y,cur_x] != entrance and checkIfExit(cur_x,cur_y):
                if cur_count < self.lowest_exit:
                    self.lowest_exit = cur_count
                    return self.lowest_exit
            else:
                temp_d = [move(cur_x,cur_y,d) for d in directionsAvailable(cur_x,cur_y)]
                temp_d = sorted(temp_d, key=cmp_to_key(compare))
                for nex_x,nex_y in temp_d:
                    nex_count = cur_count + 1
                    #if (nex_x,nex_y) not in self.visited or self.visited[(nex_x,nex_y)]>nex_count:
                    stack.append((nex_x,nex_y,nex_count))
        return self.lowest_exit if self.lowest_exit != 100000 else -1
