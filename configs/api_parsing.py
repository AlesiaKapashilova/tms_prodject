import configparser

config = configparser.ConfigParser()
config.read('configs/api_config.ini')

# user_requests
create_user = config.get("user_requests", "create")
login_user = config.get("user_requests", "login")
get_info_user = config.get("user_requests", "get_info")
logout_user = config.get("user_requests", "logout")
delete_user = config.get("user_requests", "delete")

# user
user_info = config.get("user", "info")

# pet_requests
create_pets = config.get("pet_requests", "create")
find_pets = config.get("pet_requests", "find")
update_pets = config.get("pet_requests", "create")

# pet
pet_info = config.get("pet", "info")
new_pet_name = config.get("pet", "new_name")
