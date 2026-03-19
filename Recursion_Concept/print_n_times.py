class Solution:
    def func(self, i, n):
        # Base case: once i exceeds n, stop recursion
        if i > n:
            return
        print("GFG", end=" ")   # work done before deeper call
        self.func(i + 1, n)     # recursive call with next index

    def printGfg(self, n):
        # Kick-off with i = 1
        self.func(1, n)