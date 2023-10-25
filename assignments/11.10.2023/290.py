class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        mp2 = {}
        j = 0
        i = 0
        while i < len(pattern) and j < len(s):
            str = ""
            while j < len(s) and s[j] != ' ':
                str += s[j]
                j += 1
            j += 1
            if pattern[i] in mp:
                if mp[pattern[i]] != str:
                    return False
            if str in mp2:
                if mp2[str] != pattern[i]:
                    return False
            mp[pattern[i]] = str
            mp2[str] = pattern[i]
            i += 1
        if j < len(s):
            return False
        if i < len(pattern):
            return False
        return True
        