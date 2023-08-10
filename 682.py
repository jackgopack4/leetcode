# 682. Baseball Game

# Runtime Details
# 43ms
# Beats 95.01% of users with Python3
# Memory Details
# 16.39mb
# Beats 95.28% of users with Python3
'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        runningTotal = 0
        for x in operations:
            if x.isdigit() or x[0] == '-':
                toAppend = int(x)
                record.append(toAppend)
            elif x == '+':
                toAppend = record[-1] + record[-2]
                record.append(toAppend)
            elif x == 'D':
                toAppend = 2* record[-1]
                record.append(toAppend)
            else:
                record.pop()
        return sum(record)
