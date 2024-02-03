class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1) : return False

        counter = [0]*26

        for char in s1 : counter[ord(char) - ord('a')] += 1

        candidate = [0] * 26

        for char in s2[:len(s1)] : candidate[ord(char) - ord('a')] += 1
        
        if counter == candidate : return True

        left = 0

        for right in range(len(s1), len(s2)) : 

            candidate[ord(s2[left]) - ord('a')] -= 1

            left += 1

            candidate[ord(s2[right]) - ord('a')] += 1

            if counter == candidate : return True

        return False

        # counter, left right cand
        # a=1 b=1,  0   2   e=1 i=1
                #   1        i=1
                #   1   2     i=1, d=1
                #   1   3
                #   2   3   d=1
                #   2   3   d=1, b=1
                #   2   4   b=1
                #   3   4   b=1, a=1    

