class Solution:
    def average(self, salary: List[int]) -> float:
        largest = 1000
        smallest = 1000000
        total = 0
        for s in salary:
            if s > largest:
                largest = s
            if s < smallest:
                smallest = s
            total += s
        total -= largest
        total -= smallest
        return total / (len(salary)-2)
