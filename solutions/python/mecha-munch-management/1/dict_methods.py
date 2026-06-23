"""Functions to manage a users shopping cart items."""

from collections import OrderedDict

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for i in items_to_add:
        if i in current_cart.keys():
            amount = current_cart[i] + 1
            current_cart[i] = amount
        else:
            current_cart[i] = 1
        

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    current_cart = {}

    for n in notes:
        current_cart[n] = 1

    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for k, v in recipe_updates:
        ideas[k] = v

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    new_cart = OrderedDict()
    items = list(cart.keys())
    items.sort()

    for i in items:
        new_cart[i] = cart[i]

    return new_cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    items = list(cart.keys())
    items.sort()
    items.reverse()

    new_cart = OrderedDict()

    for i in items:
        quantity = cart[i]
        aisle = aisle_mapping[i][0]
        needs_cooling = aisle_mapping[i][1]
        new_cart[i] = [quantity, aisle, needs_cooling]
        

    return new_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    items = list(fulfillment_cart.keys())

    for i in items:
        amount_in_stock = store_inventory[i][0]
        amount_in_stock = amount_in_stock - fulfillment_cart[i][0]
        aisle = store_inventory[i][1]
        needs_cooling = store_inventory[i][2]
        if amount_in_stock == 0:
            store_inventory[i] = ["Out of Stock", aisle, needs_cooling]
        else:
            store_inventory[i] = [amount_in_stock, aisle, needs_cooling]

    return store_inventory
