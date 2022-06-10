import requests
from configs.api_parsing import *
from helpers.api_logic import *


class UserAPIPage:

    def __init__(self):
        self.user = None

    def create_user(self):
        self.user = requests.post(create_user, json=user_creation())
        return self.user.status_code

    def login(self):
        self.user = requests.get(login_user)
        return self.user.status_code

    def get_user_info(self):
        self.user = requests.get(get_info_user).json()
        username = self.user["username"]
        first_name = self.user["firstName"]
        last_name = self.user["lastName"]
        email = self.user["email"]
        password = self.user["password"]
        phone = self.user["phone"]
        info = f'{username}, {first_name}, {last_name}, ' \
               f'{email}, {password}, {phone}'
        return info

    def logout(self):
        self.user = requests.get(logout_user)
        return self.user.status_code

    def delete_user(self):
        self.user = requests.delete(delete_user)
        return self.user.status_code


class PetAPIPage:

    def __init__(self):
        self.pet = None

    def create_pet(self):
        self.pet = requests.post(create_pets, json=pet_creation())
        return self.pet.status_code

    def pet_info(self):
        self.pet = requests.get(find_pets).json()
        return self.pet

    def photo_urls(self):
        ph_urls = self.pet_info()["photoUrls"]
        for element in ph_urls:
            return element

    def tags_id(self):
        tags = self.pet_info()["tags"]
        for element in tags:
            return element["id"]

    def tags_name(self):
        tags = self.pet_info()["tags"]
        for element in tags:
            return element["name"]

    def check_pet_info(self):
        creation = self.pet_info()
        urls = self.photo_urls()
        tag_id = self.tags_id()
        tag_name = self.tags_name()
        pet_id = creation["id"]
        category_id = creation["category"]["id"]
        category_name = creation["category"]["name"]
        name = creation["name"]
        status = creation["status"]
        info = f'{pet_id}, {category_id}, {category_name}, {name}, {urls}, ' \
               f'{tag_id}, {tag_name}, {status}'
        return info

    def update_pet_name(self):
        self.pet = requests.put(update_pets, json=update_pet_name())
        find = requests.get(find_pets).json()
        return find["category"]["name"]