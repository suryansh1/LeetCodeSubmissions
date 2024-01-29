class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # counter = Counter(s)

        if len(s) == 1 or len(s) == 2 : return True

        left, right = 0, len(s) - 1

        while left <= right :

            if s[left] == s[right] :

                left +=1
                right -=1

                continue

            elif s[left+1:right+1] == s[left+1:right+1][::-1] :

                return True

            elif s[left:right] == s[left:right][::-1] :

                return True

            return False
        
        
        return True