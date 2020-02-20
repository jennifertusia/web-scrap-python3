from lxml import etree

tree = etree.parse("fundamentals/src/web_page.html")
html = tree.getroot()
print(html)
title_element = html.cssselect("title")[0]
print(title_element.text)


para_element = html.cssselect("p")[0]
print(para_element.text)

list_items = html.cssselect("li")
for li in list_items:
    a = li.cssselect('a')
    if len(a) == 0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")