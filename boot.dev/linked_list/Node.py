class Node:
    val: any

    def __init__(self, val: any) -> None:
        self.val = val
        self.node = None

    def set_next(self, node: "None") -> None:
        self.next = node

    def __repr__(self):
        return self.val


a = Node("Apple")
b = Node("Banana")
c = Node("Cherry")

print(a, b, c)

a.set_next(b)
b.set_next(c)

print("val:", a.val, "next:", a.next)

print(a.next is b)  # True
print(a.next == "Banana")  # False
