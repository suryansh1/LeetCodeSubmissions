class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 1 : return 1

        l = 0

        max_length = 0

        counter = Counter()

        for r in range(len(s)) :

            if s[r] in counter : counter[s[r]] += 1
            else : counter[s[r]] = 1

            while r - l + 1 - max(counter.values()) > k :
                
                counter[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length


        

        