html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

print "--"*20
print(soup.prettify())

print "--"*20
print soup.title
# <title>The Dormouse's story</title>

print "--"*20
print soup.title.name
# u'title'

print "--"*20
print soup.title.string
# u'The Dormouse's story'

print "--"*20
print soup.title.parent.name
# u'head'

print "--"*20
print soup.p
# <p class="title"><b>The Dormouse's story</b></p>

print "--"*20
print soup.p['class']
# u'title'

print "--"*20
print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print "--"*20
print soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print "--"*20
print soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


for link in soup.find_all('a'):
    print "--"*20
    print link.get('href')

    # for i in link.get('href'):
        # print i
    # print type(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

print "--"*20
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...


