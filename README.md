# Amazon Scraper
<p align="center">
    <a href="https://dashboard.smartproxy.com/register?page=ecommerce-scraping-api%2Fpricing&utm_source=socialorganic&utm_medium=social&utm_campaign=github_ecommerce_scraper" ><img src="https://i.imgur.com/v707ui6.png"></a>
</p>

[![](https://dcbadge.vercel.app/api/server/gvJhWJPaB4)](https://discord.gg/sCr34yVDVB)

## List of contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting started](#getting-started)
- [Targets](#targets)
- [Amazon scraping by target](#amazon-scraping-by-target)
  - [Amazon listings](#amazon-listings-amazon)
  - [Amazon product search listing scraping](#amazon-product-search-listing-scraping-amazon_search)
  - [Amazon product page scraping](#amazon-product-scraping-amazon_product)
  - [Amazon product pricing scraping](#amazon-product-pricing-scraping-amazon_pricing)
  - [Amazon product reviews scraping](#amazon-product-reviews-scraping-amazon_reviews)
  - [Amazon product questions & answers scraping](#amazon-product-questions--answers-scraping-amazon_questions)
  - [Amazon product best sellers listing scraping](#amazon-product-best-sellers-listing-scraping-amazon_bestsellers)
- [Response codes](#response-codes)
  - [HTTP response codes](#http-response-codes)
  - [Parsed result response codes](#parsed-result-response-codes)
- [License](#license)

## Introduction
Amazon is a treasure trove of eCommerce information due to its vast database of products, prices, reviews, and sales data. The platform offers valuable insights into the market and competitor strategies, making it an incredibly useful target to extract information from for those seeking to thrive in the digital marketplace.

Smartproxy offers an easy way to gather data from Amazon with the [eCommerce Scraping API](https://smartproxy.com/scraping/ecommerce). It targets various product areas, such as product listings, prices, reviews, and search results, then returns the information in an easy-to-read JSON format.

## Features
 - Ready-made targets to efficiently scrape the most popular Amazon pages
 - Results retrieved as formatted JSON data
 - Quick and simple parameter configuration & authentication
 - No IP blocks or rate limitations thanks to built-in proxies
 - User-friendly web interface with scheduling options

## Getting started
To begin using the eCommerce Scraping API, grab a plan that suits your needs from the [dashboard](https://dashboard.smartproxy.com/ecommerce-scraping-api/). From here, you have two options:
- **Scrape directly from the dashboard**. Navigate to the **Scrapers** tab, click **Create new project**, and select a target from the available options. You can then easily use the web interface to build, make requests, and return results.
- **Get authentication credentials**. If you want to integrate the API into your code, go to the **API Authentication** tab. Here you'll find the automatically generated username, password, or the basic authentication token. You can use them as authentication methods inside your script. Not sure where to start? See the [examples below](#amazon-scraping-by-target).

## Targets
The eCommerce Scraping API targets the following Amazon categories and pages:
- Amazon listings (`amazon`)
- Amazon search results (`amazon_search`)
- Amazon product pages (`amazon_product`)
- Amazon product pricing (`amazon_pricing`)
- Amazon product reviews (`amazon_reviews`)
- Amazon product questions & answers (`amazon_questions`)
- Amazon bestsellers (`amazon_bestsellers`)

## Amazon scraping by target
Amazon can be targeted using one of the target parameters listed in this section. Each target has a unique set of additional parameters that define your search in more detail.

### Amazon listings `amazon`
Retrieve Amazon listings by supplying a full Amazon URL.

#### Parameters
**Required**: `target`, `url`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_search`.|
|`url`        |`string`  | The Amazon URL to retrieve data from. |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon.py > amazon.py`|
| PHP      | [php/amazon.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon.php > amazon.php`|
| Node.js  | [nodejs/amazon.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon.js > amazon.js`|

#### Response example
```
{
  "results": [
    {
      "content": {
        "results": {
          "ads": [
            {
              "pos": 1,
              "asin": "B08J3KYJKM",
              "type": "organic_also_viewed",
              "price": 19.99,
              "title": "Gamenote RGB Headphone Stand & Power Strip 2 in 1 Desk Gaming Headset Holder with 3 USB Charging Ports & 3 Power Outlets Headphones Hanger Accessories for Desktop Gamer",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/61hgSq0CM4L._AC_UL165_SR165,165_.jpg"
              ],
              "rating": 4.7,
              "location": "carousel",
              "price_upper": 19.99,
              "reviews_count": 1956,
              "is_prime_eligible": false
            },
            {
              "pos": 2,
              "asin": "B07XYPXB9Q",
              "type": "organic_also_viewed",
              "price": 130,
              "title": "Razer Kraken Kitty RGB USB Gaming Headset: THX 7.1 Spatial Surround Sound - Chroma RGB Lighting - Retractable Active Noise Cancelling Mic - Lightweight Aluminum Frame - for PC - Quartz Pink",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/814WZ5eAFoL._AC_UL165_SR165,165_.jpg"
              ],
              "rating": 4.5,
              "location": "carousel",
              "price_upper": 130,
              "reviews_count": 9622,
              "is_prime_eligible": false
            },
            {
              "pos": 3,
              "asin": "B09YY5TCMX",
              "type": "organic_also_viewed",
              "price": 39.99,
              "title": "FIFINE Gaming Headset for PC-Wired Headphones with Microphone-7.1 Surround Sound Computer USB Headset for Laptop, Streaming Headphones on PS4/PS5, with EQ Mode, RGB, Soft Ear Pads - AmpliGame H6",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/71LP40TtRHL._AC_UL165_SR165,165_.jpg"
              ],
              "rating": 4.2,
              "location": "carousel",
              "price_upper": 39.99,
              "reviews_count": 1327,
              "is_prime_eligible": false
            },
            {
              "pos": 4,
              "asin": "B07PDFBJZD",
              "type": "organic_also_viewed",
              "price": 99.99,
              "title": "Logitech G PRO X Gaming Headset (2nd Generation) with Blue Voice, DTS Headphone 7.1 and 50 mm PRO-G Drivers, for PC, Xbox One, Xbox Series X|S,PS5,PS4, Nintendo Switch - Black",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/51j6CXF9DYL._AC_UL165_SR165,165_.jpg",
                "https://m.media-amazon.com/images/I/216-OX9rBaL._SS72_.png",
                "https://m.media-amazon.com/images/I/31NojnAY4VL._SS180_.png"
              ],
              "rating": 4.4,
              "location": "carousel",
              "price_upper": 99.99,
              "reviews_count": 6551,
              "is_prime_eligible": false
            },
            {
              "pos": 5,
              "asin": "B00SAYCXWG",
              "type": "organic_also_viewed",
              "price": 59.99,
              "title": "HyperX Cloud II - Gaming Headset, 7.1 Surround Sound, Memory Foam Ear Pads, Durable Aluminum Frame, Detachable Microphone, Works with PC, PS5, PS4, Xbox Series X|S, Xbox One – Red",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/71u77S3CdSL._AC_UL165_SR165,165_.jpg"
              ],
              "rating": 4.5,
              "location": "carousel",
              "price_upper": 59.99,
              "reviews_count": 69409,
              "is_prime_eligible": false
            },
            {
              "pos": 6,
              "asin": "B0779V6BC4",
              "type": "organic_also_viewed",
              "price": 16.99,
              "title": "COZOO Headphone Stand with USB Charger Desktop Gaming Headset Holder Hanger with 3 USB Charging Station and 2 Outlets Power Strip - Suitable for Gaming, DJ, Wireless Earphone Display (Black)",
              "images": [
                "https://images-na.ssl-images-amazon.com/images/I/71BqZAaSzwL._AC_UL165_SR165,165_.jpg"
              ],
              "rating": 4.7,
              "location": "carousel",
              "price_upper": 16.99,
              "reviews_count": 5429,
              "is_prime_eligible": false
            },
            {
              "pos": 7,
              "asin": "B09ZWMYHCT",
              "type": "organic_also_viewed",
              "price": 77.6,
              "title": "SteelSeries New Arctis Nova 3 Multi-Platform Gaming Headset - Signature Arctis Sound - ClearCast Gen 2 Mic - PC, PS5/PS4, Xbox Series X|S, Switch, Mobile,Black",
              "images": [
                "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='100%' width='100%' preserveAspectRatio='none' /%3E",
                "https://m.media-amazon.com/images/I/31UmYBoX3dL._AC_SR100,100_.jpg"
              ],
              "rating": 4.5,
              "location": "carousel",
              "price_upper": 77.6,
              "reviews_count": 45,
              "is_prime_eligible": false
            },
            {
              "pos": 8,
              "asin": "B0C4ND25FT",
              "type": "organic_also_viewed",
              "price": 37.99,
              "title": "FIFINE PC Gaming Headset, USB Headset with 7.1 Surround Sound, Detachable Microphone, Control Box, 3.5mm Headphones Jack, Over-Ear Wired Headset for PS5/PS4/Xbox/Switch, Black-AmpliGame H9",
              "images": [
                "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='100%' width='100%' preserveAspectRatio='none' /%3E",
                "https://m.media-amazon.com/images/I/41TSn76LbZL._AC_SR100,100_.jpg"
              ],
              "rating": 4.3,
              "location": "carousel",
              "price_upper": 37.99,
              "reviews_count": 43,
              "is_prime_eligible": false
            },
            {
              "pos": 9,
              "asin": "B0CLLJC6QC",
              "type": "organic_also_viewed",
              "price": 49.99,
              "title": "Wireless Gaming Headset, 7.1 Surround Sound, 2.4GHz USB Gaming Headphones with Bluetooth 5.3, 100H Battery, ENC Noise Canceling Mic, 3.5mm Wired, RGB Light, Wireless Headset for PC PS5 PS4 Mac Switch",
              "images": [
                "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='100%' width='100%' preserveAspectRatio='none' /%3E",
                "https://m.media-amazon.com/images/I/41PGf7xj-iL._AC_SR100,100_.jpg"
              ],
              "rating": 4.5,
              "location": "carousel",
              "price_upper": 49.99,
              "reviews_count": 45,
              "is_prime_eligible": false
            },
            {
              "pos": 10,
              "asin": "B0BXX49Y2C",
              "type": "organic_also_viewed",
              "price": 39.99,
              "title": "EKSA [2024 New] Fenrir Gaming Headset with Microphone for PS4 PC Xbox one PS5 Switch Laptop, Over Ear Headphones Wired with Noise Cancelling Mic, 3.5m Audio Jack, 50mm Stereo Drivers, Led Light",
              "images": [
                "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='100%' width='100%' preserveAspectRatio='none' /%3E",
                "https://m.media-amazon.com/images/I/413kCBGU1kL._AC_SR100,100_.jpg"
              ],
              "rating": 4.2,
              "location": "carousel",
              "price_upper": 39.99,
              "reviews_count": 42,
              "is_prime_eligible": false
            }
          ],
          "url": "https://www.amazon.com/dp/B08JD3Z1BP/",
          "asin": "B08JD3Z1BP",
          "page": 1,
          "brand": "HP",
          "price": 28.99,
          "stock": "In Stock",
          "title": "HP USB Gaming Headset PC Over Ear Headphones 7.1 Surround Sound with Mic for PC/Mac/Laptop Gamer Headset with Noise Cancelling Mic Comfortable Design and LED Lights",
          "buybox": [
            {
              "price": 28.99,
              "stock": "In Stock",
              "delivery_type": "Delivery",
              "delivery_details": [
                {
                  "date": { "by": "Monday, June 3", "from": null },
                  "type": "FREE delivery"
                },
                {
                  "date": { "by": "Tomorrow, May 29", "from": null },
                  "type": "Or fastest delivery"
                }
              ]
            },
            {
              "price": 28.99,
              "stock": "In Stock",
              "delivery_type": "Pickup",
              "delivery_details": [
                {
                  "date": { "by": "Monday, June 3", "from": null },
                  "type": "FREE pickup"
                },
                {
                  "date": { "by": "Tomorrow, May 29", "from": null },
                  "type": "Or fastest pickup"
                }
              ]
            }
          ],
          "coupon": "",
          "images": [
            "https://m.media-amazon.com/images/I/71fp92LjqCL._AC_SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71IiqDGdyYL._AC_SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71Cy3O-APyL._AC_SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71EYx48r-RL._AC_SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71KLOzPDBvL._AC_SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71QbWxmvflL._AC_SL1250_.jpg"
          ],
          "rating": 4.3,
          "category": [
            {
              "ladder": [
                {
                  "url": "/computer-video-games-hardware-accessories/b/ref=dp_bc_aui_C_1?ie=UTF8&node=468642",
                  "name": "Video Games"
                },
                {
                  "url": "/PC-Games/b/ref=dp_bc_aui_C_2?ie=UTF8&node=229575",
                  "name": "PC"
                },
                {
                  "url": "/PC-Accessories/b/ref=dp_bc_aui_C_3?ie=UTF8&node=318813011",
                  "name": "Accessories"
                },
                {
                  "url": "/PC-Game-Headsets/b/ref=dp_bc_aui_C_4?ie=UTF8&node=402053011",
                  "name": "Headsets"
                }
              ]
            }
          ],
          "currency": "USD",
          "delivery": [
            {
              "date": { "by": "Monday, June 3", "from": null },
              "type": "FREE delivery"
            },
            {
              "date": { "by": "Tomorrow, May 29", "from": null },
              "type": "Or fastest delivery"
            }
          ],
          "_warnings": ["Could not parse pricing count."],
          "page_type": "Product",
          "price_sns": 0,
          "variation": [],
          "has_videos": false,
          "sales_rank": [
            {
              "rank": 7230,
              "ladder": [
                {
                  "url": "/gp/bestsellers/videogames/ref=pd_zg_ts_videogames",
                  "name": "Video Games "
                }
              ]
            },
            {
              "rank": 407,
              "ladder": [
                {
                  "url": "/gp/bestsellers/videogames/402053011/ref=pd_zg_hrsr_videogames",
                  "name": "PC Game Headsets"
                }
              ]
            }
          ],
          "top_review": "Pros:They fit comfortably over my ears and my big head.  For the money, the sound that comes through them is very good quality and microphone works really well and people can hear me just fine. The only con I have is that the microphone does not fold away very well, but I can live with that.\n  \nRead more",
          "asin_in_url": "B08JD3Z1BP",
          "description": "7.1 Virtual Surround Sound-Whether you want to live the game or hear where your enemies are coming from, to win them better, immersive 7.1 Surround Sound offers incredible positional audio.",
          "parent_asin": "B08JD3Z1BP",
          "price_upper": 28.99,
          "pricing_str": "",
          "pricing_url": "https://www.amazon.com/gp/offer-listing/B08JD3Z1BP?startIndex=0",
          "manufacturer": "HP",
          "max_quantity": 30,
          "price_buybox": 28.99,
          "product_name": "HP USB Gaming Headset PC Over Ear Headphones 7.1 Surround Sound with Mic for PC/Mac/Laptop Gamer Headset with Noise Cancelling Mic Comfortable Design and LED Lights",
          "sales_volume": "50+ bought in past month",
          "amazon_choice": true,
          "bullet_points": "TRUE 7.1 SURROUND SOUND EFFECT FOR IMMERSIVE GAMING EXPERIENCE. HP gaming headset adopt superior 50mm audio drivers combined with advanced audio techniques. It delivers quality simulated surround sound to enhance the immersive gaming experience. With the high responsive audio drivers, you can be better to make out the direction from which the sound is coming, like the gun fire, enemy footsteps and scenario indicators. Let you gain the competitive edge you need to take gaming to the next level\nNOISE CANCELING & ANTI-STATIC MICROPHONE FOR CRYSTAL-CLEAR COMMUNICATION. HP gaming headset has a sensitive adjustable microphone using noise canceling techniques. It filters most environmental noise around you and provide real-in-time talking without any delay. Anti-static tech inside gaming headphones prevent static sound from happening. You can chat to your fellow players with crystal clarity sound and enjoy a smooth team-work play\nERGONOMIC FIT, COMFORTABLE DESIGN-The trendy HP Gaming Headset has an ergonomically optimized fit. The padded headband, the soft and resistant ear pads and the individually adjustable microphone ensure maximum comfort. Even after intensive use for hours, the comfortable padding and headband sit comfortably firmly without hurting.\nLED LIGHTING, VOLUME CONTROL WHEEL- volume control button for microphone is designed conveniently for hand control. Glaring LED lights will light up the atmosphere while gaming. Deep Bass stereo sound field fully motivate your gaming passion.\nMULTI PLATFORM COMPATIBLITY- HP Gaming gaming headset Support PS4, PS4 Pro/Slim, New Xbox one, PSP, Nintendo 3DS, PC, Laptop, Computer, Tablet, iPad, Smartphones. (Note: additional adapter for xbox one not included)",
          "price_initial": 0,
          "pricing_count": 1,
          "reviews_count": 724,
          "sns_discounts": [],
          "developer_info": [],
          "price_shipping": 0,
          "product_details": {
            "asin": "B08JD3Z1BP",
            "material": "memory foam",
            "model_name": "HP H360GS",
            "unit_count": "1.0 Count",
            "item_weight": "1.32 pounds",
            "control_type": "Volume Control",
            "manufacturer": "hp",
            "cable_feature": "Retractable",
            "control_method": "Touch",
            "headphones_jack": "USB",
            "number_of_items": "1",
            "special_feature": "Microphone Included",
            "customer_reviews": "4.3 4.3 out of 5 stars 724 ratings 4.3 out of 5 stars",
            "best_sellers_rank": "#7,230 in Video Games (See Top 100 in Video Games) #407 in PC Game Headsets",
            "item_model_number": "HP H360",
            "product_dimensions": "9.1 x 9.1 x 9.1 inches",
            "included_components": "HEADPHONE",
            "date_first_available": "September 17, 2020",
            "age_range_description": "Adult",
            "connectivity_technology": "Wired",
            "specific_uses_for_product": "Movies and Gaming"
          },
          "featured_merchant": {
            "link": "/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=A1O935LXVIPNW3&asin=B08JD3Z1BP&ref_=dp_merchant_link&isAmazonFulfilled=1",
            "name": "Bsd Wholesale",
            "seller_id": "A1O935LXVIPNW3",
            "shipped_from": "Amazon",
            "is_amazon_fulfilled": true
          },
          "is_prime_eligible": true,
          "parse_status_code": 12005,
          "product_dimensions": "9.1 x 9.1 x 9.1 inches",
          "warranty_and_support": {
            "links": [
              {
                "url": "/gp/feature.html/ref=dp_warranty_request_3P?docId=1002406021",
                "title": "click here"
              }
            ],
            "description": "Product Warranty: For warranty information about this product, please click here"
          },
          "answered_questions_count": 0,
          "rating_stars_distribution": [
            { "rating": 5, "percentage": 66 },
            { "rating": 4, "percentage": 13 },
            { "rating": 3, "percentage": 8 },
            { "rating": 2, "percentage": 5 },
            { "rating": 1, "percentage": 8 }
          ],
          "frequently_bought_together": [
            { "asin": "B08JD3Z1BP" },
            { "asin": "B088TSR6YJ" },
            { "asin": "B09B9PCYSS" }
          ]
        },
        "errors": [],
        "status_code": 12000,
        "task_id": "7201134995845439489"
      },
      "status_code": 200,
      "url": "https://www.amazon.com/dp/B08JD3Z1BP/",
      "task_id": "7201134995845439489",
      "created_at": "2024-05-28 08:19:33",
      "updated_at": "2024-05-28 08:19:37"
    }
  ]
}
```

### Amazon product search listing scraping `amazon_search`
Retrieve Amazon search results by providing a query and a list of parameters.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_search`.|
|`query`      |`string`  | The search query. |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`category`   |`string`  | Product category ID. You can find it by opening a category and looking at the URL under the *node* parameter: `node=<category>`.|
|`merchant`   |`string`  | The merchant ID. You can find it by opening the *Sold by* link of the seller on a product page. The merchant ID appears in the URL under the *seller* parameter: `seller=<merchant>`.|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_search.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_search.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_search.py > amazon_search.py`|
| PHP      | [php/amazon_search.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_search.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_search.php > amazon_search.php`|
| Node.js  | [nodejs/amazon_search.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_search.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_search.js > amazon_search.js`|

### Amazon product scraping `amazon_product`
Retrieve Amazon listings by supplying Amazon product ID (ASIN). 

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_pricing`.|
|`query`      |`string`  | Amazon product ID (ASIN). |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`autoselect_variant`| `boolean`| To get accurate Buy Box or pricing data, set this parameter to `TRUE`. |
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_product.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_product.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_product.py > amazon_product.py`|
| PHP      | [php/amazon_product.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_product.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_product.php > amazon_product.php`|
| Node.js  | [nodejs/amazon_product.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_product.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_product.js > amazon_product.js`|

### Amazon product pricing scraping `amazon_pricing`
Retrieve Amazon pricing results by supplying Amazon product ID (ASIN). The response will list all sellers of the same product and their prices.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_pricing`.|
|`query`      |`string`  | Amazon product ID (ASIN). |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_pricing.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_pricing.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_pricing.py > amazon_pricing.py`|
| PHP      | [php/amazon_pricing.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_pricing.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_pricing.php > amazon_pricing.php`|
| Node.js  | [nodejs/amazon_pricing.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_pricing.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_pricing.js > amazon_pricing.js`|

### Amazon product reviews scraping `amazon_reviews`
Retrieve Amazon reviews by supplying Amazon product ID (ASIN).

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_reviews`.|
|`query`      |`string`  | Amazon product ID (ASIN). |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_reviews.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_reviews.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_reviews.py > amazon_reviews.py`|
| PHP      | [php/amazon_reviews.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_reviews.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_reviews.php > amazon_reviews.php`|
| Node.js  | [nodejs/amazon_reviews.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_reviews.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_reviews.js > amazon_reviews.js`|

### Amazon product questions & answers scraping `amazon_questions`
Retrieve Amazon questions and answers by supplying Amazon product ID (ASIN) using the query parameter.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_reviews`.|
|`query`      |`string`  | Amazon product ID (ASIN). |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_questions.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_questions.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_questions.py > amazon_questions.py`|
| PHP      | [php/amazon_questions.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_questions.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_questions.php > amazon_questions.php`|
| Node.js  | [nodejs/amazon_questions.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_questions.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_questions.js > amazon_questions.js`|

### Amazon product best sellers listing scraping `amazon_bestsellers`
Retrieve Amazon best-seller listings by supplying the category name to the query parameter.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_reviews`.|
|`query`      |`string`  | Category name. You can find it in the best sellers page URL located after `/zgbs/`. For example, the category name of `https://www.amazon.com/Best-Sellers-Sports-Collectibles/zgbs/sports-collectibles/` is `sports-collectibles`|
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`num_pages`  |`integer`  | Number of results to retrieve from each page.|
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: `desktop`, `desktop_chrome`, `desktop_edge`, `desktop_firefox`, `desktop_opera`, `desktop_safari`, `mobile`, `mobile_android`, `mobile_ios`, `tablet`, `tablet_android`, `tablet_ios`|
|`category`  |`string`  | Product category ID. You can find it by opening a category and looking at the URL under the *node* parameter: `node=<category>` |
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon_bestsellers.py](https://github.com/Smartproxy/Amazon-scraper/blob/main/python/amazon_bestsellers.py)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/python/amazon_bestsellers.py > amazon_bestsellers.py`|
| PHP      | [php/amazon_bestsellers.php](https://github.com/Smartproxy/Amazon-scraper/blob/main/php/amazon_bestsellers.php)    | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/php/amazon_bestsellers.php > amazon_bestsellers.php`|
| Node.js  | [nodejs/amazon_bestsellers.js](https://github.com/Smartproxy/Amazon-scraper/blob/main/nodejs/amazon_bestsellers.js)  | `curl https://raw.githubusercontent.com/Smartproxy/Amazon-scraper/main/nodejs/amazon_bestsellers.js > amazon_bestsellers.js`|

## Response codes
### HTTP response codes
An HTTP response status code indicates whether the request has been successfully completed.

| Code   | Response     | Description | Solution |
| :----- | :--------    | :---------- | :------- |
|**200** | OK           | The request was successful and server has returned a response.	 | Celebrate! |
|**204** | No content   | The job wasn't completed yet. | Wait a few seconds before trying again.     |
|**400** | Bad request  | Bad structure of the request. | Check your request again and ensure its format is correct. |
|**401** | Unauthorized | Incorrect login credentials or missing authorization. | Check your provided credentials for authorization. |
|**403** | Forbidden    | Your account doesn't have access to this resource. | Ensure that the target is supported and isn't on the [blocked target list](#https://smartproxy.com/faq/general/do-you-have-any-blocked-sites).|
|**404** | Not found    | Your target wasn't found. | Check if the URL you entered is correct. |
|**429** | Too many requests | Exceeded subscription rate limit. | Make sure you still have at least one request left. Wait a couple of minutes and try again. If you're encountering the error often – [chat with us](#https://direct.lc.chat/12092754/) to see if your rate limit can be increased. |
|**500** | Internal server error | Service unavailable, possibly due to internal issues. | Wait a couple of minutes and send another request. [Contact us](#https://direct.lc.chat/12092754/) for more information. |
|**524** | Timeout | Service unavailable due to internal issues or request timed out. | Wait a couple of minutes and send another request. [Contact us](#https://direct.lc.chat/12092754/) for more information. |

### Parsed result response codes
You can find these response codes in the JSON response as `parse_status_code` and `status_code`.
|Code        | Response        | Description | Solution |
|:-----------|:----------------|:------------|:---------|
| **12000**  |Success          | Server has replied and given the requested response.|Party!|
| **12002**  |Error            | Parsing has failed. |Try again in a few minutes, or check your request parameters.|
| **12003**  |Not supported    | Targeted page parsing isn't supported. |Only target parseable pages, or use parsing libraries to extract specific data from an HTML response. |
| **12004**  |Response not full| Some fields were not parsed and are missing. |Ensure that the target page contains the required information and try again.|
| **12005**  |Response not fully parsed| Some fields might not have been parsed and are returned unparsed. |Try again in a few minutes, or check your request parameters.|
| **12006**  |Error    | Unexpected error.|[Let us know]((#https://direct.lc.chat/12092754/)) the task ID, and we'll check what went wrong.|
| **12007**  |Unknown  | Couldn't determine whether the data was parsed correctly.|Check the response manually to see if it was parsed correctly.|
| **12008**  |Error    | Failed to parse all the data. |Check your request parameters, or if the information is present on the target page.|
| **12009**  |Error    | Target not found. |Make sure the parameters you passed are correct and supported.|

## License
All code is released under the [MIT License](https://github.com/Smartproxy/Smartproxy/blob/master/LICENSE).
