class Solution:
    def slope(self,coord1,coord2):
        rise = coord2[1]-coord1[1]
        run = coord2[0]-coord1[0]
        if run != 0:
            return rise / run
        else:
            return 1000000000000000
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = self.slope(coordinates[1],coordinates[0])
        for i in range(2,len(coordinates)):
            if self.slope(coordinates[i],coordinates[i-1]) != slope:
                return False
        return True
