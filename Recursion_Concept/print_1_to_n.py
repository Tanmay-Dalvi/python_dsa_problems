class Solution:
    def func(self, i, n):
        if i > n:  # Base case: stop recursion when i exceeds n
            return
        print(i, end=" ")  # Print the current number
        self.func(i + 1, n)  # Recursive call with the next number

    def printNos(self, n):
        self.func(1, n)  # Start recursion from 1 to n