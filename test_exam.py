import exam
import unittest

class TestArProgSum(unittest.TestCase):
    def test_positive_case(self):
        self.assertEqual(exam.ar_prog_sum(2, 3, 4), 26)
        self.assertEqual(exam.ar_prog_sum(0, 1, 10), 45)


    def test_invalid_n(self):
        self.assertRaises(ValueError, exam.ar_prog_sum, 1, 3, 0)

if __name__ == "__main__":
    unittest.main()