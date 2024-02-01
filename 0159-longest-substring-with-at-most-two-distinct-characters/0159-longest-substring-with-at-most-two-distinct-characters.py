class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        l = 0

        max_length = 0

        counter = Counter()

        for r in range(len(s)):

            if s[r] in counter :

                counter[s[r]] += 1

                max_length = max(max_length, r - l +1)

            elif len(counter) < 2 :

                counter[s[r]] = 1
                max_length = max(max_length, r - l +1)

            else : 

                while s[l] in counter :

                    counter[s[l]] -= 1

                    if counter[s[l]] == 0 :

                        del(counter[s[l]])

                        l += 1
                        break

                    l += 1

                counter[s[r]] = 1
       
        return max_length

           
                


