# swagger_client.CatalogApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item**](CatalogApi.md#get_catalog_item) | **GET** /catalog/v0/items/{asin} | 
[**list_catalog_categories**](CatalogApi.md#list_catalog_categories) | **GET** /catalog/v0/categories | 
[**list_catalog_items**](CatalogApi.md#list_catalog_items) | **GET** /catalog/v0/items | 


# **get_catalog_item**
> GetCatalogItemResponse get_catalog_item(marketplace_id, asin)



Returns a specified item and its attributes.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 2 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
marketplace_id = 'marketplace_id_example' # str | A marketplace identifier. Specifies the marketplace for the item.
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) of the item.

try:
    api_response = api_instance.get_catalog_item(marketplace_id, asin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| A marketplace identifier. Specifies the marketplace for the item. | 
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) of the item. | 

### Return type

[**GetCatalogItemResponse**](GetCatalogItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_categories**
> ListCatalogCategoriesResponse list_catalog_categories(marketplace_id, asin=asin, seller_sku=seller_sku)



Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 1 | 40 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
marketplace_id = 'marketplace_id_example' # str | A marketplace identifier. Specifies the marketplace for the item.
asin = 'asin_example' # str | The Amazon Standard Identification Number (ASIN) of the item. (optional)
seller_sku = 'seller_sku_example' # str | Used to identify items in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit. (optional)

try:
    api_response = api_instance.list_catalog_categories(marketplace_id, asin=asin, seller_sku=seller_sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| A marketplace identifier. Specifies the marketplace for the item. | 
 **asin** | **str**| The Amazon Standard Identification Number (ASIN) of the item. | [optional] 
 **seller_sku** | **str**| Used to identify items in the given marketplace. SellerSKU is qualified by the seller&#39;s SellerId, which is included with every operation that you submit. | [optional] 

### Return type

[**ListCatalogCategoriesResponse**](ListCatalogCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_items**
> ListCatalogItemsResponse list_catalog_items(marketplace_id, query=query, query_context_id=query_context_id, seller_sku=seller_sku, upc=upc, ean=ean, isbn=isbn, jan=jan)



Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 6 | 40 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
marketplace_id = 'marketplace_id_example' # str | A marketplace identifier. Specifies the marketplace for which items are returned.
query = 'query_example' # str | Keyword(s) to use to search for items in the catalog. Example: 'harry potter books'. (optional)
query_context_id = 'query_context_id_example' # str | An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items. (optional)
seller_sku = 'seller_sku_example' # str | Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit. (optional)
upc = 'upc_example' # str | A 12-digit bar code used for retail packaging. (optional)
ean = 'ean_example' # str | A European article number that uniquely identifies the catalog item, manufacturer, and its attributes. (optional)
isbn = 'isbn_example' # str | The unique commercial book identifier used to identify books internationally. (optional)
jan = 'jan_example' # str | A Japanese article number that uniquely identifies the product, manufacturer, and its attributes. (optional)

try:
    api_response = api_instance.list_catalog_items(marketplace_id, query=query, query_context_id=query_context_id, seller_sku=seller_sku, upc=upc, ean=ean, isbn=isbn, jan=jan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| A marketplace identifier. Specifies the marketplace for which items are returned. | 
 **query** | **str**| Keyword(s) to use to search for items in the catalog. Example: &#39;harry potter books&#39;. | [optional] 
 **query_context_id** | **str**| An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items. | [optional] 
 **seller_sku** | **str**| Used to identify an item in the given marketplace. SellerSKU is qualified by the seller&#39;s SellerId, which is included with every operation that you submit. | [optional] 
 **upc** | **str**| A 12-digit bar code used for retail packaging. | [optional] 
 **ean** | **str**| A European article number that uniquely identifies the catalog item, manufacturer, and its attributes. | [optional] 
 **isbn** | **str**| The unique commercial book identifier used to identify books internationally. | [optional] 
 **jan** | **str**| A Japanese article number that uniquely identifies the product, manufacturer, and its attributes. | [optional] 

### Return type

[**ListCatalogItemsResponse**](ListCatalogItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

