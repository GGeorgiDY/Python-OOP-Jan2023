# import unittest
# from exercise_my_math import add, subtract, multiply, divide
#
#
# class TestMyMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(5, 6), 11)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(2, 3), -1)
#
#     def test_multiply(self):
#         self.assertEqual(multiply(2, 3), 6)
#
#     def test_divide(self):
#         self.assertEqual(divide(10, 5), 2)
#
#
# if __name__ == "__main__":
#     unittest.main()

#/////////////////////////////////////////////////////////////////////////////////////

# import unittest
#
#
# class MyTests(unittest.TestCase):
#
#     # много е важно тестовете да започват с test_, защото unittest търси тестове само започващи с test_
#     def test_addition(self):
#         result = 2 + 2
#         self.assertEqual(result, 4)
#
#     def test_subtraction(self):
#         result = 5 - 3
#         self.assertEqual(result, 2)
#
#     def test_multiplication(self):
#         result = 5 * 3
#         self.assertEqual(result, 15)
#
#     def test_division(self):
#         result = 8 / 4
#         self.assertEqual(result, 2)
#
#
# # долното се извиква за да изпълни всички тестове в конкретния клас
# if __name__ == "__main__":
#     unittest.main()


#/////////////////////////////////////////////////////////////////////////////////////




#/////////////////////////////////////////////////////////////////////////////////////

# import unittest
# import time
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         start_time = time.time()
#         time.sleep(2)
#         end_time = time.time()
#         diff = start_time - end_time
#         print(f'Test too {diff} seconds to complete')
#         self.assertTrue(True)
#
#
# if __name__ == '__main__':
#     unittest.main()

#/////////////////////////////////////////////////////////////////////////////////////

# import unittest
#
#
# def divide_number(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Cannot divide by zero')
#     return x / y
#
#
# class TestDivisionNumbers(unittest.TestCase):
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide_number(5, 0)
#
#
# if __name__ == '__main__':
#     unittest.main()

#/////////////////////////////////////////////////////////////////////////////////////

# import unittest
#
#
# class MyClass:
#     def method1(self):
#         return 'Hello SoftUni'
#
#     def method2(self):
#         return 42
#
#
# class TestMyClass(unittest.TestCase):
#     # чрез долните 2 реда, си сетваме това което ще тестваме
#     def setUp(self) -> None:
#         self.my_obj = MyClass()
#
#     def test_method1(self):
#         result = self.my_obj.method1()
#         self.assertEqual(result, 'Hello SoftUni')
#
#     def test_method2(self):
#         result = self.my_obj.method2()
#         self.assertEqual(result, 42)
#
#
# if __name__ == '__main__':
#     unittest.main()

#/////////////////////////////////////////////////////////////////////////////////////





#/////////////////////////////////////////////////////////////////////////////////////