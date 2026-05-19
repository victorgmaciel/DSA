
def first_non_repeating_character(word: str) -> str:
    print(word)

    # account for no word at all
    if word == "":
        return ""
    # account for caps and remove space
    word = word.lower().replace(" ", "")
    #chance of spaces in string
    non_repeating_character_list = []

    for letters in word:
        if letters not in non_repeating_character_list:
            non_repeating_character_list.append(letters)
    return non_repeating_character_list




test_case_one = "a Ab b c" # should return c
test_case_two = "a" # should return none 
test_case_three = "tvgatvggls" # should return v
test_case_four = "aabbc c" # should return c

print(first_non_repeating_character(test_case_one))
# print(first_non_repeating_character(test_case_three))

