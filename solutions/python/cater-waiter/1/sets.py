"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    "Remove duplicates from `dish_ingredients`."

    ingredients_set = set(dish_ingredients)
    return (dish_name, ingredients_set)


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`."""

    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    "Categorize `dish_name` based on `dish_ingredients`."

    if dish_ingredients <= VEGAN:
        return f"{dish_name}: VEGAN"
    if dish_ingredients <= VEGETARIAN:
        return f"{dish_name}: VEGETARIAN"
    if dish_ingredients <= PALEO:
        return f"{dish_name}: PALEO"
    if dish_ingredients <= KETO:
        return f"{dish_name}: KETO"
    if dish_ingredients <= OMNIVORE:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    "Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."

    ingredients = set(dish[1]).intersection(SPECIAL_INGREDIENTS)
    return (dish[0], ingredients) 


def compile_ingredients(dishes):
    "Create a master list of ingredients."

    ingredients_set = set()
    for d in dishes:
        ingredients_set |= d
    return ingredients_set


def separate_appetizers(dishes, appetizers):
    "Determine which `dishes` are designated `appetizers` and remove them."

    return list(set(dishes).difference(set(appetizers)))


def singleton_ingredients(dishes, intersection):
    """Find singleton ingredients within the group of dishes (ingredients that only appear once across dishes)."""

    ingredients = set()
    for dish in dishes:
        ingredients |= dish
    return ingredients - intersection
