r"""
    Hackerrank > Algorithms > Dynamic Programming > Maximum Subarray

    Given an array A = {a_1, ... , a_N } of N elements, find the maximum
    possible sum of a
        (1.)  contiguous subarray;
        (2.)  non-contiguous (not necessarily continguous) subarray.

    Input Format:
    First line of the input has an integer T.
    T test cases follow. Each test case begins with an integer N.
    In the next line, N integers follow representing the elements of array A.

    Constraints:
    1 <= T <= 10
    1 <= N <= 10**5
    -10**4 <= a_i <= 10**4

    The subarray and subsequences you consider should have at least one element.

    Output Format:
    Two space-separated integers denoting the sum of the maximum contiguous and
    non-contiguous subarray. At least one integer should be selected and put
    into the subarrays (this may be required in cases where all elements are
    negative).
"""


__author__ = 'ignyfera'

class Solution(object):
    def __init__(self, arr):
        self.arr = arr

    def maxSumContig(self):
        max_to_here = self.arr[0]
        max_overall = self.arr[0]
        for x in self.arr[1:]:
            max_to_here = max(x, max_to_here + x)
            max_overall = max(max_overall, max_to_here)
        return max_overall

    def maxSumSet(self):
        if all(x <= 0 for x in self.arr):
            return max(self.arr)
        else:
            return sum([ x for x in self.arr if x > 0 ])

    def solve(self):
        return ' '.join(map(str, [self.maxSumContig(), self.maxSumSet()]))


# read input and write output
t = int(raw_input().strip())
for _ in range(t):
    n   = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    print Solution(arr).solve()
