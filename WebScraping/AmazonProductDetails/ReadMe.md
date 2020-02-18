# Amazon Web Scraper

## Scrape Product Details like Product Name and Price from amazon.in

```python

from selectorlib import Extractor
import requests 
import json 
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('url', help='Amazon Product Details URL')

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('TribitSpeaker.txt')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

# Download the page using requests
args = argparser.parse_args()
r = requests.get(args.url, headers=headers)

# Pass the HTML of the page and create 
data = e.extract(r.text)

# Print the data 
#print(json.dumps(data, indent=True))

for item, detail in data.items():
    print(item, ":", detail)

#price = int(str(data['price'])[2:-3].replace(",", ""))
#print(price)

#if price < 8000:
#    send email 
```

## Steps to run this script:

In command prompt, write the below code:
```python 
python amazon_scraper.py '<url_of_the_product>'
```
## Output:
![img](https://github.com/deepankarkotnala/PlayWithPython/blob/master/WebScraping/AmazonProductDetails/Images/amazon_scraper_output.JPG)
