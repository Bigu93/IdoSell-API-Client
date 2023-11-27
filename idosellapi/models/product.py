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
        iconsmall: str,
        iconmini: str,
        iconsecond: Optional[str],
        dateAdd: datetime,
        size: str,
        sizesecond: Optional[str],
        exto: Optional[str],
        ext: Optional[str],
        exts: Optional[str],
        extsecond: Optional[str],
        extssecond: Optional[str],
        extm: Optional[str],
        urlvaro: Optional[str],
        urlvar: Optional[str],
        urlvars: Optional[str],
        urlvarsecond: Optional[str],
        urlvarssecond: Optional[str],
        iconsmallsecond: Optional[str],
        sizesmall: str,
        sizesmallsecond: Optional[str],
        productAuctionIconExists: str,
        productAuctionIconLargeSize: str,
        productAuctionIconSmallUrl: str,
        productAuctionIconLargeUrl: str,
        productAuctionIconLargeWidth: int,
        productAuctionIconLargeHeight: int,
        productAuctionIconHash: str,
    ) -> None:
        self.icon_small = iconsmall
        self.icon_mini = iconmini
        self.icon_second = iconsecond
        self.date_add = dateAdd
        self.size = size
        self.size_second = sizesecond
        self.exto = exto
        self.ext = ext
        self.exts = exts
        self.ext_second = extsecond
        self.exts_second = extssecond
        self.extm = extm
        self.url_varo = urlvaro
        self.url_var = urlvar
        self.url_vars = urlvars
        self.url_var_second = urlvarsecond
        self.url_vars_second = urlvarssecond
        self.icon_small_second = iconsmallsecond
        self.size_small = sizesmall
        self.size_small_second = sizesmallsecond
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
        iconlargedate: datetime,
        iconsmallwidth: int,
        iconsmallheight: int,
        iconsmallsize: str,
        iconsmalldate: datetime,
        productIconExists: str,
        productIconSmallUrl: str,
        productIconLargeUrl: str,
        productIconLargeWidth: int,
        productIconLargeHeight: int,
        productIconLargeSize: str,
        productIconHash: str,
    ) -> None:
        self.icon_large_date = iconlargedate
        self.icon_small_width = iconsmallwidth
        self.icon_small_height = iconsmallheight
        self.icon_small_size = iconsmallsize
        self.icon_small_date = iconsmalldate
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
        self.lang_dd = langId
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
    def __init__(self, url: str, langid: str, shopId: Optional[int]) -> None:
        self.url = url
        self.lang_id = langid
        self.shop_id = shopId


class Result:
    def __init__(
        self,
        url_lang_data: List[URLLangDatum],
        productIndividualDescriptionsData: List[ProductIndividualDescriptionsDatum],
        sizeschart: int,
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
        productParametersDistinction: List[ProductParametersDistinction],
        productDiscount: ProductDiscount,
        productSizes: List[ProductSize],
        **kwargs,
    ) -> None:
        self.url_lang_data = url_lang_data
        self.product_individual_descriptions_data = productIndividualDescriptionsData
        self.sizes_chart = sizeschart
        self.last_purchase_price = last_purchase_price
        self.product_id = productId
        self.product_descriptions_lang_data = productDescriptionsLangData
        self.product_displayed_code = productDisplayedCode
        self.product_note = productNote
        self.size_chart_id = sizeChartId
        self.size_chart_name = sizeChartName
        self.category_came = categoryName
        self.product_icon = productIcon
        self.product_auction_icon = productAuctionIcon
        self.product_images = productImages
        self.product_in_new = productInNew
        self.product_retail_price = productRetailPrice
        self.product_wholesale_price = productWholesalePrice
        self.product_minimal_price = productMinimalPrice
        self.product_pos_price = productPosPrice
        self.product_strikethrough_retail_price = productStrikethroughRetailPrice
        self.product_purchase_price_gross_last = productPurchasePriceGrossLast
        self.product_weight = productWeight
        self.product_complex_notes = productComplexNotes
        self.product_parameters_distinction = productParametersDistinction
        self.product_discount = productDiscount
        self.product_sizes = productSizes
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
