import configparser

config = configparser.ConfigParser()
config.read('configs/common_configs.ini')

# admin login data
username = config.get("authorization data", "Admin")
password = config.get("authorization data", "Admin_password")

# new user login data
new_username = config.get("user_data", "Username")
new_password = config.get("user_data", "Password")

# new date and time for image
data = config.get("image_data", "data")
time = config.get("image_data", "time")
new_date = config.get("image_data", "new_date")

# greeting a new user by his name
welcome_name = config.get("welcome", "welcome_name")

# group for users
group_name = config.get("group_for_user", "group")