from datetime import datetime
from typing import List, Optional


class Authenticate:
    def __init__(self, system_login: Optional[str], system_key: str) -> None:
        self.system_login = system_login
        self.system_key = system_key


class Errors:
    def __init__(self, faultCode: int, faultString: str) -> None:
        self.faultCode = faultCode
        self.faultString = faultString


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
        self.iconsmall = iconsmall
        self.iconmini = iconmini
        self.iconsecond = iconsecond
        self.dateAdd = dateAdd
        self.size = size
        self.sizesecond = sizesecond
        self.exto = exto
        self.ext = ext
        self.exts = exts
        self.extsecond = extsecond
        self.extssecond = extssecond
        self.extm = extm
        self.urlvaro = urlvaro
        self.urlvar = urlvar
        self.urlvars = urlvars
        self.urlvarsecond = urlvarsecond
        self.urlvarssecond = urlvarssecond
        self.iconsmallsecond = iconsmallsecond
        self.sizesmall = sizesmall
        self.sizesmallsecond = sizesmallsecond
        self.productAuctionIconExists = productAuctionIconExists
        self.productAuctionIconLargeSize = productAuctionIconLargeSize
        self.productAuctionIconSmallUrl = productAuctionIconSmallUrl
        self.productAuctionIconLargeUrl = productAuctionIconLargeUrl
        self.productAuctionIconLargeWidth = productAuctionIconLargeWidth
        self.productAuctionIconLargeHeight = productAuctionIconLargeHeight
        self.productAuctionIconHash = productAuctionIconHash


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
        self.langId = langId
        self.productName = productName
        self.productAuctionName = productAuctionName
        self.productPriceComparisonSitesName = productPriceComparisonSitesName
        self.productDescription = productDescription
        self.productLongDescription = productLongDescription
        self.productAuctionLongDescription = productAuctionLongDescription
        self.productMetaTitle = productMetaTitle
        self.productMetaDescription = productMetaDescription
        self.productMetaKeywords = productMetaKeywords


class ProductDiscount:
    def __init__(self, promoteItemEnabled: str) -> None:
        self.promoteItemEnabled = promoteItemEnabled


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
        self.iconlargedate = iconlargedate
        self.iconsmallwidth = iconsmallwidth
        self.iconsmallheight = iconsmallheight
        self.iconsmallsize = iconsmallsize
        self.iconsmalldate = iconsmalldate
        self.productIconExists = productIconExists
        self.productIconSmallUrl = productIconSmallUrl
        self.productIconLargeUrl = productIconLargeUrl
        self.productIconLargeWidth = productIconLargeWidth
        self.productIconLargeHeight = productIconLargeHeight
        self.productIconLargeSize = productIconLargeSize
        self.productIconHash = productIconHash


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
        self.productImageLargeUrl = productImageLargeUrl
        self.productImageMediumUrl = productImageMediumUrl
        self.productImageSmallUrl = productImageSmallUrl
        self.productImageId = productImageId
        self.productImageWidth = productImageWidth
        self.productImageHeight = productImageHeight
        self.productImageSize = productImageSize
        self.productImageDate = productImageDate
        self.productImagePriority = productImagePriority
        self.productImageHash = productImageHash


class ProductIndividualDescriptionsDatum:
    def __init__(
        self,
        shopId: int,
        langId: str,
        productName: str,
        productDescription: str,
        productLongDescription: str,
    ) -> None:
        self.shopId = shopId
        self.langId = langId
        self.productName = productName
        self.productDescription = productDescription
        self.productLongDescription = productLongDescription


class ProductParametersDistinction:
    def __init__(
        self,
        parameterId: int,
        parameterName: str,
        parameterValueId: int,
        parameterValueName: str,
    ) -> None:
        self.parameterId = parameterId
        self.parameterName = parameterName
        self.parameterValueId = parameterValueId
        self.parameterValueName = parameterValueName


class ProductSize:
    def __init__(self, sizeId: str, sizePanelName: int) -> None:
        self.sizeId = sizeId
        self.sizePanelName = sizePanelName


class URLLangDatum:
    def __init__(self, url: str, langid: str, shopId: Optional[int]) -> None:
        self.url = url
        self.langid = langid
        self.shopid = shopId


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
    ) -> None:
        self.url_lang_data = url_lang_data
        self.productIndividualDescriptionsData = productIndividualDescriptionsData
        self.sizeschart = sizeschart
        self.last_purchase_price = last_purchase_price
        self.productId = productId
        self.productDescriptionsLangData = productDescriptionsLangData
        self.productDisplayedCode = productDisplayedCode
        self.productNote = productNote
        self.sizeChartId = sizeChartId
        self.sizeChartName = sizeChartName
        self.categoryName = categoryName
        self.productIcon = productIcon
        self.productAuctionIcon = productAuctionIcon
        self.productImages = productImages
        self.productInNew = productInNew
        self.productRetailPrice = productRetailPrice
        self.productWholesalePrice = productWholesalePrice
        self.productMinimalPrice = productMinimalPrice
        self.productPosPrice = productPosPrice
        self.productStrikethroughRetailPrice = productStrikethroughRetailPrice
        self.productPurchasePriceGrossLast = productPurchasePriceGrossLast
        self.productWeight = productWeight
        self.productComplexNotes = productComplexNotes
        self.productParametersDistinction = productParametersDistinction
        self.productDiscount = productDiscount
        self.productSizes = productSizes


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
        self.resultsPage = resultsPage
        self.resultsLimit = resultsLimit
        self.resultsNumberPage = resultsNumberPage
        self.resultsNumberAll = resultsNumberAll
        self.errors = errors
        self.results = results
        self.__dict__.update(kwargs)
