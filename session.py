"""
Code for handling sessions in our web application
"""

from bottle import request

import model

def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""


def get_cart_contents():
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
