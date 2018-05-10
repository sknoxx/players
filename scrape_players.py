#! /usr/bin/env python

from selenium import webdriver	# pip install selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

url_list = ['https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(25%E2%80%9399_appearances)',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(1%E2%80%9324_appearances)']
players_from_webpage_list = []

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

driver = webdriver.Firefox()

for url in url_list:
    print url
    driver.get(url)
    driver.find_element_by_css_selector("th.headerSort:nth-child(5)").click()
    driver.find_element_by_css_selector("th.headerSort:nth-child(5)").click()

    table = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr')
    for row in table:
        cell = row.find_elements_by_tag_name("th")[0]
        player_object = {'appearances': unicode(row.find_elements_by_tag_name("td")[5].text)}

        first_string = unicode(cell.text.split(' ')[0])
        second_string = unicode(' '.join(cell.text.split(' ')[1:]))

        if second_string == '':
            player_object['first_name'] = unicode('Mr.')
            player_object['last_name'] = first_string
        else:
            player_object['first_name'] = first_string
            player_object['last_name'] = second_string
        print cell.text, player_object
        players_from_webpage_list.append(player_object)

    print len(players_from_webpage_list)
# driver.quit()

f = open('players.py', 'w')
f.writelines('#!/usr/bin/env python\n\nplayers_list = ')
f.writelines(json.dumps(players_from_webpage_list, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()

