# ScrapeIt

It is a generalized scrapper which will scrap the content from any webpage on the basis of the CSS tags. This app will use **lxml**, **BeatifulSoap** and **CSS-Select** library.
This is a multiple page data retriever i.e. if we provide the base link then it is capable of retreiving data from all of the relevant links in the parent link.
By relevant link, it means all the links which are present as Next/Previous in the current parent URL.
Here is brief of lxml and BeatifulSoap:

#lxml
The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API, mostly compatible but superior to the well-known ElementTree API. The latest release works with all CPython versions from 2.6 to 3.6. 
For more details, [click here](http://lxml.de/)

#BeautifulSoap
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
For more details, [click here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#cssselect: CSS Selectors for Python
cssselect parses CSS3 Selectors and translate them to XPath 1.0 expressions. Such expressions can be used in lxml or another XPath engine to find the matching elements in an XML or HTML document.

This module used to live inside of lxml as lxml.cssselect before it was extracted as a stand-alone project.
For more details, [click here](https://vverma.net/scrape-the-web-using-css-selectors-in-python.html) Or [click here](https://cssselect.readthedocs.io/en/latest/)
