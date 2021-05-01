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


class QualifiersType(object):
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
        'item_condition': 'str',
        'item_subcondition': 'str',
        'fulfillment_channel': 'str',
        'ships_domestically': 'str',
        'shipping_time': 'ShippingTimeType',
        'seller_positive_feedback_rating': 'str'
    }

    attribute_map = {
        'item_condition': 'ItemCondition',
        'item_subcondition': 'ItemSubcondition',
        'fulfillment_channel': 'FulfillmentChannel',
        'ships_domestically': 'ShipsDomestically',
        'shipping_time': 'ShippingTime',
        'seller_positive_feedback_rating': 'SellerPositiveFeedbackRating'
    }

    def __init__(self, item_condition=None, item_subcondition=None, fulfillment_channel=None, ships_domestically=None, shipping_time=None, seller_positive_feedback_rating=None, _configuration=None):  # noqa: E501
        """QualifiersType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._item_condition = None
        self._item_subcondition = None
        self._fulfillment_channel = None
        self._ships_domestically = None
        self._shipping_time = None
        self._seller_positive_feedback_rating = None
        self.discriminator = None

        self.item_condition = item_condition
        self.item_subcondition = item_subcondition
        self.fulfillment_channel = fulfillment_channel
        self.ships_domestically = ships_domestically
        self.shipping_time = shipping_time
        self.seller_positive_feedback_rating = seller_positive_feedback_rating

    @property
    def item_condition(self):
        """Gets the item_condition of this QualifiersType.  # noqa: E501

        The condition of the item. Possible values: New, Used, Collectible, Refurbished, or Club.  # noqa: E501

        :return: The item_condition of this QualifiersType.  # noqa: E501
        :rtype: str
        """
        return self._item_condition

    @item_condition.setter
    def item_condition(self, item_condition):
        """Sets the item_condition of this QualifiersType.

        The condition of the item. Possible values: New, Used, Collectible, Refurbished, or Club.  # noqa: E501

        :param item_condition: The item_condition of this QualifiersType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and item_condition is None:
            raise ValueError("Invalid value for `item_condition`, must not be `None`")  # noqa: E501

        self._item_condition = item_condition

    @property
    def item_subcondition(self):
        """Gets the item_subcondition of this QualifiersType.  # noqa: E501

        The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.  # noqa: E501

        :return: The item_subcondition of this QualifiersType.  # noqa: E501
        :rtype: str
        """
        return self._item_subcondition

    @item_subcondition.setter
    def item_subcondition(self, item_subcondition):
        """Sets the item_subcondition of this QualifiersType.

        The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.  # noqa: E501

        :param item_subcondition: The item_subcondition of this QualifiersType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and item_subcondition is None:
            raise ValueError("Invalid value for `item_subcondition`, must not be `None`")  # noqa: E501

        self._item_subcondition = item_subcondition

    @property
    def fulfillment_channel(self):
        """Gets the fulfillment_channel of this QualifiersType.  # noqa: E501

        The fulfillment channel for the item. Possible values:  * Amazon - Fulfilled by Amazon. * Merchant - Fulfilled by the seller.  # noqa: E501

        :return: The fulfillment_channel of this QualifiersType.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_channel

    @fulfillment_channel.setter
    def fulfillment_channel(self, fulfillment_channel):
        """Sets the fulfillment_channel of this QualifiersType.

        The fulfillment channel for the item. Possible values:  * Amazon - Fulfilled by Amazon. * Merchant - Fulfilled by the seller.  # noqa: E501

        :param fulfillment_channel: The fulfillment_channel of this QualifiersType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fulfillment_channel is None:
            raise ValueError("Invalid value for `fulfillment_channel`, must not be `None`")  # noqa: E501

        self._fulfillment_channel = fulfillment_channel

    @property
    def ships_domestically(self):
        """Gets the ships_domestically of this QualifiersType.  # noqa: E501

        Indicates whether the marketplace specified in the request and the location that the item ships from are in the same country. Possible values: True, False, or Unknown.  # noqa: E501

        :return: The ships_domestically of this QualifiersType.  # noqa: E501
        :rtype: str
        """
        return self._ships_domestically

    @ships_domestically.setter
    def ships_domestically(self, ships_domestically):
        """Sets the ships_domestically of this QualifiersType.

        Indicates whether the marketplace specified in the request and the location that the item ships from are in the same country. Possible values: True, False, or Unknown.  # noqa: E501

        :param ships_domestically: The ships_domestically of this QualifiersType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ships_domestically is None:
            raise ValueError("Invalid value for `ships_domestically`, must not be `None`")  # noqa: E501

        self._ships_domestically = ships_domestically

    @property
    def shipping_time(self):
        """Gets the shipping_time of this QualifiersType.  # noqa: E501

        (0-2 days, 3-7 days, 8-13 days, or 14 or more days) � Indicates the maximum time within which the item will likely be shipped once an order has been placed.  # noqa: E501

        :return: The shipping_time of this QualifiersType.  # noqa: E501
        :rtype: ShippingTimeType
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this QualifiersType.

        (0-2 days, 3-7 days, 8-13 days, or 14 or more days) � Indicates the maximum time within which the item will likely be shipped once an order has been placed.  # noqa: E501

        :param shipping_time: The shipping_time of this QualifiersType.  # noqa: E501
        :type: ShippingTimeType
        """
        if self._configuration.client_side_validation and shipping_time is None:
            raise ValueError("Invalid value for `shipping_time`, must not be `None`")  # noqa: E501

        self._shipping_time = shipping_time

    @property
    def seller_positive_feedback_rating(self):
        """Gets the seller_positive_feedback_rating of this QualifiersType.  # noqa: E501

        (98-100%, 95-97%, 90-94%, 80-89%, 70-79%, Less than 70%, or Just launched ) � Indicates the percentage of feedback ratings that were positive over the past 12 months.  # noqa: E501

        :return: The seller_positive_feedback_rating of this QualifiersType.  # noqa: E501
        :rtype: str
        """
        return self._seller_positive_feedback_rating

    @seller_positive_feedback_rating.setter
    def seller_positive_feedback_rating(self, seller_positive_feedback_rating):
        """Sets the seller_positive_feedback_rating of this QualifiersType.

        (98-100%, 95-97%, 90-94%, 80-89%, 70-79%, Less than 70%, or Just launched ) � Indicates the percentage of feedback ratings that were positive over the past 12 months.  # noqa: E501

        :param seller_positive_feedback_rating: The seller_positive_feedback_rating of this QualifiersType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and seller_positive_feedback_rating is None:
            raise ValueError("Invalid value for `seller_positive_feedback_rating`, must not be `None`")  # noqa: E501

        self._seller_positive_feedback_rating = seller_positive_feedback_rating

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
        if issubclass(QualifiersType, dict):
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
        if not isinstance(other, QualifiersType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualifiersType):
            return True

        return self.to_dict() != other.to_dict()
