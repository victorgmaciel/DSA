from typing import List

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    biggest = 0

    for num in nums:
        if num == 1:
            count +=1
        else:
            biggest = max(biggest,count)
            if biggest > 0:
                count = 0
    return max(biggest, count)
                    



# print(findMaxConsecutiveOnes([0,0,1,1,1,1,0,0]))
print(findMaxConsecutiveOnes([1,1,0,1,1,1])) # SHOULD return 3