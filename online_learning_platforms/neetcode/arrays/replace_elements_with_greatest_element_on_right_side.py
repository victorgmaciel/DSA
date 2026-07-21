"""
You are given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
"""

from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    n = len(arr)
    ans = [0] * n
    rightMax = -1
    for i in range(n - 1, -1, -1):
        ans[i] = rightMax
        rightMax = max(rightMax, arr[i])
    return ans


# ---

test_one_arr = [2, 4, 5, 3, 1, 2]  # output should be [5,5,3,2,2,-1]


print(replace_elements(test_one_arr))
