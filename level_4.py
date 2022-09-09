from webbot import Browser
from urllib.request import urlopen
import re

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
pattern = re.compile("and the next nothing is (\d+)")

# web = Browser()
# web.go_to(link % num)
# while True:
#     tmp = web.get_page_source()
#     match = pattern.search(tmp)
#     new = match.group(1)
#     if match == None:
#         break
#     web.go_to(link + new)

while True:
    content = urlopen(link % num).read().decode('utf-8')
    print(content)

    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)
