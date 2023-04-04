from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):

    def setUp(self):
        self.plantation1 = Plantation(100)

    def test_initialization(self):
        self.assertEqual(100, self.plantation1.size)
        self.assertEqual({}, self.plantation1.plants)
        self.assertEqual([], self.plantation1.workers)

    def test_size_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation1 = Plantation(-1)
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_ve(self):
        self.plantation1.workers = ['ivan']
        with self.assertRaises(ValueError) as ve:
            result = self.plantation1.hire_worker('ivan')
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker_result_and_return(self):
        self.plantation1.workers = ['ivan']
        result = self.plantation1.hire_worker('georgi')
        self.assertEqual(['ivan', 'georgi'], self.plantation1.workers)
        self.assertEqual("georgi successfully hired.", result)

    def test_len(self):
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}
        result = self.plantation1.__len__()
        self.assertEqual(4, result)

    def test_planting_worker_not_hired_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation1.planting('kiro', "flower1")
        self.assertEqual(str(ve.exception), "Worker with name kiro is not hired!")

    def test_planting_plantation_is_full_ve(self):
        self.plantation1.size = 4
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}
        self.plantation1.workers = ['ivan', 'georgi']
        with self.assertRaises(ValueError) as ve:
            self.plantation1.planting('ivan', "flower4")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_result_and_return(self):
        self.plantation1.size = 10
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}
        self.plantation1.workers = ['ivan', 'georgi']
        result = self.plantation1.planting('ivan', "flower4")
        self.assertEqual({'ivan': ['flower1', 'flower2', 'flower3', 'flower4'], 'georgi': ['flower4']}, self.plantation1.plants)
        self.assertEqual("ivan planted flower4.", result)

    def test_planting_second_result_and_return_2(self):
        self.plantation1.size = 10
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3']}
        self.plantation1.workers = ['ivan', 'georgi']
        result = self.plantation1.planting('georgi', "flower4")
        self.assertEqual({'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}, self.plantation1.plants)
        self.assertEqual("georgi planted it's first flower4.", result)

    def test_str(self):
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}
        self.plantation1.workers = ['ivan', 'georgi']
        result = self.plantation1.__str__()
        result2 = "Plantation size: 100" + "\n"
        result2 += "ivan, georgi" + "\n"
        result2 += "ivan planted: flower1, flower2, flower3" + "\n"
        result2 += "georgi planted: flower4"
        self.assertEqual(result, result2)

    def test_repr(self):
        self.plantation1.plants = {'ivan': ['flower1', 'flower2', 'flower3'], 'georgi': ['flower4']}
        self.plantation1.workers = ['ivan', 'georgi']
        result = self.plantation1.__repr__()
        result2 = 'Size: 100' + "\n"
        result2 += 'Workers: ivan, georgi'
        self.assertEqual(result, result2)


if __name__ == "__main__":
    main()