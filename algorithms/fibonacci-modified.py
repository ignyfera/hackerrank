r"""
    Hackerrank > Algorithms > Dynamic Programming > Fibonacci Modified

    Given the nth and (n+1)st terms, the (n+2)nd can be computed by the
    following relation:
        T_{n+2} = T_{n+1}^2 + T_n

    Input Format:
    Three space-separated integers A, B, N.

    Constraints:
    0 <= A, B <= 2
    3 <= N <= 20

    Output Format:
    The Nth term of the series, given that the first two terms are A and B,
    respectively. (T_1 = A, T_2 = B)

    Example:
        Sample Input:
        0 1 5

        Sample Output:
        5
        (The fifth element of the sequence 0, 1, 1, 2, 5, 27, ...)
"""


__author__  = 'ignyfera'

class Solution(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fib(self, n):
        F = [self.a, self.b]
        for i in xrange(2, n+1):
            F.append(F[i-1]**2 + F[i-2])
        return F[n]

    def solve(self, n):
        return self.fib(n-1)


# read input and write output
A, B, N = map(int, raw_input().strip().split())
print Solution(A, B).solve(N)
