# Conan HTPASSWD Authorization Manager

This is a simple htpasswd authorization manager for conan > 0.21

#Deployment

Copy the authenticator to `[path to conan_server]/plugins/authenticator` and add `htpasswd_authenticator` to the server config by adding 
`custom_authenticator: htpasswd_authenticator` in the `[server]` section

To customize the htpasswd file location, add the key
`htpasswd_file: {location}` to the `[server]` section



