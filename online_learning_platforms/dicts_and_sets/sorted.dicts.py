from sortedcontainers import SortedDict


def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    list_of_values = []

    for key, value in sorted_dict.items():
        if key != target:
            list_of_values.append(value)
        else:
            break
    return list_of_values



# expected [25, 35]

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))