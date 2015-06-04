# scrapper to pull location of each listed item
from lxml import html
import requests
from bs4 import BeautifulSoup 
from urllib2 import urlopen

url = 'http://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1311.R2.TR10.TRC0.A0.H0.Xmini+display+.TRS0&_nkw=mini+display+port+to+hdmi&_sacat=0'

html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
# print soup
mydiv = soup.find("ul", {'id' :'ListViewInner'})
# print mydiv

elements = mydiv.findAll("li",{'class':'sresult lvresult clearfix li shic'})
# elements = elements[:1]
for x in elements:
	link =  x.find('a',{'class':'img imgWr2'})
	print link['href']
	page = BeautifulSoup(urlopen(link['href']).read(),"lxml")
	loc = page.find('div',{"class":"iti-eu-bld-gry "})
	print loc.text


# print boccat
