import mechanize
import urllib2
from bs4 import BeautifulSoup

url = "http://events.berkeley.edu/?view=quick&timeframe=day&date=2013-09-28&tab=all_events"
br = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)
br.select_form(nr=0)
br.form['AllFields'] = 'food'
soup = BeautifulSoup(br.submit().read())

event_urls = list()
for div in soup.find_all("div", "event"):
	for h3 in div.find_all("h3"):
		for link in h3.find_all("a"):
		    full_link = "http://events.berkeley.edu/" + link.get('href')
		    event_urls.append(full_link)

page = urllib2.urlopen(event_urls[0])
soup = BeautifulSoup(page.read())

all_info = soup.find_all("div", "event")[0]

name_tag = all_info.find('h3')
name = name_tag.get_text()

various_info = name_tag.find_next_sibling("p").get_text()
info_list = various_info.split('|')
date = info_list[1]
time = info_list[2].replace('\n', ' ').replace('\t', ' ')
location = info_list[3]

sponsor = None
event_contact = None

location_label = all_info.find('label', text="Location: ")
if location_label:
	location = location_label.next_sibling.get_text()

sponsor_label = all_info.find('label', text="Sponsor: ")
sponsor = sponsor_label.next_sibling.get_text()

description = sponsor_label.parent.find_next_sibling("p").get_text()

event_contact_label = all_info.find('label', text="Event Contact: ")
if event_contact_label:
	event_contact = event_contact_label.next_sibling.next_sibling.get_text()


# various_info = all_info.find_all('p')[5].get_text()
# location = all_info.find_all('p')[6].get_text()
# sponsor = all_info.find_all('p')[7].get_text()
# description = all_info.find_all('p')[8].get_texkt()
# contact = all_info.find_all('p')[9].get_text()

# name = first_child.get_text()
# next_sibs = first_child.next_siblings

# various_info = next_sibs.next()
# location = next_sibs.next()
# sponsor = next_sibs.next()
# description = next_sibs.next()
# contact = next_sibs.next()

print name
print date
print time
print location
print sponsor
print description
print event_contact

a = all_info
n = all_info.find('h3')



