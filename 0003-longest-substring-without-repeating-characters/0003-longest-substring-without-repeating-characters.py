class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "" : return 0

        max_length = 1

        left, right = 0, 0

        substring = set({s[0]})

        while right < len(s)-1:

            # Expanding window from right
            right += 1

            # If new character is not in substring
            # Add to substring and increase max_length
            if s[right] not in substring :
                 
                substring.add(s[right])
                if right - left + 1 > max_length : max_length = right - left + 1

            # If new character is present in substring
            # 
            else :

                while s[left] != s[right] : 
                    
                    substring.remove(s[left])
                    left += 1

                left += 1

        return max_length

        