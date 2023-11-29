from datetime import datetime
from typing import List, Optional


class Authenticate:
    def __init__(self, system_login: Optional[str], system_key: str) -> None:
        self.system_login = system_login
        self.system_key = system_key


class Errors:
    def __init__(self, faultCode: int, faultString: str) -> None:
        self.fault_code = faultCode
        self.fault_string = faultString


class ProductAuctionIcon:
    def __init__(
        self,
        icon_small: str,
        icon_mini: str,
        icon_second: Optional[str],
        dateAdd: datetime,
        size: str,
        size_second: Optional[str],
        ext_o: Optional[str],
        ext: Optional[str],
        ext_s: Optional[str],
        ext_second: Optional[str],
        ext_s_second: Optional[str],
        ext_m: Optional[str],
        url_var_o: Optional[str],
        url_var: Optional[str],
        url_var_s: Optional[str],
        url_var_second: Optional[str],
        url_var_s_second: Optional[str],
        icon_small_second: Optional[str],
        size_small: str,
        size_small_second: Optional[str],
        productAuctionIconExists: str,
        productAuctionIconLargeSize: str,
        productAuctionIconSmallUrl: str,
        productAuctionIconLargeUrl: str,
        productAuctionIconLargeWidth: int,
        productAuctionIconLargeHeight: int,
        productAuctionIconHash: str,
    ) -> None:
        self.icon_small = icon_small
        self.icon_mini = icon_mini
        self.icon_second = icon_second
        self.date_add = dateAdd
        self.size = size
        self.size_second = size_second
        self.ext_o = ext_o
        self.ext = ext
        self.ext_s = ext_s
        self.ext_second = ext_second
        self.ext_s_second = ext_s_second
        self.ext_m = ext_m
        self.url_var_o = url_var_o
        self.url_var = url_var
        self.url_var_s = url_var_s
        self.url_var_second = url_var_second
        self.url_var_s_second = url_var_s_second
        self.icon_small_second = icon_small_second
        self.size_small = size_small
        self.size_small_second = size_small_second
        self.product_auction_icon_exists = productAuctionIconExists
        self.product_auction_icon_large_size = productAuctionIconLargeSize
        self.product_auction_icon_small_url = productAuctionIconSmallUrl
        self.product_auction_icon_large_url = productAuctionIconLargeUrl
        self.product_auction_icon_large_width = productAuctionIconLargeWidth
        self.product_auction_icon_large_height = productAuctionIconLargeHeight
        self.product_auction_icon_hash = productAuctionIconHash


class ProductDescriptionsLangDatum:
    def __init__(
        self,
        langId: str,
        productName: str,
        productAuctionName: str,
        productPriceComparisonSitesName: str,
        productDescription: str,
        productLongDescription: str,
        productAuctionLongDescription: str,
        productMetaTitle: str,
        productMetaDescription: str,
        productMetaKeywords: str,
    ) -> None:
        self.lang_id = langId
        self.product_name = productName
        self.product_auction_name = productAuctionName
        self.product_price_comparison_sites_name = productPriceComparisonSitesName
        self.product_description = productDescription
        self.product_long_description = productLongDescription
        self.product_auction_long_description = productAuctionLongDescription
        self.product_meta_title = productMetaTitle
        self.product_meta_description = productMetaDescription
        self.product_meta_keywords = productMetaKeywords


class ProductDiscount:
    def __init__(self, promoteItemEnabled: str) -> None:
        self.promote_item_enabled = promoteItemEnabled


class ProductIcon:
    def __init__(
        self,
        icon_large_date: datetime,
        icon_small_width: int,
        icon_small_height: int,
        icon_small_size: str,
        icon_small_date: datetime,
        productIconExists: str,
        productIconSmallUrl: str,
        productIconLargeUrl: str,
        productIconLargeWidth: int,
        productIconLargeHeight: int,
        productIconLargeSize: str,
        productIconHash: str,
    ) -> None:
        self.icon_large_date = icon_large_date
        self.icon_small_width = icon_small_width
        self.icon_small_height = icon_small_height
        self.icon_small_size = icon_small_size
        self.icon_small_date = icon_small_date
        self.product_icon_Exists = productIconExists
        self.product_icon_small_url = productIconSmallUrl
        self.product_icon_large_url = productIconLargeUrl
        self.product_icon_large_width = productIconLargeWidth
        self.product_icon_large_height = productIconLargeHeight
        self.product_icon_large_size = productIconLargeSize
        self.product_icon_hash = productIconHash


