<?php
//"[MERCHANTNAME]",
//"[MERCHANTPROMOCOUNT]",
//"[MERCHANTFIRSTPROMOTITLE]",
//"[MERCHANTMAXDISCOUNT]",
//"[MERCHANTAVERAGEDISCOUNT]",
//"[YEAR]",
//"[YEAR+5]",
//"[MONTH]",
//"[MONTH+5]",
//"[DAY]",
//"[KEYWORD1]",
//"[KEYWORD2]",
//"[KEYWORD3]",
//"[KEYWORD4]",
//"[KEYWORD5]",
//"[TAGPROMOCOUNT]",
//"[TAGFIRSTPROMOTITLE]",
//"[TAGMAXDISCOUNT]",

//"[MERCHANTALIASNAME]"
//"[ALIAS_OR_NAME]"
//"[PROMOTIONDETAIL]",
//"[STRINGTOTALCOUNT]",
//"[MERCHANTCODECOUNT]",
//"[MERCHANTDEALCOUNT]",
//"[STOREDESCRIPTION]",
//"[MERCHANTDOMAIN]",
//"[KEYWORD1_LOWER]",
//"[KEYWORD2_LOWER]",
//"[KEYWORD3_LOWER]",
//"[KEYWORD4_LOWER]",
//"[KEYWORD5_LOWER]",
//"[MERCHANTAVERAGESAVINGS]",
//"[STRMERCHANTAVERAGESAVINGS]"
//"[STR2MERCHANTAVERAGESAVINGS]"
//"[TOTALSTORECOUNT]"
//"[TOTALPROMOCOUNT]"
//"[SITENAME]"
//"[LETTER]"
//"[TOPICNAME]"
//"[MERCHANTPROMOCOUNT+]"

$meta_page = 'default';
$_SiteMeta[$meta_page]['Title']										= "优惠券，折扣码，免邮促销，全球知名优惠码频道 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "这里我们提供了大量免费的，在线的折扣信息，覆盖各个热门分类，全球知名商家，使用我们提供的折扣码，促销信息购买商品使您享受大的折扣优惠，购物更省钱。";
$_SiteMeta[$meta_page]['Keywords']									= "优惠码，折扣，免费邮寄，包邮促销，免邮促销";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * homepage
 */
$meta_page = 'index';
$_SiteMeta[$meta_page]['Title']										= "优惠券，折扣码，免邮促销，全球知名优惠码频道 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "这里我们提供了大量免费的，在线的折扣信息，覆盖各个热门分类，全球知名商家，使用我们提供的折扣码，促销信息购买商品使您享受大的折扣优惠，购物更省钱。";
$_SiteMeta[$meta_page]['Keywords']									= "优惠码，折扣，免费邮寄，包邮促销，免邮促销";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";


/*
 * merchant
 */
$meta_page = 'merchant';
$meta_index = 0;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME][KEYWORD1]，[KEYWORD2]，下单最高可获得[MERCHANTMAXDISCOUNT]优惠 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "使用我们提供的[MERCHANTPROMOCOUNT]条有效的[MERCHANTNAME][KEYWORD3]，优惠码信息购买商品，可立可享受[MERCHANTMAXDISCOUNT]优惠. 今日最新。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]优惠码，[MERCHANTNAME]折扣码，[MERCHANTNAME]免邮促销，[MERCHANTNAME]在线促销";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我们提供优惠信息的商家之一，在这里您可以找到更多的、更全的、更及时的大量优惠码，折扣信息，目前共有[MERCHANTNAME]的各种优惠码，折扣信息[MERCHANTPROMOCOUNT]条，现在下单购买[MERCHANTNAME]的在线商品，最高可获得[MERCHANTMAXDISCOUNT]优惠，购物更省钱。";

$meta_index = 1;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME][KEYWORD1]，[KEYWORD3]，最高省[MERCHANTMAXDISCOUNT]，更新：[YEAR+5]年[MONTH+5]月 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "我们提供了[MERCHANTPROMOCOUNT]条有效在线[MERCHANTNAME][KEYWORD4]促销，折扣信息，现在购买立可享受减[MERCHANTMAXDISCOUNT]优惠。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]优惠券，[MERCHANTNAME]折扣码，[MERCHANTNAME]免邮促销，[MERCHANTNAME]免邮优惠";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我们为用户提供优惠码，折扣的商家之一，目前该商家共有折扣信息[MERCHANTPROMOCOUNT]条，您可以通过使用这些优惠码，促销等折扣信息，下单购买[MERCHANTNAME]的在线商品，最高可获得[MERCHANTMAXDISCOUNT]优惠，后面会有的更多，更全的，更及时的[MERCHANTNAME]促销信息提供给您。";

