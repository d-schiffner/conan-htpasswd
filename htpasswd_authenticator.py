"""
A plugin for conan htpasswd authentication
"""

import os
from ConfigParser import ConfigParser
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
        #try to locate the server config and load it
        server_folder = os.path.join(os.path.expanduser("~"), '.conan_server')
        server_conf = os.path.join(server_folder, "server.conf")
        htpasswd_location = os.path.join(server_folder, "plugins", "authentication", ".htpasswd")
        if os.path.exists(server_conf):
            conf = ConfigParser()
            conf.read(server_conf)
            new_loc = conf.get("server", "htpasswd_file")
            if os.path.exists(new_loc):
                htpasswd_location = new_loc

        self.htpasswd = HtpasswdFile(htpasswd_location)

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
