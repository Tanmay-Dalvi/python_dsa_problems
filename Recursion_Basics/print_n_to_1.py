class Solution:
    def func(self, num):
        # Base Case: when num goes below 1, stop recursion
        if num < 1:
            return
        print(num, end=" ")    # print current number
        self.func(num - 1)     # recurse on the next smaller number

    def printNos(self, n):
        # Driver method that kicks off recursion
        self.func(n)