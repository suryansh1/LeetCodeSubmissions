class Solution:

    def check_palindrome(self, s:str) -> str:


        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        
        # counter = Counter(s)

        if len(s) == 1 or len(s) == 2 : return True

        left, right = 0, len(s) - 1

        while left <= right :

            if s[left] == s[right] :

                left +=1
                right -=1

                continue

            elif self.check_palindrome(s[left+1:right+1]) or self.check_palindrome(s[left:right]) :

                return True

            return False
        
        
        return True