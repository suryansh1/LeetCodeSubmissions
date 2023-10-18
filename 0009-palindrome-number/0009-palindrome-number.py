from math import floor
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 : return False

        num = x
        rev = 0
        
        while num:
            rev *= 10
            rev += num %10
            
            num = floor(num/10)
            # print (rev, num)

        
        return rev == x