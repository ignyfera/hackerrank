r"""
    Hackerrank > Algorithms > Dynamic Programming > Nikita and the Game

    Initially, there is an array A containing N integers.

    In each move, Nikita must partition the array into two non-empty parts
    such that the sum of the elements in the left partition is equal to the sum
    of the elements in the right partition.

    If Nikita can make such a move, she gets 1 point; otherwise, the game ends.

    After each successful move, Nikita discards either the left partition or
    the right partition and continues playing by using the remaining partition
    as array A.

    Given A, can you find and print the maximum number of points she can score?

    Input Format:
    The first line contains an integer T, denoting the number of test cases.
    Each test case is described over two lines in the following format:
    - A line containing a single integer N, denoting the size of array A.
    - A line of N space-separated integers describing the elements in array A.

    Constraints:
    1 <= T <= 10
    1 <= N <= 2**14
    0 <= A_i <= 10**9

    Scoring:
    1 <= N <= 2**8  for  30% of the test data
    1 <= N <= 2**11 for  60% of the test data
    1 <= N <= 2**14 for 100% of the test data

    Output Format:
    For each test case, print Nikita's maximum possible score on a new line.
"""
