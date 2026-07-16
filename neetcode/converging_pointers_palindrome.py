import re

def is_palindrome(word: str) -> bool:
    word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    print(word)
    end =len(word) - 1

    for i in range(len(word)):
        if word[i] == word[end]:
            end -= 1
        else:
            return False
    return True 



word_1 = 'abcdcba' # yes
word_2 = 'beefcakemoney' # no
word_3 = 'racecar' # yes
word_4 = 'blasting' # no

# print(is_palindrome(word_1))
# print(is_palindrome(word_2))
# print(is_palindrome(word_3))
# print(is_palindrome(word_4))
print(is_palindrome("Was it a car or a cat I saw?"))