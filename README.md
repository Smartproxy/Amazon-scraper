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
  - [Amazon product sellers scraping](#amazon-sellers-amazon_sellers)
  - [Amazon product best sellers listing scraping](#amazon-product-best-sellers-listing-scraping)
- [Response codes](#response-codes)
  - [HTTP response codes](#http-response-codes)
  - [Parsed result response codes](#parsed-result-response-codes)
- [Postman collection](#postman-collection)
- [License](#license)

## Introduction
Amazon is a treasure trove of eCommerce information due to its vast database of products, prices, reviews, and sales data. The platform offers valuable insights into the market and competitor strategies, making it an incredibly useful target to extract information from for those seeking to thrive in the digital marketplace.

Smartproxy offers an easy way to gather data from Amazon with the [eCommerce Scraping API](https://smartproxy.com/scraping/ecommerce). It targets various product areas, such as product listings, prices, reviews, and search results, then returns the information in an easy-to-read JSON format.

## Features
 - Ready-made targets to efficiently scrape the most popular Amazon pages
 - Retrieves results as formatted JSON data
 - Quick and simple authentication
 - Easy parameter configuration
 - User-friendly web interface with scheduling options

## Getting started
To begin using the eCommerce Scraping API, grab a plan that suits your needs from the [dashboard](https://dashboard.smartproxy.com/ecommerce-scraping-api/). From here, you have two options:
- **Scrape directly from the dashboard**. Navigate to the **Scrapers** tab, click **Create new project** and select a target from the available options. You can then use the web interface to build and make requests and return results with ease.
- **Get authentication credentials**. If you want to integrate the API into your code, go to the **API Authentication** tab. Here you'll find the automatically generated username, password, or the basic authentication token. You can use them as authentication methods inside your script. Not sure where to start? See the [examples below](#amazon-scraping-by-target).

## Targets
The eCommerce Scraping API targets the following Amazon categories and pages:
- Amazon listings (`amazon`)
- Amazon search results (`amazon_search`)
- Amazon product pages (`amazon_product`)
- Amazon product pricing (`amazon_pricing`)
- Amazon product reviews (`amazon_reviews`)
- Amazon product questions & answers (`amazon_questions`)
- Amazon sellers (`amazon_sellers`)
- Amazon bestsellers (`amazon_bestsellers`)

## Amazon scraping by target
Amazon can be targeted by using one of the target parameters listed in this section. Each target has a unique set of additional parameters that are used to define your search in more detail.

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|
| PHP      | [php/amazon.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|
| Node.js  | [nodejs/amazon.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|

#### Response Example
`?`

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`category`   |`string`  | Product category ID. You can find it by opening a category and looking at the URL, under the *node* parameter: `node=<category>`.|
|`merchant`   |`string`  | The merchant ID. You can find it by opening the *Sold by* link of the seller on a product page. The merchant ID appears in the URL under the *seller* parameter: `seller=<merchant>`.|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-search.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|
| PHP      | [php/amazon-search.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|
| Node.js  | [nodejs/amazon-search.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazon-search.py`|

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`autoselect_variant`| `boolean`| To get accurate Buy Box or pricing data, set this parameter to `TRUE`. |
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-product.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-product.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-product.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-pricing.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-pricing.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-pricing.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-reviews.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-reviews.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-reviews.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

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
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-questions.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-questions.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-questions.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

### Amazon sellers `amazon_sellers`
Retrieve Amazon seller page information by supplying a seller ID.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_reviews`.|
|`query`      |`string`  | 13-character seller ID. |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML.|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`geo`        |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-sellers.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-sellers.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-sellers.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

### Amazon product best sellers listing scraping
Retrieve Amazon best seller listings by supplying the category name to the query parameter.

#### Parameters
**Required**: `target`, `query`

| Parameter   | Type     | Description |
|:------------|:---------|:------------|
|`target`     |`string`  | Must be `amazon_reviews`.|
|`query`      |`string`  | Amazon product ID (ASIN). |
|`parse`      |`boolean` | Set it to `TRUE` if the result should be parsed in HTML|
|`domain`     |`string`  | The site domain determines the regional version of Amazon you'll see. For example, using `.co.uk` will show you results from the UK version of Amazon.|
|`page_from`  |`integer`  | The specific result page number to start scraping from. |
|`num_pages`  |`integer`  | Number of results to retrieve from each page.|
|`device_type`|`string`  | The type of device and browser the request should simulate. Possible values: <br>`desktop`<br>`desktop_chrome`<br>`desktop_edge`<br>`desktop_firefox`<br>`desktop_opera`<br>`desktop_safari`<br>`mobile`<br>`mobile_android`<br>`mobile_ios`<br>`tablet`<br>`tablet_android`<br>`tablet_ios`|
|`category`  |`string`  | Product category ID. You can find it by opening a category and looking at the URL, under the *node* parameter: `node=<category>` |
|`geo`       |`string`  | The geographical location that the result depends on. You can use an [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) country code (ex. `GB`) or a US ZIP code (ex. `99950`).|
|`session_id`|`string`  | Name your session to re-use the same IP for multiple requests for up to 10 minutes. |

#### Examples
| Language | File                             | Download  |
|:---------|:---------------------------------|:----------|
| Python   | [python/amazon-questions.py](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| PHP      | [php/amazon-questions.php](/url)    | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|
| Node.js  | [nodejs/amazon-questions.js](/url)  | `curl hhttps://raw.githubusercontent.com/Smartproxy/eCommerce-Scraping-API/main/python/amazonsearch.py > amazonsearch.py`|

## Response codes
### HTTP response codes
A HTTP response status code indicates whether the request has been successfully completed.

| Code   | Response     | Description | Solution |
| :----- | :--------    | :---------- | :------- |
|**200** | OK           | The request was successful and server has returned a response.	 | Celebrate! |
|**204** | No content   | The job wasn't completed yet. | Wait a few seconds before trying again.     |
|**400** | Bad request  | Bad structure of the request. | Check your request again and ensure it's format is correct. |
|**401** | Unauthorized | Incorrect login credentials or missing authorization. | Check your provided credentials for authorization. |
|**403** | Forbidden    | Your account doesn't have access to this resource. | Ensure that the target is supported and isn't on the [blocked target list](#https://smartproxy.com/faq/general/do-you-have-any-blocked-sites).|
|**404** | Not found    | Your target wasn't found. | Check if the URL you entered is correct. |
|**429** | Too many requests | Exceeded subscription rate limit. | Make sure you still have at least one request left. Wait a couple minutes and try again. If you're encountering the error often – [chat with us](#https://direct.lc.chat/12092754/) to see if your rate limit can be increased. |
|**500** | Internal server error | Service unavailable, possibly due to internal issues. | Wait a couple minutes and send another request. [Contact us](#https://direct.lc.chat/12092754/) for more information. |
|**524** | Timeout | Service unavailable due to internal issues or request timed out. | Wait a couple minutes and send another request. [Contact us](#https://direct.lc.chat/12092754/) for more information. |

### Parsed result response codes
You can find these response codes in the JSON response as `parse_status_code` and `status_code`.
|Code        | Response        | Description | Solution |
|:-----------|:----------------|:------------|:---------|
| **12000**  |Success          | Server has replied and given the requested response.|Party!|
| **12002**  |Error            | Parsing has failed. |Try again in a few minutes, or check your request parameters.|
| **12003**  |Not supported    | Targeted page parsing isn't supported. |Only target pages that are parseable, or use parsing libraries to extract specific data from an HTML response. |
| **12004**  |Response not full| Some fields were not parsed and are missing. |Ensure that the target page contains the required information and try again.|
| **12005**  |Response not fully parsed| Some fields might not have been parsed and are returned unparsed. |Try again in a few minutes, or check your request parameters.|
| **12006**  |Error    | Unexpected error.|[Let us know]((#https://direct.lc.chat/12092754/)) the task ID and we'll check what went wrong.|
| **12007**  |Unknown  | Couldn't determine whether the data was parsed correctly.|Check the response manually to see if it was parsed correctly.|
| **12008**  |Error    | Failed to parse all the data. |Check your request parameters, or if the information is present on the target page.|
| **12009**  |Error    | Target not found. |Make sure the parameters you passed are correct and supported.|

## Postman collection
-

## License
All code is released under the [MIT License](https://github.com/Smartproxy/Smartproxy/blob/master/LICENSE).
