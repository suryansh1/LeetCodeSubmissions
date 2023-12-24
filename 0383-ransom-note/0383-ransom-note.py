from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if (len(ransomNote) > len(magazine)) : return False

        ransomNoteCounter = Counter(ransomNote)

        magazineCounter = Counter(magazine)

        for pair in ransomNoteCounter :

            if pair[0] not in magazineCounter : return False

            if magazineCounter[pair[0]] < ransomNoteCounter[pair[0]] : return False

        return True