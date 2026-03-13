# Find the number of factors for a given integer n.

#  Examples:

# Input: n = 5
# Output: 2
# Explanation: 5 has 2 factors 1 and 5
# Input: n = 25
# Output: 3
# Explanation: 25 has 3 factors 1, 5, 25 
# Constraints:
# 1 ≤ n ≤ 105

class Solution:
    def countFactors(self, n):
        count = 0
        i = 1
        
        while i * i <= n:
            if n % i == 0:
                if i == n // i:
                    count += 1
                else:
                    count += 2
            i += 1
        
        return count