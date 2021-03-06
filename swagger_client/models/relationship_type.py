# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RelationshipType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifiers': 'IdentifierType',
        'color': 'str',
        'edition': 'str',
        'flavor': 'str',
        'gem_type': 'list[str]',
        'golf_club_flex': 'str',
        'hand_orientation': 'str',
        'hardware_platform': 'str',
        'material_type': 'list[str]',
        'metal_type': 'str',
        'model': 'str',
        'operating_system': 'list[str]',
        'product_type_subcategory': 'str',
        'ring_size': 'str',
        'shaft_material': 'str',
        'scent': 'str',
        'size': 'str',
        'size_per_pearl': 'str',
        'golf_club_loft': 'DecimalWithUnits',
        'total_diamond_weight': 'DecimalWithUnits',
        'total_gem_weight': 'DecimalWithUnits',
        'package_quantity': 'int',
        'item_dimensions': 'DimensionType'
    }

    attribute_map = {
        'identifiers': 'Identifiers',
        'color': 'Color',
        'edition': 'Edition',
        'flavor': 'Flavor',
        'gem_type': 'GemType',
        'golf_club_flex': 'GolfClubFlex',
        'hand_orientation': 'HandOrientation',
        'hardware_platform': 'HardwarePlatform',
        'material_type': 'MaterialType',
        'metal_type': 'MetalType',
        'model': 'Model',
        'operating_system': 'OperatingSystem',
        'product_type_subcategory': 'ProductTypeSubcategory',
        'ring_size': 'RingSize',
        'shaft_material': 'ShaftMaterial',
        'scent': 'Scent',
        'size': 'Size',
        'size_per_pearl': 'SizePerPearl',
        'golf_club_loft': 'GolfClubLoft',
        'total_diamond_weight': 'TotalDiamondWeight',
        'total_gem_weight': 'TotalGemWeight',
        'package_quantity': 'PackageQuantity',
        'item_dimensions': 'ItemDimensions'
    }

    def __init__(self, identifiers=None, color=None, edition=None, flavor=None, gem_type=None, golf_club_flex=None, hand_orientation=None, hardware_platform=None, material_type=None, metal_type=None, model=None, operating_system=None, product_type_subcategory=None, ring_size=None, shaft_material=None, scent=None, size=None, size_per_pearl=None, golf_club_loft=None, total_diamond_weight=None, total_gem_weight=None, package_quantity=None, item_dimensions=None, _configuration=None):  # noqa: E501
        """RelationshipType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifiers = None
        self._color = None
        self._edition = None
        self._flavor = None
        self._gem_type = None
        self._golf_club_flex = None
        self._hand_orientation = None
        self._hardware_platform = None
        self._material_type = None
        self._metal_type = None
        self._model = None
        self._operating_system = None
        self._product_type_subcategory = None
        self._ring_size = None
        self._shaft_material = None
        self._scent = None
        self._size = None
        self._size_per_pearl = None
        self._golf_club_loft = None
        self._total_diamond_weight = None
        self._total_gem_weight = None
        self._package_quantity = None
        self._item_dimensions = None
        self.discriminator = None

        if identifiers is not None:
            self.identifiers = identifiers
        if color is not None:
            self.color = color
        if edition is not None:
            self.edition = edition
        if flavor is not None:
            self.flavor = flavor
        if gem_type is not None:
            self.gem_type = gem_type
        if golf_club_flex is not None:
            self.golf_club_flex = golf_club_flex
        if hand_orientation is not None:
            self.hand_orientation = hand_orientation
        if hardware_platform is not None:
            self.hardware_platform = hardware_platform
        if material_type is not None:
            self.material_type = material_type
        if metal_type is not None:
            self.metal_type = metal_type
        if model is not None:
            self.model = model
        if operating_system is not None:
            self.operating_system = operating_system
        if product_type_subcategory is not None:
            self.product_type_subcategory = product_type_subcategory
        if ring_size is not None:
            self.ring_size = ring_size
        if shaft_material is not None:
            self.shaft_material = shaft_material
        if scent is not None:
            self.scent = scent
        if size is not None:
            self.size = size
        if size_per_pearl is not None:
            self.size_per_pearl = size_per_pearl
        if golf_club_loft is not None:
            self.golf_club_loft = golf_club_loft
        if total_diamond_weight is not None:
            self.total_diamond_weight = total_diamond_weight
        if total_gem_weight is not None:
            self.total_gem_weight = total_gem_weight
        if package_quantity is not None:
            self.package_quantity = package_quantity
        if item_dimensions is not None:
            self.item_dimensions = item_dimensions

    @property
    def identifiers(self):
        """Gets the identifiers of this RelationshipType.  # noqa: E501

        The identifiers that uniquely identify the item that is related.  # noqa: E501

        :return: The identifiers of this RelationshipType.  # noqa: E501
        :rtype: IdentifierType
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this RelationshipType.

        The identifiers that uniquely identify the item that is related.  # noqa: E501

        :param identifiers: The identifiers of this RelationshipType.  # noqa: E501
        :type: IdentifierType
        """

        self._identifiers = identifiers

    @property
    def color(self):
        """Gets the color of this RelationshipType.  # noqa: E501

        The color variation of the item.  # noqa: E501

        :return: The color of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this RelationshipType.

        The color variation of the item.  # noqa: E501

        :param color: The color of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def edition(self):
        """Gets the edition of this RelationshipType.  # noqa: E501

        The edition variation of the item.  # noqa: E501

        :return: The edition of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this RelationshipType.

        The edition variation of the item.  # noqa: E501

        :param edition: The edition of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def flavor(self):
        """Gets the flavor of this RelationshipType.  # noqa: E501

        The flavor variation of the item.  # noqa: E501

        :return: The flavor of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this RelationshipType.

        The flavor variation of the item.  # noqa: E501

        :param flavor: The flavor of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._flavor = flavor

    @property
    def gem_type(self):
        """Gets the gem_type of this RelationshipType.  # noqa: E501

        The gem type variations of the item.  # noqa: E501

        :return: The gem_type of this RelationshipType.  # noqa: E501
        :rtype: list[str]
        """
        return self._gem_type

    @gem_type.setter
    def gem_type(self, gem_type):
        """Sets the gem_type of this RelationshipType.

        The gem type variations of the item.  # noqa: E501

        :param gem_type: The gem_type of this RelationshipType.  # noqa: E501
        :type: list[str]
        """

        self._gem_type = gem_type

    @property
    def golf_club_flex(self):
        """Gets the golf_club_flex of this RelationshipType.  # noqa: E501

        The golf club flex variation of an item.  # noqa: E501

        :return: The golf_club_flex of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._golf_club_flex

    @golf_club_flex.setter
    def golf_club_flex(self, golf_club_flex):
        """Sets the golf_club_flex of this RelationshipType.

        The golf club flex variation of an item.  # noqa: E501

        :param golf_club_flex: The golf_club_flex of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._golf_club_flex = golf_club_flex

    @property
    def hand_orientation(self):
        """Gets the hand_orientation of this RelationshipType.  # noqa: E501

        The hand orientation variation of an item.  # noqa: E501

        :return: The hand_orientation of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._hand_orientation

    @hand_orientation.setter
    def hand_orientation(self, hand_orientation):
        """Sets the hand_orientation of this RelationshipType.

        The hand orientation variation of an item.  # noqa: E501

        :param hand_orientation: The hand_orientation of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._hand_orientation = hand_orientation

    @property
    def hardware_platform(self):
        """Gets the hardware_platform of this RelationshipType.  # noqa: E501

        The hardware platform variation of an item.  # noqa: E501

        :return: The hardware_platform of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._hardware_platform

    @hardware_platform.setter
    def hardware_platform(self, hardware_platform):
        """Sets the hardware_platform of this RelationshipType.

        The hardware platform variation of an item.  # noqa: E501

        :param hardware_platform: The hardware_platform of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._hardware_platform = hardware_platform

    @property
    def material_type(self):
        """Gets the material_type of this RelationshipType.  # noqa: E501

        The material type variations of an item.  # noqa: E501

        :return: The material_type of this RelationshipType.  # noqa: E501
        :rtype: list[str]
        """
        return self._material_type

    @material_type.setter
    def material_type(self, material_type):
        """Sets the material_type of this RelationshipType.

        The material type variations of an item.  # noqa: E501

        :param material_type: The material_type of this RelationshipType.  # noqa: E501
        :type: list[str]
        """

        self._material_type = material_type

    @property
    def metal_type(self):
        """Gets the metal_type of this RelationshipType.  # noqa: E501

        The metal type variation of an item.  # noqa: E501

        :return: The metal_type of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._metal_type

    @metal_type.setter
    def metal_type(self, metal_type):
        """Sets the metal_type of this RelationshipType.

        The metal type variation of an item.  # noqa: E501

        :param metal_type: The metal_type of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._metal_type = metal_type

    @property
    def model(self):
        """Gets the model of this RelationshipType.  # noqa: E501

        The model variation of an item.  # noqa: E501

        :return: The model of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RelationshipType.

        The model variation of an item.  # noqa: E501

        :param model: The model of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def operating_system(self):
        """Gets the operating_system of this RelationshipType.  # noqa: E501

        The operating system variations of an item.  # noqa: E501

        :return: The operating_system of this RelationshipType.  # noqa: E501
        :rtype: list[str]
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this RelationshipType.

        The operating system variations of an item.  # noqa: E501

        :param operating_system: The operating_system of this RelationshipType.  # noqa: E501
        :type: list[str]
        """

        self._operating_system = operating_system

    @property
    def product_type_subcategory(self):
        """Gets the product_type_subcategory of this RelationshipType.  # noqa: E501

        The product type subcategory variation of an item.  # noqa: E501

        :return: The product_type_subcategory of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._product_type_subcategory

    @product_type_subcategory.setter
    def product_type_subcategory(self, product_type_subcategory):
        """Sets the product_type_subcategory of this RelationshipType.

        The product type subcategory variation of an item.  # noqa: E501

        :param product_type_subcategory: The product_type_subcategory of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._product_type_subcategory = product_type_subcategory

    @property
    def ring_size(self):
        """Gets the ring_size of this RelationshipType.  # noqa: E501

        The ring size variation of an item.  # noqa: E501

        :return: The ring_size of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._ring_size

    @ring_size.setter
    def ring_size(self, ring_size):
        """Sets the ring_size of this RelationshipType.

        The ring size variation of an item.  # noqa: E501

        :param ring_size: The ring_size of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._ring_size = ring_size

    @property
    def shaft_material(self):
        """Gets the shaft_material of this RelationshipType.  # noqa: E501

        The shaft material variation of an item.  # noqa: E501

        :return: The shaft_material of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._shaft_material

    @shaft_material.setter
    def shaft_material(self, shaft_material):
        """Sets the shaft_material of this RelationshipType.

        The shaft material variation of an item.  # noqa: E501

        :param shaft_material: The shaft_material of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._shaft_material = shaft_material

    @property
    def scent(self):
        """Gets the scent of this RelationshipType.  # noqa: E501

        The scent variation of an item.  # noqa: E501

        :return: The scent of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._scent

    @scent.setter
    def scent(self, scent):
        """Sets the scent of this RelationshipType.

        The scent variation of an item.  # noqa: E501

        :param scent: The scent of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._scent = scent

    @property
    def size(self):
        """Gets the size of this RelationshipType.  # noqa: E501

        The size variation of an item.  # noqa: E501

        :return: The size of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RelationshipType.

        The size variation of an item.  # noqa: E501

        :param size: The size of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def size_per_pearl(self):
        """Gets the size_per_pearl of this RelationshipType.  # noqa: E501

        The size per pearl variation of an item.  # noqa: E501

        :return: The size_per_pearl of this RelationshipType.  # noqa: E501
        :rtype: str
        """
        return self._size_per_pearl

    @size_per_pearl.setter
    def size_per_pearl(self, size_per_pearl):
        """Sets the size_per_pearl of this RelationshipType.

        The size per pearl variation of an item.  # noqa: E501

        :param size_per_pearl: The size_per_pearl of this RelationshipType.  # noqa: E501
        :type: str
        """

        self._size_per_pearl = size_per_pearl

    @property
    def golf_club_loft(self):
        """Gets the golf_club_loft of this RelationshipType.  # noqa: E501

        The golf club loft variation of an item.  # noqa: E501

        :return: The golf_club_loft of this RelationshipType.  # noqa: E501
        :rtype: DecimalWithUnits
        """
        return self._golf_club_loft

    @golf_club_loft.setter
    def golf_club_loft(self, golf_club_loft):
        """Sets the golf_club_loft of this RelationshipType.

        The golf club loft variation of an item.  # noqa: E501

        :param golf_club_loft: The golf_club_loft of this RelationshipType.  # noqa: E501
        :type: DecimalWithUnits
        """

        self._golf_club_loft = golf_club_loft

    @property
    def total_diamond_weight(self):
        """Gets the total_diamond_weight of this RelationshipType.  # noqa: E501

        The total diamond weight variation of an item.  # noqa: E501

        :return: The total_diamond_weight of this RelationshipType.  # noqa: E501
        :rtype: DecimalWithUnits
        """
        return self._total_diamond_weight

    @total_diamond_weight.setter
    def total_diamond_weight(self, total_diamond_weight):
        """Sets the total_diamond_weight of this RelationshipType.

        The total diamond weight variation of an item.  # noqa: E501

        :param total_diamond_weight: The total_diamond_weight of this RelationshipType.  # noqa: E501
        :type: DecimalWithUnits
        """

        self._total_diamond_weight = total_diamond_weight

    @property
    def total_gem_weight(self):
        """Gets the total_gem_weight of this RelationshipType.  # noqa: E501

        The total gem weight variation of an item.  # noqa: E501

        :return: The total_gem_weight of this RelationshipType.  # noqa: E501
        :rtype: DecimalWithUnits
        """
        return self._total_gem_weight

    @total_gem_weight.setter
    def total_gem_weight(self, total_gem_weight):
        """Sets the total_gem_weight of this RelationshipType.

        The total gem weight variation of an item.  # noqa: E501

        :param total_gem_weight: The total_gem_weight of this RelationshipType.  # noqa: E501
        :type: DecimalWithUnits
        """

        self._total_gem_weight = total_gem_weight

    @property
    def package_quantity(self):
        """Gets the package_quantity of this RelationshipType.  # noqa: E501

        The package quantity variation of an item.  # noqa: E501

        :return: The package_quantity of this RelationshipType.  # noqa: E501
        :rtype: int
        """
        return self._package_quantity

    @package_quantity.setter
    def package_quantity(self, package_quantity):
        """Sets the package_quantity of this RelationshipType.

        The package quantity variation of an item.  # noqa: E501

        :param package_quantity: The package_quantity of this RelationshipType.  # noqa: E501
        :type: int
        """

        self._package_quantity = package_quantity

    @property
    def item_dimensions(self):
        """Gets the item_dimensions of this RelationshipType.  # noqa: E501

        The item dimensions relationship of an item.  # noqa: E501

        :return: The item_dimensions of this RelationshipType.  # noqa: E501
        :rtype: DimensionType
        """
        return self._item_dimensions

    @item_dimensions.setter
    def item_dimensions(self, item_dimensions):
        """Sets the item_dimensions of this RelationshipType.

        The item dimensions relationship of an item.  # noqa: E501

        :param item_dimensions: The item_dimensions of this RelationshipType.  # noqa: E501
        :type: DimensionType
        """

        self._item_dimensions = item_dimensions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RelationshipType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationshipType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelationshipType):
            return True

        return self.to_dict() != other.to_dict()
