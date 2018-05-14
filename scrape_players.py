#! /usr/bin/env python

from selenium import webdriver	# pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wik_page_locators import WikiPageLocators
import json

URL_LIST = ['https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(25%E2%80%9399_appearances)',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(1%E2%80%9324_appearances)']


def main():
    players_from_webpage_list = []
    driver = webdriver.Firefox()

    for url in URL_LIST:
        print url
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(WikiPageLocators.MAIN_PAGE_LINK))

        for _ in range(2):
            driver.find_element(*WikiPageLocators.TOTAL_COLUMN_HEADER).click()

        rows = driver.find_elements(*WikiPageLocators.ROWS_IN_TABLE)

        for row in rows:
            player_dict = {'appearances': unicode(row.find_elements(*WikiPageLocators.CELL_IN_ROW)[5].text)}

            cell = row.find_element(*WikiPageLocators.NAME_CELL_IN_ROW)

            first_name = unicode(cell.text.split(' ')[0])
            surname = unicode(' '.join(cell.text.split(' ')[1:]))

            if surname == '':
                player_dict['first_name'] = unicode('Mr.')
                player_dict['last_name'] = first_name
            else:
                player_dict['first_name'] = first_name
                player_dict['last_name'] = surname

            print cell.text, player_dict
            players_from_webpage_list.append(player_dict)

        print len(players_from_webpage_list)
    driver.quit()

    f = open('players.py', 'w')
    f.writelines('#!/usr/bin/env python\n\nplayers_list = ')
    f.writelines(json.dumps(players_from_webpage_list, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()


if __name__ == '__main__':
    main()
