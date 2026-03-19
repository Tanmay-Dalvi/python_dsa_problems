class Solution:
    # helper that returns F(num)
    def func(self, num):
        if num <= 1:            # base cases: F(0)=0, F(1)=1
            return num
        # recursive calls for previous two numbers
        return self.func(num - 1) + self.func(num - 2)

    def fib(self, n: int) -> int:
        # simply delegate to the helper
        return self.func(n)