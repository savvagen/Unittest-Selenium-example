import unittest


class ExampleTests1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_1_passing(self):
        self.assertGreater(2, 1)
        self.assertEqual(1, 1)

    def test_2_failed(self):
        self.assertEqual(1, 2)

    @unittest.skip
    def test_3_skipped(self):
        self.assertEqual(2, 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)
