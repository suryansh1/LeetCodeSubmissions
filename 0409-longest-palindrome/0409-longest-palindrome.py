from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        counter = Counter(s)

        # Construct palindrome with largest odd letters in the middle and 
        # even letters on each side. 

        # For each letter with odd counts, use all but 1 of that letter
        # to make it an even count and add to palindrome length

        answer = 0
        odd_vals = []
        max_odd_val = 0

        for key, val in counter.items():
            
            if val % 2 == 1 :
                odd_vals.append(val)

            else : 
                answer += val
        
        # if odd_vals == [] : return answer

        return answer + sum(odd_vals) - len(odd_vals) + int(odd_vals != [])
                