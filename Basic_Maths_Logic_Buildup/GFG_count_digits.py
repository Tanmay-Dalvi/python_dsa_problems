# Given a natural number n. You have to find the number of digits in it and return it.

# Examples:

# Input: n = 12
# Output: 2
# Explanation: 12 has 2 digits
# Input: n = 456
# Output: 3
# Explanation: 456 has 3 digits
# Constraints:
# 1 ≤ n ≤ 105

class Solution:
    def countDigits(self, n):
    #  code here 
        num = n
        count = 0
        while (num > 0):
            count += 1
            num = num // 10
        return count