import unittest

from calculator import calculate


class TestCalculate(unittest.TestCase):
	
	def test_whole_numbers(self):
		self.assertEqual(calculate('2-2'),'0', "Should be 0")
		self.assertEqual(calculate('1-2'), '-1', "Should be -1")
		self.assertEqual(calculate('10*2'), '20', "Should be 20")
		self.assertEqual(calculate('10/2'), '5', "Should be 5")
		self.assertEqual(calculate('1/2'), '1/2', "Should be 1/2")

	def test_fraction_math(self):
		self.assertEqual(calculate('1/2 + 1/4'), '3/4', "Should be 3/4")
		self.assertEqual(calculate('1/2 - 1/4'), '1/4', "Should be 1/4")
		self.assertEqual(calculate('1/2 * 1/4'), '1/8', "Should be 1/8")
		self.assertEqual(calculate('1/2 * 2/1'), '1', "Should be 1")
		self.assertEqual(calculate('1/2 / 1/4'), '2', "Should be 2")
	
	def test_mixed_fractions(self):
		self.assertEqual(calculate('1/2 * 3_3/4'), '1_7/8', "Should be 1_7/8")
		self.assertEqual(calculate('2_3/8 + 9/8'), '3_1/2', "Should be 3_1/2")

	def test_many_fractions_math(self):
		self.assertEqual(calculate('1/2 + 1/4 + 3/4'), '1_1/2', "Should be 1_1/2")
		self.assertEqual(calculate('1/2 * 1/4 - 3/4'), '-5/8', "Should be -5/8")

	def test_whitespace(self):
		self.assertEqual(calculate('?1 + 2'), '3', "Should be 3")
		self.assertEqual(calculate('1 + 2'), '3', "Should be 3")
		self.assertEqual(calculate('1+  2'), '3', "Should be 3")
		self.assertEqual(calculate('1+    2   - 2'), '1', "Should be 1")

if __name__ == '__main__':
    unittest.main()