$meta_index = 2;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME]有效[KEYWORD1]，[KEYWORD3]，最高可省[MERCHANTMAXDISCOUNT]，更新：[YEAR+5]年[MONTH+5]月 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "我们提供了[MERCHANTPROMOCOUNT]条及时的、有效的在线[MERCHANTNAME][KEYWORD4]促销，优惠码信息，现在购买立可享受减[MERCHANTMAXDISCOUNT]优惠。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]优惠券，[MERCHANTNAME]折扣码，[MERCHANTNAME]免邮促销，[MERCHANTNAME]免邮优惠";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我们为用户提供优惠码，折扣的商家之一，目前该商家共有折扣信息[MERCHANTPROMOCOUNT]条，您可以通过使用这些优惠码，促销等折扣信息，下单购买[MERCHANTNAME]的在线商品，最高可获得[MERCHANTMAXDISCOUNT]优惠，后面会有更多的、更全的、更及时的[MERCHANTNAME]促销信息提供给您。";

$_SiteMeta['StoreDescription'][0] = [
    $_SiteMeta[$meta_page][0]['StoreDesc'],
];
$_SiteMeta['StoreDescription'][1] = [
    $_SiteMeta[$meta_page][1]['StoreDesc'],
];
$_SiteMeta['StoreDescription'][2] = [
    $_SiteMeta[$meta_page][2]['StoreDesc'],
];

/*
 * category
 */
$meta_page = 'category';
$_SiteMeta[$meta_page]['Title']										= "免费[CATEGORYNAME]优惠码，折扣活动 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "[CATEGORYNAME][YEAR+5]年[MONTH+5]月最新优惠，折扣信息";
$_SiteMeta[$meta_page]['Keywords']									= "[CATEGORYNAME]优惠码，[CATEGORYNAME]折扣，[CATEGORYNAME]促销，[CATEGORYNAME]热门商家";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "[CATEGORYNAME]促销";

/*
 * all category
 */
$meta_page = 'allcategories';
$_SiteMeta[$meta_page]['Title']										= "所有分类 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "浏览全部分类，可查找热门促销，优惠，折扣活动";
$_SiteMeta[$meta_page]['Keywords']									= "优惠码，折扣，免费邮寄，包邮促销，免邮促销";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']	                                    = "所有分类";

/*
 * all store
 */
$meta_page = 'allstores';
$_SiteMeta[$meta_page]['Title']										= "浏览字母开头的商家：A-Z，获取及时，有效的折扣信息";
$_SiteMeta[$meta_page]['Description']								= "这里我们提供了大量免费的，在线的折扣信息，覆盖各个热门分类，全球知名商家，使用我们提供的折扣码，促销信息购买商品使您享受大的折扣优惠，购物更省钱。";
$_SiteMeta[$meta_page]['Keywords']									= "优惠码，折扣，免费邮寄，包邮促销，免邮促销";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "全部商家：A-Z";

$meta_page = 'store';
$_SiteMeta[$meta_page]['Title']										= "浏览字母[LETTER]开头的商家，获取及时，有效的折扣信息";
$_SiteMeta[$meta_page]['Description']								= "这里我们提供了大量免费的，在线的折扣信息，覆盖各个热门分类，全球知名商家，使用我们提供的折扣码，促销信息购买商品使您享受大的折扣优惠，购物更省钱。";
$_SiteMeta[$meta_page]['Keywords']									= "优惠码，折扣，免费邮寄，包邮促销，免邮促销";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "浏览字母[LETTER]开头的商家";

/*
 * all tag & tag by char
 */
$meta_page = 'alltags';
$_SiteMeta[$meta_page]['Title']										= "Discount Codes & Vouchers for All Brands & Products";
$_SiteMeta[$meta_page]['Description']								= "Browse discount codes & vouchers for all brands & products A-Z. Search for top discount vouchers & deals through your favorite brands and products.";
$_SiteMeta[$meta_page]['Keywords']									= "Discount Codes, Vouchers, Promo Codes, Offers, Deals, Shopping Vouchers";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Browse Brands & Products A-Z";

$meta_page = 'alltagchar';
$_SiteMeta[$meta_page]['Title']										= "Browse Hot Vouchers for All Brands & Products By [LETTER]";
$_SiteMeta[$meta_page]['Description']								= "Save money with free discount codes & offers for hot brands & products by [LETTER] at [SITENAME]. Search discount vouchers for your favorite brands.";
$_SiteMeta[$meta_page]['Keywords']									= "Discount Codes, Vouchers, Promo Codes, Offers, Deals, Money Off Vouchers";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Browse Brands & Products by [LETTER]";

