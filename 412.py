# 412. Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            divThree = False
            divFive = False
            if i % 3 == 0: divThree = True
            if i % 5 == 0: divFive = True
            if divThree and divFive: result.append("FizzBuzz")
            elif divThree: result.append("Fizz")
            elif divFive: result.append("Buzz")
            else: result.append(str(i))
        return result
