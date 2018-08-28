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
$_SiteMeta[$meta_page]['Title']										= "優惠券，摺扣碼，免郵促銷，全球知名優惠碼頻道 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "這裏我們提供瞭大量免費的，在綫的摺扣信息，覆蓋各個熱門分類，全球知名商傢，使用我們提供的摺扣碼，促銷信息購買商品使您享受大的摺扣優惠，購物更省錢。";
$_SiteMeta[$meta_page]['Keywords']									= "優惠碼，摺扣，免費郵寄，包郵促銷，免郵促銷";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";

/*
 * homepage
 */
$meta_page = 'index';
$_SiteMeta[$meta_page]['Title']										= "優惠券，摺扣碼，免郵促銷，全球知名優惠碼頻道 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "這裏我們提供瞭大量免費的，在綫的摺扣信息，覆蓋各個熱門分類，全球知名商傢，使用我們提供的摺扣碼，促銷信息購買商品使您享受大的摺扣優惠，購物更省錢。";
$_SiteMeta[$meta_page]['Keywords']									= "優惠碼，摺扣，免費郵寄，包郵促銷，免郵促銷";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "";


/*
 * merchant
 */
$meta_page = 'merchant';
$meta_index = 0;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME][KEYWORD1]，[KEYWORD2]，下單最高可獲得[MERCHANTMAXDISCOUNT]優惠 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "使用我們提供的[MERCHANTPROMOCOUNT]條有效的[MERCHANTNAME][KEYWORD3]，優惠碼信息購買商品，可立可享受[MERCHANTMAXDISCOUNT]優惠. 今日最新。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]優惠碼，[MERCHANTNAME]摺扣碼，[MERCHANTNAME]免郵促銷，[MERCHANTNAME]在綫促銷";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我們提供優惠信息的商傢之一，在這裏您可以找到更多的、更全的、更及時的大量優惠碼，摺扣信息，目前共有[MERCHANTNAME]的各種優惠碼，摺扣信息[MERCHANTPROMOCOUNT]條，現在下單購買[MERCHANTNAME]的在綫商品，最高可獲得[MERCHANTMAXDISCOUNT]優惠，購物更省錢。";

$meta_index = 1;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME][KEYWORD1]，[KEYWORD3]，最高省[MERCHANTMAXDISCOUNT]，更新：[YEAR+5]年[MONTH+5]月 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "我們提供瞭[MERCHANTPROMOCOUNT]條有效在綫[MERCHANTNAME][KEYWORD4]促銷，摺扣信息，現在購買立可享受減[MERCHANTMAXDISCOUNT]優惠。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]優惠券，[MERCHANTNAME]摺扣碼，[MERCHANTNAME]免郵促銷，[MERCHANTNAME]免郵優惠";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我們為用戶提供優惠碼，摺扣的商傢之一，目前該商傢共有摺扣信息[MERCHANTPROMOCOUNT]條，您可以通過使用這些優惠碼，促銷等摺扣信息，下單購買[MERCHANTNAME]的在綫商品，最高可獲得[MERCHANTMAXDISCOUNT]優惠，後麵會有的更多，更全的，更及時的[MERCHANTNAME]促銷信息提供給您。";

$meta_index = 2;
$_SiteMeta[$meta_page][$meta_index]['Title'] 				= "[MERCHANTNAME]有效[KEYWORD1]，[KEYWORD3]，最高可省[MERCHANTMAXDISCOUNT]，更新：[YEAR+5]年[MONTH+5]月 | [SITENAME]";
$_SiteMeta[$meta_page][$meta_index]['Description']			= "我們提供瞭[MERCHANTPROMOCOUNT]條及時的、有效的在綫[MERCHANTNAME][KEYWORD4]促銷，優惠碼信息，現在購買立可享受減[MERCHANTMAXDISCOUNT]優惠。";
$_SiteMeta[$meta_page][$meta_index]['Keywords']				= "[MERCHANTNAME]優惠券，[MERCHANTNAME]摺扣碼，[MERCHANTNAME]免郵促銷，[MERCHANTNAME]免郵優惠";
$_SiteMeta[$meta_page][$meta_index]['StoreDesc']			= "[MERCHANTNAME]是我們為用戶提供優惠碼，摺扣的商傢之一，目前該商傢共有摺扣信息[MERCHANTPROMOCOUNT]條，您可以通過使用這些優惠碼，促銷等摺扣信息，下單購買[MERCHANTNAME]的在綫商品，最高可獲得[MERCHANTMAXDISCOUNT]優惠，後麵會有更多的、更全的、更及時的[MERCHANTNAME]促銷信息提供給您。";

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
$_SiteMeta[$meta_page]['Title']										= "免費[CATEGORYNAME]優惠碼，摺扣活動 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "[CATEGORYNAME][YEAR+5]年[MONTH+5]月最新優惠，摺扣信息";
$_SiteMeta[$meta_page]['Keywords']									= "[CATEGORYNAME]優惠碼，[CATEGORYNAME]摺扣，[CATEGORYNAME]促銷，[CATEGORYNAME]熱門商傢";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "[CATEGORYNAME]促銷";

/*
 * all category
 */
$meta_page = 'allcategories';
$_SiteMeta[$meta_page]['Title']										= "所有分類 | [SITENAME]";
$_SiteMeta[$meta_page]['Description']								= "瀏覽全部分類，可查找熱門促銷，優惠，摺扣活動";
$_SiteMeta[$meta_page]['Keywords']									= "優惠碼，摺扣，免費郵寄，包郵促銷，免郵促銷";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']	                                    = "所有分類";

/*
 * all store
 */
$meta_page = 'allstores';
$_SiteMeta[$meta_page]['Title']										= "瀏覽字母開頭的商傢：A-Z，獲取及時，有效的摺扣信息";
$_SiteMeta[$meta_page]['Description']								= "這裏我們提供瞭大量免費的，在綫的摺扣信息，覆蓋各個熱門分類，全球知名商傢，使用我們提供的摺扣碼，促銷信息購買商品使您享受大的摺扣優惠，購物更省錢。";
$_SiteMeta[$meta_page]['Keywords']									= "優惠碼，摺扣，免費郵寄，包郵促銷，免郵促銷";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "全部商傢：A-Z";

$meta_page = 'store';
$_SiteMeta[$meta_page]['Title']										= "瀏覽字母[LETTER]開頭的商傢，獲取及時，有效的摺扣信息";
$_SiteMeta[$meta_page]['Description']								= "這裏我們提供瞭大量免費的，在綫的摺扣信息，覆蓋各個熱門分類，全球知名商傢，使用我們提供的摺扣碼，促銷信息購買商品使您享受大的摺扣優惠，購物更省錢。";
$_SiteMeta[$meta_page]['Keywords']									= "優惠碼，摺扣，免費郵寄，包郵促銷，免郵促銷";
$_SiteMeta[$meta_page]['HeadLine']									= "";
$_SiteMeta[$meta_page]['H1']										= "瀏覽字母[LETTER]開頭的商傢";

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