/*
 * all topic
 */
$meta_page = 'topic';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * search coupon
 */
$meta_page = 'search_coupon';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * save coupon
 */
$meta_page = 'save_coupon';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * coupon
 */
$meta_page = 'coupon';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * code
 */
$meta_page = 'code';
$_SiteMeta[$meta_page]['Title']										= "Browse All Discount Codes & Vouchers for [MONTH+5] [YEAR+5]";
$_SiteMeta[$meta_page]['Description']								= "Find all the latest promotions including promo codes, deals, free delivery & site wide vouchers at [SITENAME]. Save money for your favorite stores.";
$_SiteMeta[$meta_page]['Keywords']									= "Vouchers, Discount Codes, Promo Codes, Voucher Codes";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Online Discount Codes";

/*
 * deal
 */
$meta_page = 'deal';
$_SiteMeta[$meta_page]['Title']										= "All Online Discount Vouchers & Deals in [MONTH+5] [YEAR+5] | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "Grab great savings w/ all our latest discount deals & vouchers for thousands of stores.";
$_SiteMeta[$meta_page]['Keywords']									= "Online Deals, Discount Deals, Sales, Vouchers, Best Deals";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Online Deals";

/*
 * productdeal
 */
$meta_page = 'productdeal';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";
/*
 * instore
 */
$meta_page = 'instore';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * freeshipping
 */
$meta_page = 'freeshipping';
$_SiteMeta[$meta_page]['Title']										= "Free Delivery Discount Codes & Vouchers in [MONTH+5] [YEAR+5] | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "Get free delivery promo codes & discount vouchers at [SITENAME]. Lower your shipping cost from favorite stores.";
$_SiteMeta[$meta_page]['Keywords']									= "Free Delivery Code, Free Shipping Code, Free Delivery Vouchers, Free Delivey Discounts";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Free Delivery Vouchers";

/*
 * sitewide
 */
$meta_page = 'sitewide';
$_SiteMeta[$meta_page]['Title']										= "[YEAR] Site Wide Vouchers & Discount Codes From [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "Browse all the up-dated site wide discount vouchers & promo codes for extra savings. Updated at [MONTH] [YEAR] by [SITENAME].";
$_SiteMeta[$meta_page]['Keywords']									= "Site Wide Sales, Site Wide Offers, Site Wide Vouchers, Site Wide Codes,Vouchers";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Site Wide Vouchers";

/*
 * 410
 */
$meta_page = '410';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * privacy
 */
$meta_page = 'privacy_policy';
$_SiteMeta[$meta_page]['Title']										= "Privacy Policy| [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "[SITENAME] provides free and exclusive voucher codes, discount codes and discount vouchers for UK's popular online stores. Save money with our latest and daily updated promo codes and deals for your favorite stores.";
$_SiteMeta[$meta_page]['Keywords']									= "Vouchers, Discount Codes, Promo Codes, Offers, Deals";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Privacy Policy";

/*
 * termsofuse
 */
$meta_page = 'terms_of_use';
$_SiteMeta[$meta_page]['Title']										= "Terms of Use  | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "[SITENAME] provides free and exclusive voucher codes, discount codes and discount vouchers for UK's popular online stores. Save money with our latest and daily updated promo codes and deals for your favorite stores.";
$_SiteMeta[$meta_page]['Keywords']									= "Vouchers, Discount Codes, Promo Codes, Offers, Deals";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Terms of Use";

/*
 * contactus
 */
$meta_page = 'contact_us';
$_SiteMeta[$meta_page]['Title']										= "Contact Us | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "Discover all the latest discount codes, vouchers & deals for thousands of stores at [SITENAME]. Contact us when you have any questions. ";
$_SiteMeta[$meta_page]['Keywords']									= "Vouchers, Discount Codes, Promo Codes, Offers, Deals";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "Contact Us";

/*
 * faq
 */
$meta_page = 'help';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * aboutus
 */
$meta_page = 'about_us';
$_SiteMeta[$meta_page]['Title']										= "About Us | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "[SITENAME]'s mission is to help you to save while shopping at thousands of online stores. You can find all the latest discount codes, vouchers & deals for your favorite stores at [SITENAME].";
$_SiteMeta[$meta_page]['Keywords']									= "Vouchers, Discount Codes, Promo Codes, Offers, Deals";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "About Us";

/*
 * couponalert
 */
$meta_page = 'couponalert';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";


/*
 * adddeal
 */
$meta_page = 'adddeal';
$_SiteMeta[$meta_page]['Title']										= "";
$_SiteMeta[$meta_page]['Description']								= "";
$_SiteMeta[$meta_page]['Keywords']									= "";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

?>