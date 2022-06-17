import configparser

config = configparser.ConfigParser()
config.read('configs/database_configs.ini')

# database_connection
user = config.get("database_connection", "user")
password = config.get("database_connection", "password")
host = config.get("database_connection", "host")
database = config.get("database_connection", "database")

# database_data
user_name = config.get("database_data", "user_name")
group_name = config.get("database_data", "group_name")

