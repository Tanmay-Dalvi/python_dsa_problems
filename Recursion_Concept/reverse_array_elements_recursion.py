class Solution:
    def func(self, arr, left, right):
        # Base case: If left index is greater than or equal to right index, return
        if left >= right:
            return
        
        # Swap the elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        self.func(arr, left + 1, right - 1)

    def reverseSubArray(self, arr, l, r):
        self.func(arr, l - 1, r - 1)
        return arr