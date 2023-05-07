from collections import deque


class Numbers:

    def __init__(self):
        self.numbers = deque([])

    def add_number(self, val):
        # Insert method to add element
        if val not in self.numbers:
            self.numbers.insert(0, val)
            return True
        return False

    def size(self):
        return len(self.numbers)

    def remove_last(self):
        self.numbers.popleft()

    def remove_first(self):
        self.numbers.pop()

    def printContent(self):
        print(self.numbers)


numbers = Numbers()

for i in range(20):
    numbers.add_number(i+1)

numbers.printContent()

numbers.remove_first()
numbers.remove_first()
numbers.remove_last()

numbers.printContent()
