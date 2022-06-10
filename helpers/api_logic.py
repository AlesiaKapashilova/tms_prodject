import json

with open('/home/alesya/les/my_work/tms_prodject/helpers/api.json',
          'r') as file:
    object = json.load(file)


def user_creation():
    return object[0]


def pet_creation():
    return object[1]


def update_pet_name():
    return object[2]
