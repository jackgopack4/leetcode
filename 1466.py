class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create dict for each city
        self.adj = [[] for _ in range(n)]
        self.count = 0
        self.n = n
        for src,dst in connections:
            self.adj[src].append((dst,1))
            self.adj[dst].append((src,0))

        def dfs():
            stack = []
            visited = set()
            stack.extend(self.adj[0])
            self.adj[0].clear()
            prev = 0
            visited.add(prev)
            while stack and len(visited) < self.n:
                cur, val = stack.pop()
                if cur not in visited and prev != cur:
                    visited.add(cur)
                    self.count += val
                stack.extend(self.adj[cur])
                self.adj[cur].clear()
                prev = cur
        dfs()
        return self.count
