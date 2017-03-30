"""
A plugin for conan htpasswd authentication

TODO:
Make location of htpasswd file configurable
"""
from passlib.apache import HtpasswdFile

def get_class():
    """ plugin entry point """
    return HtpasswdAuthenticator()


class HtpasswdAuthenticator(object):
    """
    Handles the user authentication for htpasswd files
    htpasswd is the location of the htpasswd to use
    """
    def __init__(self):
        self.htpasswd = HtpasswdFile(".htpasswd")

    def valid_user(self, username, plain_password):
        """
        username: Username to be authenticated
        plain_password: The password to authenticate with
        return: True if match False if don't
        """
        # Update
        self.htpasswd.load_if_changed()
        # Verify
        return username in self.htpasswd.users() and \
               self.htpasswd.check_password(username, plain_password)
