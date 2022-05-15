import json # to deal with json files
from tabulate import tabulate # to make table

# open json files
users_file = open('users.json')
restaurant_file = open('restaurant.json')

users_data = json.load(users_file) # load users data
restaurant_data = json.load(restaurant_file) # load restaurant data


# extracting restraunt data and dishs from restaurant.json file

def load_restaurant_data(restaurant_data):
    restaurant_name = restaurant_data["name"]
    restaurant_type = restaurant_data["type"]
    restaurant_location = ''.join(str(restaurant_data["location"]))
    restaurant_offers =  restaurant_data["offers"]
    restaurant_dishs = restaurant_data["dishes"]

    list_of_dishs = []
    
    for dish in restaurant_dishs:
        dish_name = restaurant_dishs[dish]["name"]
        dish_components = restaurant_dishs[dish]["components"]
        dish_tags = restaurant_dishs[dish]["tags"]
        dish_price = restaurant_dishs[dish]["Price"]
        list_of_dishs.append([dish_name, dish_components, dish_tags, dish_price])

    return list_of_dishs   



# extracting users data from uers.json file

def load_users_data(users_data):
    list_of_users = []

    for users in users_data:
        name = users_data[users]['name']
        email = users_data[users]['email']
        gender = users_data[users]['gender']
        age = users_data[users]['userInfo']['age']
        phoneNumber = users_data[users]['phoneNumber']
        height = users_data[users]['userInfo']['height']
        weight = users_data[users]['userInfo']['weight']
        typesPrefered = users_data[users]['userInfo']['typesPrefered']
        choronicConditions = users_data[users]['medicalHistory']['choronicConditions']
        alergics = users_data[users]['medicalHistory']['alergics']
        all_info = [
            name,
            email,
            gender,
            age,
            phoneNumber,
            height,
            weight,
            typesPrefered,
            choronicConditions,
            alergics
        ]
        list_of_users.append(all_info)
    return list_of_users


# filtering dishs that user can eat

def eating_filter(list_of_users, list_of_dishs):
    dishs_allowed = []
    dishs_denied = []
    for user in list_of_users:
        name = user[0]
        user_alergics = user[9]
        for dish in list_of_dishs:
            dish_name = dish[0]
            dish_components = dish[1]
            if set(user_alergics).intersection(set(dish_components)):
                dishs_denied.append(dish_name)
            else:
                dishs_allowed.append(dish_name)
        final_result = [name, dishs_allowed, dishs_denied]
        print(tabulate([final_result], headers=["name", "dish_allowed", "dishs_denied"], tablefmt='grid'), "\n\n")
        final_result = []
        dishs_allowed = []
        dishs_denied = []


eating_filter(load_users_data(users_data), load_restaurant_data(restaurant_data))
