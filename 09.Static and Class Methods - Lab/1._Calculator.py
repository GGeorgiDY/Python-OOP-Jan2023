from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    # @staticmethod
    # def multiply(*args):
    #     result = 1
    #     for i in args:
    #         result *= i
    #     return result
    # може и горното, може и долното

    @staticmethod
    def multiply(*args):
        return reduce(lambda a, b: a * b, args)
    # reduce получава параметъра.
    # 1ви е някакв функция "lambda a, b: a * b"
    # 2рия е колекция през която итерира "args"
    # 1вия получва 2 параметъра или иначе казвано reduce ще извади първите две неща от args. В случая това са 1 и 2. Това
    # което ще направи функцията е да умножи двете числа. След това този резултат ще се върне обратно в args на индекс 0.

    @staticmethod
    def divide(*args):
        result = args[0] / args[1]
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for i in args[1:]:
            result -= i
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
