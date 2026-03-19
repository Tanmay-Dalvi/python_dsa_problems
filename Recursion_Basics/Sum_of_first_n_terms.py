class Solution:
    def func(self, num):
        # Base case: the sum of the first 1 term is simply 1³ = 1
        if num == 1:
            return 1
        # Recursive step: add the current cube and recurse on num - 1
        return num**3 + self.func(num - 1)

    def sumOfSeries(self, n):
        # Entry point: delegate work to the recursive helper
        return self.func(n)