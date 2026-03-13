# You are given a 3-digit number n, Find whether it is an Armstrong number or not.

# An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

# Examples:

# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. 
# Input: n = 372
# Output: false
# Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. 
# Input: n = 100
# Output: false
# Explanation: 100 is not an Armstrong number since 13 + 03 + 03 = 1. 
# Constraints:
# 100 ≤ n <1000 

#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        num = n
        total = 0
        number_of_digits = len(str(n))
        
        while (num >  0):
            last_digit = num % 10
            total = total + (last_digit ** number_of_digits)
            num = num // 10
        return total == n