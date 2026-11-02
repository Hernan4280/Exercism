"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    #Add items to shopping cart.

    updated_cart = dict(current_cart)
    for item in items_to_add:
        if item in updated_cart:
            updated_cart[item] += 1
        else:
            updated_cart[item] = 1
    return updated_cart


def read_notes(notes):
    #Create user cart from an iterable notes entry.

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    #Update the recipe ideas dictionary.

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    #Sort a user's shopping cart in alphabetical order.

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    #Combine user's order to aisle and refrigeration information.

    new_cart = dict()
    for key, value in aisle_mapping.items():
        if key in cart and isinstance(value[0], int):
            new_cart[key] = value
        elif key in cart and isinstance(value[0], str):
            new_cart[key] = [cart[key]] + value
            
    return dict(sorted(new_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    #Update store inventory levels with user order.

    for key, value in fulfillment_cart.items():
        store_inventory[key][0] -= value[0]
        if store_inventory[key][0] == 0:
            store_inventory[key][0] = 'Out of Stock'
        
    return store_inventory
