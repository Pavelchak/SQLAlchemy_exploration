import unittest
import view


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(view.smile(), ":)")


if __name__ == '__main__':
    unittest.main()