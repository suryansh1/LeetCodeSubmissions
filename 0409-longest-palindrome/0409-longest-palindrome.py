from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        counter = Counter(s)

        # Construct palindrome with largest odd letters in the middle and 
        # even letters on each side

        answer = 0
        odd_vals = []
        max_odd_val = 0

        for key, val in counter.items():
            
            if val % 2 == 1 :
                odd_vals.append(val)

            else : 
                answer += val
        
        if odd_vals == [] : return answer

        return answer + sum(odd_vals) - len(odd_vals) + 1
                