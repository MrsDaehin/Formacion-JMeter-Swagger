import connexion
import six

from swagger_server.models.item_principal import ItemPrincipal  # noqa: E501
from swagger_server import util


def search_inventory(searchString=None, skip=None, limit=None):  # noqa: E501
    """searches inventory

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param searchString: pass an optional search string for looking up inventory
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[ItemPrincipal]
    """
    return 'do some magic!'
