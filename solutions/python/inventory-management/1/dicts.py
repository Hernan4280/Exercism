"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""

    counting_dict = {}
    for item in items:
        counting_dict[item] = counting_dict.get(item, 0) + 1
    return counting_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""

    new_inventory = create_inventory(items)
    for k, v in new_inventory.items():
        if k in inventory:
            inventory[k] += v
        else:
            inventory[k] = v
    return inventory


def decrement_items(inventory, items):
    "Decrement items in inventory using elements from the `items` list."

    for i in items:
        if i in inventory and inventory[i] > 0:
            inventory[i] -= 1
    return inventory


def remove_item(inventory, item):
    "Remove item from inventory if it matches `item` string."

    inventory.pop(item, inventory)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory."""

    return [(k, v) for k, v in inventory.items() if v > 0]
