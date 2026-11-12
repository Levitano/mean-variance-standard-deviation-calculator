import unittest

from mean_var_std import calculate


class TestCalculate(unittest.TestCase):
    def test_example(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(result["mean"][0], [3.0, 4.0, 5.0])
        self.assertEqual(result["mean"][1], [1.0, 4.0, 7.0])
        self.assertEqual(result["mean"][2], 4.0)
        self.assertEqual(result["sum"], [[9, 12, 15], [3, 12, 21], 36])
        self.assertEqual(result["max"], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(result["min"], [[0, 1, 2], [0, 3, 6], 0])

    def test_too_few_numbers(self):
        with self.assertRaisesRegex(
            ValueError, "A lista deve conter nove números"
        ):
            calculate([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
