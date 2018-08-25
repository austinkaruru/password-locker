import unittest
from cred import Cred


class TestCred(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Cred(
            "lulu@lu.com", "123")  # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_cred.email, "lulu@lu.com")
        self.assertEqual(self.new_cred.password, "123")


if __name__ == '__main__':
    unittest.main()
