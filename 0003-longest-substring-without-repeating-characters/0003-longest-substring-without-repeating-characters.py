class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) in [0,1] : return len(s)

        l, r = 0,1

        # Sliding window
        

        # initialize a window set
        window = set(s[l])

        max_length = 1

        # Scan each character
        while r < len(s) :        

            # Check if new character is in window 
            if s[r] not in window :
                
                #add to window set
                window.add(s[r])          

                # update max_length
                max_length = max(max_length, r-l+1)

                r += 1                  

            else:
                # Left increments until 
                # s[r] is removed from window

                while s[l] != s[r]:

                    window.remove(s[l])
                    l += 1

                l += 1

                r += 1


                # right increments until 
                # we find the first character not in window

                # while r < len(s) and s[r] in window:
                    
                    # r += 1

                # if r == len(s) : break
                
                # left = index of the first character not in window   
                # l = r - 1
                # r = l + 1

                # window = set(s[l])                        
        
        return max_length