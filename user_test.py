import unittest  # Importing unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("Twitter", "kalulu@ms.com", "wololo")

    def tearDown(self):
        '''
        does clean up after each test
        '''
        User.users = []

    def test_save_user(self):
        '''
        to test the test case to test if user object is saved into users list
        '''

        self.new_user.save_user()  # save new user
        self.assertEqual(len(User.users), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to see if we can save multiple users object to User(list)
        '''
        self.new_user.save_user()
        test_user = User("Testapp", "user@us.com", "123")  # new user
        test_user.save_user()
        self.assertEqual(len(User.users), 2)

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.application, "Twitter")
        self.assertEqual(self.new_user.email, "kalulu@ms.com")
        self.assertEqual(self.new_user.password, "wololo")

    def test_delete_user(self):
        '''
        tests if we can delete a user account
        '''
        self.new_user.save_user()
        test_user = User("Testapp", "user@us.com", "123")
        test_user.save_user()

        self.new_user.delete_user()  # Delete a user object
        self.assertEqual(len(User.users), 1)

    def test_find_user_by_application(self):
        ''' 
        test if we can find user account by searching using the application registered
        '''

        self.new_user.save_user()
        test_user = User("Testapp", "user@us.com", "123")  # new user
        test_user.save_user()

        found_user = User.find_by_application("Testapp")

        self.assertEqual(found_user.email, test_user.email)


if __name__ == '__main__':
    unittest.main()
