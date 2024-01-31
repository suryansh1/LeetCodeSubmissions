class Solution:

    def longestSubstring(self, s:str) -> int:

        l = 0

        result = 0

        window = set()

        for r in range(len(s)):

            while s[r] in window:
                window.discard(s[l])
                l += 1

            window.add(s[r])

            result = max(result, r - l + 1)

        return result

    def lengthOfLongestSubstring(self, s: str) -> int:

        return self.longestSubstring(s)
        
        if len(s) in [0,1] : return len(s)

        l, r = 0,0

        # Sliding window
        

        # initialize a window set
        window = set()

        max_length = 1

        # Scan each character
        # while r < len(s) :        

        for r in range(len(s)):

            # Check if new character is in window 
            if s[r] not in window :
                
                #add to window set
                window.add(s[r])          

                # update max_length
                max_length = max(max_length, r-l+1)

                # r += 1                  

            else:
                # Left increments until 
                # s[r] is removed from window

                while s[l] != s[r]:

                    window.remove(s[l])
                    l += 1

                l += 1

                # r += 1
       
        return max_length