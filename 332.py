import heapq
from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights_dict = {}
        for t in tickets:
            if t[0] not in flights_dict:
                flights_dict[t[0]] = [t[1]]
                heapify(flights_dict[t[0]])
            else:
                heappush(flights_dict[t[0]],t[1])
        stack = deque()
        res = []
        stack.append("JFK")
        while stack:
            loc = stack[-1]
            if loc in flights_dict and flights_dict[loc]:
                stack.append(heappop(flights_dict[loc]))
            else:
                res.append(stack.pop())
        return res[::-1]
