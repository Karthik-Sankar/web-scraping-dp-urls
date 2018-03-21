# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:54:03 2018

@author: sankarth
"""

import requests as req
import re
from lxml import html
import pandas as pd
import time
dataset = pd.read_csv('sku.csv')
skus = dataset.iloc[:,0].values
file = open('urls.csv','a')
for i in range(len(skus)):
    response = req.get('http://www.canadacomputers.com/search_results.php?search_in=&keywords='+skus[i+1], 
                       proxies={"http":"http://159.203.20.231:3128"})
    tree = html.fromstring(str(response.content))
    url = str(tree.xpath('//div[@id="desc1"]//p/@onclick'))
    fin_url = re.search(r"(http.*)\\\\';",url,re.M|re.I)
    file.write(str(fin_url.group(1))+'\n')
file.close()
