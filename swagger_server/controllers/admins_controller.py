import connexion
import six

from swagger_server.models.item_principal import ItemPrincipal  # noqa: E501
from swagger_server import util


def add_inventory(inventoryItem=None):  # noqa: E501
    """adds an inventory item

    Adds an item to the system # noqa: E501

    :param inventoryItem: Inventory item to add
    :type inventoryItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inventoryItem = ItemPrincipal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
