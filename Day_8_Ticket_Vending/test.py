import unittest
import change_text

class TestChangeText(unittest.TestCase):
    def test_capitals(self):
        text = 'hello'
        result = change_text.capitals(text)
        self.assertEqual('HELLO', result)

if __name__ == '__main__':
    unittest.main()