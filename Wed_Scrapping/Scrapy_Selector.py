from scrapy import Selector

html = '''
<html>
<body>
<div class="hello datacamp">
<p>Hello World!</p>
</div>
<p>Enjoy DataCamp!</p>
</body>
</html>
'''
sel = Selector( text = html )

# Chain together xpath methods to select desired p element
sel.xpath( '//div' ).xpath( './span/p[3]')

sel.xpath('//div/span/p[3]')




# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text=html )

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )
