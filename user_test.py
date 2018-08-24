import unittest  # Importing unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        self.assertEqual(self.new_user.application, "Twitter")
        self.assertEqual(self.new_user.email, "kalulu@ms.com")
        self.assertEqual(self.new_user.password, "wololo")


if __name__ == '__main__':
    unittest.main()
