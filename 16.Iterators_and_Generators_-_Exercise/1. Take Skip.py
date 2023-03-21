class take_skip:
    def __init__(self, step:int, count:int):
        self.step = step
        self.count = count
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.counter + 1:
            raise StopIteration
        self.counter += 1
        return self.step * self.counter


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
