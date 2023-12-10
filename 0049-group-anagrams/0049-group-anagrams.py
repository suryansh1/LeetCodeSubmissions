

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        # key str(Counter object), value = [strings]
        myDict = {}

        ctr0 = [0]*26

        for s in strs :

            ctr = [0]*26

            for char in s:
                ctr[ord(char) - ord('a')] += 1                        

            if tuple(ctr) in myDict:
                myDict[tuple(ctr)].append(s)

            else:
                myDict[tuple(ctr)] = [s]

        # print(myDict)

        return myDict.values()

