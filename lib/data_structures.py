spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: {"🌶" * food.get("heat_level")}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    
def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_food)

def get_average_heat_level(spicy_foods):
    heat_level = [food.get("heat_level") for food in spicy_foods]
    return sum(heat_level) / len(heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
