import requests
from lxml import html

resp = requests.get(url="http://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimalDetails2.aspx?id=41148500&css=", headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})

tree = html.fromstring(html=resp.text)

description = tree.xpath("//span[contains(@id,'lbDescription')]/text()")
print(description)
