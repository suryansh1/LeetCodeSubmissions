class Solution:
    
    def lengthOfLongestSubstringSet(self, s: str) -> int:

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
                max_length = max(max_length, right - left + 1)

            # If new character is present in substring
            # remove leftmost character and shorten substring
            # until we have an all unique substring including right
            else :

                while s[left] != s[right] : 
                    
                    substring.remove(s[left])
                    left += 1

                left += 1

        return max_length

    def lengthOfLongestSubstringDict(self, s: str) -> int:

        if s == "" : return 0

        max_length = 0

        left, right = 0, 0

        # Dict to store index of left
        myDict = {}


        for right in range(len(s)):

            if s[right] in myDict :
                 
                left = max(myDict[s[right]], left)
                

            max_length = max(max_length, right - left + 1)
            
            myDict[s[right]] = right + 1
            
        return max_length
        
    def lengthOfLongestSubstring(self, s: str) -> int:

        return self.lengthOfLongestSubstringDict(s)

        if s == "" : return 0

        if len(s) == 1: return 1

        substring = set()        

        left, right = 0, 1

        max_length = 1

        substring.add(s[left])

        while right < len(s) - 1:

            if s[right] in substring :

                while s[left] != s[right] : 
                    
                    substring.remove(s[left])

                    left += 1

                left += 1
                right += 1

            else :

                substring.add(s[right])                

                max_length = max(max_length, right - left + 1)

                right += 1

        return max_length






        