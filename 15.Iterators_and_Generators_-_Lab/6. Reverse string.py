def reverse_text(my_string):
    for i in range(len(my_string) -1, -1, -1):
        yield my_string[i]


for char in reverse_text("step"):
    print(char, end='')
