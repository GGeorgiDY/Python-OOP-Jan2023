import unittest
from project_testing.my_class import MyClass


class TestMyClass(unittest.TestCase):
    # чрез долните 2 реда, си сетваме това което ще тестваме
    def setUp(self) -> None:
        self.my_obj = MyClass()

    def test_method1(self):
        result = self.my_obj.method1()
        self.assertEqual(result, 'Hello SoftUni')

    def test_method2(self):
        result = self.my_obj.method2()
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()