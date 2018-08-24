import pyperclip


class User:
    """
    Class that generates new instances of user

    """

    def delete_user(self):
        '''
        deletes a saved user from users(list)
        '''

        User.users.remove(self)

    users = []  # Empty users list

    def save_user(self):
        '''
        save_user method saves user objects to users(list)
        '''
        User.users.append(self)

    @classmethod
    def find_by_application(cls, application):
        '''
        method that takes in an application and returns a user that matches the application

        Args:
            application: App to search for
        Returns :
            User of person that matches the app.


        '''
        for user in cls.users:
            if user.application == application:
                return user

    @classmethod
    def user_exist(cls, application):

        for user in cls.users:
            if user.application == application:
                return True
        return False

    @classmethod
    def copy_email(cls, application):
        user_found = User.find_by_application(application)
        pyperclip.copy(user_found.email)

    @classmethod
    def display_users(cls):

        return cls.users

    def __init__(self, application, email, password):

        self.application = application
        self.email = email
        self.password = password


def create_user(application, email, password):
    '''
    function to create new user account
    '''
    new_user = User(application, email, password)
    return new_user


def save_users(user):
    '''
    function to save user account
    '''
    user.save_user()


def del_user(user):
    '''
    function to delete user account
    '''
    user.delete_user()
