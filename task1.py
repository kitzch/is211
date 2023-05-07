from collections import deque


class Numbers:

    def __init__(self):
        self.numbers = deque([])

    def add_first(self, val):
        self.numbers.appendleft(val)

    def add_last(self, val):
        self.numbers.append(val)

    def remove_first(self):
        self.numbers.popleft()

    def remove_last(self):
        self.numbers.pop()

    def print_content(self):
        print(self.numbers)


numbers = Numbers()

numbers.add_last(1)
numbers.add_last(2)
numbers.add_last(3)
numbers.add_last(4)
numbers.add_first(69)

numbers.print_content()

numbers.remove_first()
numbers.remove_last()

numbers.print_content()