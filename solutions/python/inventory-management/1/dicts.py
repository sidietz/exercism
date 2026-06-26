"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    inventory = {}

    for element in items:
        if element in inventory.keys():
            tmp = inventory[element]
            inventory[element] = tmp + 1
        else:
            inventory[element] = 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    new_inventory = inventory

    for element in items:
        if element in inventory.keys():
            tmp = inventory[element]
            new_inventory[element] = tmp + 1
        else:
            new_inventory[element] = 1
    return new_inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    new_inventory = inventory

    for element in items:
        if element in inventory.keys():
            tmp = inventory[element] - 1
            if tmp <= 0:
                new_inventory[element] = 0
            else:    
                new_inventory[element] = tmp
        else:
            pass
    return new_inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    new_inventory = inventory

    if item in inventory.keys():
        del(new_inventory[item])
    return new_inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    result = []

    for key, value in inventory.items():
        if value >= 1:
            result.append((key, value))            

    return result
