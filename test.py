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
script, index, keyword, sort = argv

# Create amazon object with AWS keys
amazon = bottlenose.Amazon("AKIAJH5EETC4L6R6VFUQ", "NZLt8i3TL7HTvFX4321HHKZE0yINDHmvTjAfDIw4", "httpwwwpdspro-20")
outfile = "%s_%s.txt" % (index,keyword)
#print outfile

# Call ItemSearch to search in Books category, sort by salesrank, with best sellers keywords and get Reviews links
for x in range(1, 3):
    itemsearch = "amazon.ItemSearch(SearchIndex=\"%s\", Sort=\"%s\", Keywords=\"%s\", ItemPage=%d, ResponseGroup=\"Reviews\")" % (index,sort,keyword,x)
    response = eval(itemsearch)
    #print response

    # Create a beautiful soup  to parse xml
    soup = BeautifulSoup(response, "xml")
    tempfile = "temp.txt"
    for asin in soup.find_all("ASIN",recursive=True):
        asinid = asin.text
        url = '''http://www.amazon.com/product-reviews/%s'''% asinid
        #print url
        call(["perl", "downloadAmazonReviews.pl", "com", asinid])
        pathtoreview = "amazonreviews/com/" + asinid + "/*"
        command = "perl extractAmazonReviews.pl %s %s" % (tempfile,pathtoreview)
        code = check_call([command], shell=True)
    with open(outfile, 'a') as outputfile:
        with open(tempfile) as infile:
            outputfile.write(infile.read())

