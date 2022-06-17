import configparser

config = configparser.ConfigParser()
config.read('configs/common_configs.ini')

# admin login data
username = config.get("authorization data", "Admin")
password = config.get("authorization data", "Admin_password")

# new user login data
new_username = config.get("user_data", "Username")
new_password = config.get("user_data", "Password")

# group for users
group_name = config.get("group_for_user", "group")

# links

admin_link = config.get("links","admin_link")
logout_link = config.get("links","logout_link")
