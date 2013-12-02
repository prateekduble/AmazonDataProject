import bottlenose
import urllib2
from lxml import etree
import bs4.builder._lxml
from bs4 import BeautifulSoup
import subprocess
from subprocess import call
from subprocess import check_call

from sys import argv

# take filename as argument
script, index, keyword = argv

# Create amazon object with AWS keys
amazon = bottlenose.Amazon("AKIAJH5EETC4L6R6VFUQ", "NZLt8i3TL7HTvFX4321HHKZE0yINDHmvTjAfDIw4", "httpwwwpdspro-20")
outfile = "%s_%s.txt" % (index,keyword)
print outfile
# Call ItemSearch to search in Books category, sort by salesrank, with best sellers keywords and get Reviews links
itemsearch = "amazon.ItemSearch(SearchIndex=\"%s\", Sort=\"salesrank\", Keywords=\"%s\", ItemPage=1, ResponseGroup=\"Reviews\")" % (index,keyword)
response = eval(itemsearch)

# Create a beautiful soup  to parse xml
soup = BeautifulSoup(response, "xml")
csv = open("reviews.txt", "w")
for asin in soup.find_all("ASIN",recursive=True):
    asinid = asin.text
    url = '''http://www.amazon.com/product-reviews/%s'''% asinid
    print url
    call(["perl", "downloadAmazonReviews.pl", "com", asinid])
    pathtoreview = "amazonreviews/com/" + asinid + "/*"
    command = "perl extractAmazonReviews.pl %s %s" % (outfile,pathtoreview)
    print command
    code = check_call([command], shell=True)
    print code
