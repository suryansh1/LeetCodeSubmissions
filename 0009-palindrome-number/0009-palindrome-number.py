class Solution:

    def isPalindrome_extraSpace(self, x: int) -> bool:

        digits = []

        while x :

            digits.append(x%10)

            x = x//10

            # print(digits)

        return digits == digits[::-1]

    def isPalindrome_reverse(self, x: int) -> bool:

        temp = x

        reverse = 0

        while temp:

            reverse *=10
            reverse += temp%10

            temp //=10
        
        return x == reverse

    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 : return False

        return str(x) == str(x)[::-1]

        # return self.isPalindrome_reverse(x)

        # return self.isPalindrome_extraSpace(x)

