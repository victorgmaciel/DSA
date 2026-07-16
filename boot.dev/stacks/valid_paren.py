class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item


def is_valid_parens(input_str) -> bool:

    # if string matches parens in this dict, then we know we have a match
    parens_dict = {"(": ")"}

    valid_parens_stack = Stack()

    for character in input_str:
        print(character)


print(is_valid_parens("()()"))  # true
# print(is_valid_parens("(()))"))  # false
