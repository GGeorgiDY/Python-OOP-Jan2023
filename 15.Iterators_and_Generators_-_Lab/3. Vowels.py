class vowels:

    def __init__(self, some_string):
        self.string = some_string
        self.index = 0

    @property
    def vowels(self):
        return 'aeiyou'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration

        letter = self.string[self.index]
        self.index += 1

        if letter.lower() in self.vowels:
            return letter

        return self.__next__()


# Part below is part from automatic judge system from SoftUni
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


