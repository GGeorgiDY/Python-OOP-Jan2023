class reverse_iter:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.my_list[self.index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
