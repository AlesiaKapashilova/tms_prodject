import configparser

config = configparser.ConfigParser()
config.read('/home/alesya/les/my_work/tms_prodject/configs/data_base_configs.ini')

# database_connection
user = config.get("database_connection", "user")
password = config.get("database_connection", "password")
host = config.get("database_connection", "host")
database = config.get("database_connection", "database")

# queries
create_group = config.get("queries", "create_group")
user_checked = config.get("queries", "user_checked")
checked_group = config.get("queries", "checked_group")
checked_user_in_group = config.get("queries", "checked_user_in_group")
delete_user_from_group = config.get("queries", "delete_user_from_group")
delete_user = config.get("queries", "delete_user")

# created_group
group_name = config.get("created_group", "group_name")

# created user
user_in_group = config.get("created_user", "user_in_group")
