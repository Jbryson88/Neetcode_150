class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = 0
            
        for idx in range(len(s)-1, -1, -1):
            if i == 0 and s[idx] == " ":
                continue
            if i != 0 and s[idx] == " ":
                break
            i += 1

        return i