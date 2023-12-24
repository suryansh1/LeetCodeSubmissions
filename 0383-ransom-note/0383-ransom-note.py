from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if (len(ransomNote) > len(magazine)) : return False

        ransomNoteCounter = Counter(ransomNote)

        magazineCounter = Counter(magazine)

        for char in ransomNoteCounter.keys() :

            if char not in magazineCounter : return False

            if magazineCounter[char] < ransomNoteCounter[char] : return False

        return True