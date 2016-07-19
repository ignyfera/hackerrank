r"""
    Hackerrank > Algorithms > Strings > Pangrams
"""

class Solution(object):
    def __init__(self, string):
        self.string = string
        
    def isPangram(self):
        s = [ ch.lower() for ch in self.string if ch.isalpha() ]
        if len(set(s)) == 26:
            return True
        else:
            return False
        
    def solve(self):
        if self.isPangram():
            return 'pangram'
        else:
            return 'not pangram'


# read input and write output        
print Solution(raw_input().strip()).solve()
