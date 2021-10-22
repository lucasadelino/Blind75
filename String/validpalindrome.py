import re
regex = re.compile(r'[A-Za-z0-9]+')

class Solution:
    def isPalindrome(self, s: str) -> bool:
        matches = regex.findall(s)
        no_space = ''.join(matches).lower()
        j = len(no_space) - 1
        if j <= 0:
            return True
        until = int(j/2)
        i = 0
        while i <= until:
            if no_space[i] != no_space[j]:
                return False
            else:
                i +=1
                j -=1
        return True