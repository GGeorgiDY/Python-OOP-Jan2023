# class countdown_iterator:
#     def __init__(self, number: int):
#         self.number = number
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == self.number:
#             raise StopIteration
#         self.index += 1
#         return self.number - self.index

class countdown_iterator:
    def __init__(self, number: int):
        self.number = number + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        self.number -= 1
        return self.number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
