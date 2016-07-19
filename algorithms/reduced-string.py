r"""
    Hackerrank > Algorithms > Strings > Super Reduced String
"""

class Solution(object):
    def __init__(self, string):
        self.string   = string
        
    def removePairs(self, string):
        for i in xrange(len(string)-1):
            if string[i] == string[i+1]:
                return self.removePairs(string[:i] + string[i+2:])
        return string
    
    def solve(self):
        pairfree = self.removePairs(self.string)
        if len(pairfree) > 0:
            return pairfree
        else:
            return 'Empty String'


# read input and write output
print Solution(raw_input().strip()).solve()
