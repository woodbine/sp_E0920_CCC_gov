# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

# Set up variables
entity_id = "E0920_CCC_gov"
url = "http://www.cumbria.gov.uk/managingyourcouncil/councilspend500/default.asp"

# Set up functions
def convert_mth_strings(mth_string):
    month_numbers = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
    # loop through the months in our dictionary
    for k, v in month_numbers.items():
        #  then replace the word with the number
        mth_string = mth_string.replace(k, v)
    return mth_string

# pull down the content from the webpage
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

# find all entries with the required class
block = soup.find('ul',{'class':'navsublist'})
yrPageLinks = block.findAll('li')

for yrPageLink in yrPageLinks:
    yrPageUrl = 'http://www.cumbria.gov.uk' + yrPageLink.a['href']
    html2 = urllib2.urlopen(yrPageUrl)
    soup2 = BeautifulSoup(html2)
    subBlock = soup2.find('ul', {'class':'navsublist'})
    mthPageLinks = subBlock.findAll('li')

    for mthPageLink in mthPageLinks:
        mthPageUrl = 'http://www.cumbria.gov.uk' + mthPageLink.a['href']
        html3 = urllib2.urlopen(mthPageUrl)
        soup3 = BeautifulSoup(html2)
        print soup3
        
        '''
        for filePageLink in filePageLinks:
            
            if '.csv' in fileUrl:
                # create the right strings for the new filename
                title = fileBlock.a.contents[0]
                title = title.upper()
                csvYr = title.split(' ')[-1]
                csvMth = title.split(' ')[-2][:3]
                csvMth = convert_mth_strings(csvMth);
                filename = entity_id + "_" + csvYr + "_" + csvMth
                todays_date = str(datetime.now())
                scraperwiki.sqlite.save(unique_keys=['l'], data={"l": fileUrl, "f": filename, "d": todays_date})

            print filename
        '''
