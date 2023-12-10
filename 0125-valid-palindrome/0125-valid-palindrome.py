class Solution:

    def isPalindromeExtraSpace(self, s:str) -> bool:

        result = ""

        for char in s :
            if char.isalnum(): result += char.lower()

        return result == result[::-1]


    def isPalindromeListComprehension(self, s:str) -> bool:

        result = [char for char in s.lower() if char.isalnum()]

        return result == result[::-1]

    def isPalindromeTwoPointers(self, s:str) -> bool:

        l, r = 0, len(s) - 1


        while(l < r):

            if not s[l].isalnum() :
                l+=1
                continue
            
            if not s[r].isalnum() :
                r-=1
                continue

            if s[l].lower() != s[r].lower() :
                return False

            l+=1
            r-=1

        return True

    def isPalindrome(self, s: str) -> bool:
        
        # return self.isPalindromeExtraSpace(s)

        return self.isPalindromeTwoPointers(s)


        