class ProductImage:
    def __init__(
        self,
        productImageLargeUrl: str,
        productImageMediumUrl: str,
        productImageSmallUrl: str,
        productImageId: str,
        productImageWidth: int,
        productImageHeight: int,
        productImageSize: str,
        productImageDate: datetime,
        productImagePriority: Optional[str],
        productImageHash: str,
    ) -> None:
        self.product_image_large_url = productImageLargeUrl
        self.product_image_medium_url = productImageMediumUrl
        self.product_image_small_url = productImageSmallUrl
        self.product_image_id = productImageId
        self.product_image_width = productImageWidth
        self.product_image_height = productImageHeight
        self.product_image_size = productImageSize
        self.product_image_date = productImageDate
        self.product_image_priority = productImagePriority
        self.product_image_hash = productImageHash


class ProductIndividualDescriptionsDatum:
    def __init__(
        self,
        shopId: int,
        langId: str,
        productName: str,
        productDescription: str,
        productLongDescription: str,
    ) -> None:
        self.shop_id = shopId
        self.lang_id = langId
        self.product_name = productName
        self.product_description = productDescription
        self.product_longDescription = productLongDescription


class ProductParametersDistinction:
    def __init__(
        self,
        parameterId: int,
        parameterName: str,
        parameterValueId: int,
        parameterValueName: str,
    ) -> None:
        self.parameter_id = parameterId
        self.parameter_name = parameterName
        self.parameter_value_id = parameterValueId
        self.parameter_value_name = parameterValueName


class ProductSize:
    def __init__(self, sizeId: str, sizePanelName: int) -> None:
        self.size_id = sizeId
        self.size_panel_name = sizePanelName


class URLLangDatum:
    def __init__(self, url: str, lang_id: str, shop_id: Optional[int]) -> None:
        self.url = url
        self.lang_id = lang_id
        self.shop_id = shop_id


class Result:
    def __init__(
        self,
        url_lang_data: List[URLLangDatum],
        productIndividualDescriptionsData: List[ProductIndividualDescriptionsDatum],
        last_purchase_price: str,
        productId: int,
        productDescriptionsLangData: List[ProductDescriptionsLangDatum],
        productDisplayedCode: str,
        productNote: str,
        sizeChartId: int,
        sizeChartName: str,
        categoryName: str,
        productIcon: ProductIcon,
        productAuctionIcon: ProductAuctionIcon,
        productImages: List[ProductImage],
        productInNew: str,
        productRetailPrice: int,
        productWholesalePrice: int,
        productMinimalPrice: float,
        productPosPrice: str,
        productStrikethroughRetailPrice: int,
        productPurchasePriceGrossLast: str,
        productWeight: int,
        productComplexNotes: int,
        productParametersDistinction: List[ProductParametersDistinction] = [],
        productDiscount: ProductDiscount = {},
        productSizes: List[ProductSize] = [],
        **kwargs,
    ) -> None:
        self.url_lang_data = [URLLangDatum(**url_data) for url_data in url_lang_data]
        self.individual_descriptions_data = [
            ProductIndividualDescriptionsDatum(**individual_data)
            for individual_data in productIndividualDescriptionsData
        ]
        self.last_purchase_price = last_purchase_price
        self.id = productId
        self.descriptions_lang_data = [
            ProductDescriptionsLangDatum(**lang_data)
            for lang_data in productDescriptionsLangData
        ]
        self.displayed_code = productDisplayedCode
        self.note = productNote
        self.size_chart_id = sizeChartId
        self.size_chart_name = sizeChartName
        self.category_name = categoryName
        self.icon = ProductIcon(**productIcon)
        self.auction_icon = ProductAuctionIcon(**productAuctionIcon)
        self.images = [ProductImage(**image_data) for image_data in productImages]
        self.in_new = productInNew
        self.retail_price = productRetailPrice
        self.wholesale_price = productWholesalePrice
        self.minimal_price = productMinimalPrice
        self.pos_price = productPosPrice
        self.strikethrough_retail_price = productStrikethroughRetailPrice
        self.purchase_price_gross_last = productPurchasePriceGrossLast
        self.weight = productWeight
        self.complex_notes = productComplexNotes
        self.parameters_distinction = [
            ProductParametersDistinction(**param_data)
            for param_data in productParametersDistinction
        ]
        self.discount = ProductDiscount(**productDiscount)
        self.sizes = [ProductSize(**size_data) for size_data in productSizes]
        self.__dict__.update(kwargs)


class Product:
    def __init__(
        self,
        authenticate: Authenticate,
        resultsPage: int,
        resultsLimit: int,
        resultsNumberPage: int,
        resultsNumberAll: int,
        errors: Errors,
        results: List[Result],
        **kwargs,
    ) -> None:
        self.authenticate = authenticate
        self.results_page = resultsPage
        self.results_limit = resultsLimit
        self.results_number_page = resultsNumberPage
        self.results_number_all = resultsNumberAll
        self.errors = errors
        self.results = results
        self.__dict__.update(kwargs)
