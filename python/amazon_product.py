import requests
  
url = "https://scraper-api.smartproxy.com/v2/scrape"
  
payload = {
      "target": "amazon_product",
      "query": "B09H74FXNW",
      "parse": True,
      "autoselect_variant": False
}
  
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic [your basic authentication token]"
}
  
response = requests.post(url, json=payload, headers=headers)
  
print(response.text)