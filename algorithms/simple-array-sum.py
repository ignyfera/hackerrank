r"""
    Hackerrank > Algorithms > Warmup > Simple Array Sum

    Given an array of N integers, sum its elements.

    Input Format
    - The first line contains an integer, N, denoting the size of the array.
    - The second line contains N space-separated integers representing the
      array's elements.

    Output Format
    Print the sum of the array's elements as a single integer.
"""


__author__ = 'ignyfera'


class Solution(object):
    def __init__(self, arr):
        self.array = arr

    def solve(self):
        return sum(self.array)


# read input and write output
_ = raw_input().strip()
print Solution(map(int,raw_input().strip().split())).solve()
