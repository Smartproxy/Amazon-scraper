import requests
  
url = "https://scraper-api.smartproxy.com/v2/scrape"
  
payload = {
      "target": "amazon",
      "url": "https://www.amazon.com/dp/B08JD3Z1BP/",
      "parse": True,
}
  
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic [your basic authentication token]"
}
  
response = requests.post(url, json=payload, headers=headers)
  
print(response.text)
