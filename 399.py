from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.variables = defaultdict(dict)
        res = []
        self.visited = set()
        for idx, (v1, v2) in enumerate(equations):
            self.variables[v1][v2] = values[idx]
            self.variables[v2][v1] = 1 / values[idx]
        def dfs(x,y):
            if x not in self.variables or y not in self.variables:
                return -1.0
            if y in self.variables[x]:
                return self.variables[x][y]
            for i in self.variables[x]:
                if i not in self.visited:
                    self.visited.add(i)
                    calc = dfs(i,y)
                    if calc == -1.0:
                        continue
                    else:
                        return self.variables[x][i]*calc
            return -1.0
        for num, denom in queries:
            res.append(dfs(num,denom))
            self.visited.clear()
        return res
