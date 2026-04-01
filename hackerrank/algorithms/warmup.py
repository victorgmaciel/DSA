


from typing import Tuple, List


def compare_triplets(int_a: List[int], int_b: List[int]) -> List[int]:

    final_score_list = []
    final_a_score = 0
    final_b_score = 0

    for index, (a, b) in enumerate(zip(int_a, int_b)):
        print(int_a[index])





margs_scores = [5,6,7]
dannys_scores = [3,6,10]

print(compare_triplets(margs_scores, dannys_scores))