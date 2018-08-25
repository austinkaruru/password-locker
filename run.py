#!/usr/bin/env python3.6
from user import User
import random


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


def find_user(application):
    '''
    function to find user account using the application
    '''
    return User.find_by_application(application)


def check_existing_users(application):
    return User.user_exist(application)


def display_users():
    '''
    function that returns all saved users
    '''
    return User.display_users()


def main():
    print("Hello There, Welcome to password-locker.Please login to continue.")
    user_email = input()
    random_number = random.randint(99999, 999999)

    print(f"Hello @{user_email}, your new password is {random_number}")

    print('\n')

    while True:
        # if user_email == email
        #    user_password == password

        print(
            "What do you want to do : sc - save new account with credentials, da - Display accounts, fa - find account, ex - exit the app")

        short_code = input().lower()

        if short_code == 'sc':
            print("New account")
            print("-"*10)

            print("App")
            application = input()

            print("Email")
            email = input()

            random_number = random.randint(99999, 999999)
            print("random_number")
            # password = input()

            save_users(create_user(
                application, email, random_number))

            print('\n')
            print(
                f"New user Application:{application} Email:{email} password:{random_number} created")

            print('\n')

        elif short_code == 'da':

            if display_users():
                print("Here is a list of users")
                print('\n')

                for user in display_users():
                    print(
                        f"{user.application} {user.email} {user.password}")

                print('\n')
            else:
                print('\n')
                print("None currently exist")

                print('\n')
        elif short_code == 'fa':

            print("enter the user you want")

            search_application = input()
            if check_existing_users(search_application):
                search_application = find_user(
                    search_application)
                print(
                    f"{search_application.application} {search_application.email}")
                print('-'*20)

                print(
                    f"Application .... {search_application.application}")
                print(
                    f"Email address ... {search_application.email}")

            else:
                print("Not found")

        elif short_code == "ex":
            print("Bye....")
            break
        else:
            print("Sorry,I didn't get that.Try again")


if __name__ == '__main__':

    main()
