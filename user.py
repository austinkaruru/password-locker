class User:
    """
    Class that generates new instances of contacts

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

    def __init__(self, application, email, password):

        self.application = application
        self.email = email
        self.password = password
