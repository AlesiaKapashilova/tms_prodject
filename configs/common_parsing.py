import configparser

config = configparser.ConfigParser()
config.read('/home/alesya/les/my_work/tms_prodject/configs/сommon_configs.ini')

# admin login data
username = config.get("login_info", "username")
password = config.get("login_info", "password")

# new user login data
new_username = config.get("new_user_info", "username")
new_password = config.get("new_user_info", "password")

# new date and time for image
data = config.get("picture_info", "data")
time = config.get("picture_info", "time")
new_date = config.get("picture_info", "new_date")

# greeting a new user by his name
welcome_name = config.get("welcome", "welcome_name")
