#! /usr/bin/env python

from selenium import webdriver	# pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wik_page_locators import WikiPageLocators
import json
import csv

URL_LIST = ['https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(25%E2%80%9399_appearances)',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._players_(1%E2%80%9324_appearances)',
            'https://en.wikipedia.org/wiki/List_of_Manchester_United_W.F.C._players']


def main():
    players_from_webpage_list = []
    # driver = webdriver.Chrome('../chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    for url in URL_LIST:
        print(url)
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(WikiPageLocators.LIST_OF_PLAYERS_LINK))
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(WikiPageLocators.TOTAL_COLUMN_HEADER))

        for _ in range(2):
            driver.find_element(*WikiPageLocators.TOTAL_COLUMN_HEADER).click()

        rows = driver.find_elements(*WikiPageLocators.ROWS_IN_TABLE)

        for row in rows:
            player_dict = {
                'appearances': row.find_elements(*WikiPageLocators.CELL_IN_ROW)[5].text,
                'goals': row.find_elements(*WikiPageLocators.CELL_IN_ROW)[6].text,
                'nationality': row.find_elements(*WikiPageLocators.CELL_IN_ROW)[0].text.strip()}

            cell = row.find_element(*WikiPageLocators.NAME_CELL_IN_ROW)

            first_name = cell.text.split(' ')[0]
            surname = ' '.join(cell.text.split(' ')[1:])

            if surname == '':
                player_dict['first_name'] = 'Mr.'
                player_dict['last_name'] = first_name
            else:
                player_dict['first_name'] = first_name
                player_dict['last_name'] = surname

            # print(cell.text, player_dict)
            full_name = f"{player_dict['first_name']} {player_dict['last_name']}"

            print(f"| {full_name:<25} | Country: {player_dict['nationality']:<20.20} | "
                  f"Apps: {player_dict['appearances']:>6} | Goals: {player_dict['goals']:>5} |")
            players_from_webpage_list.append(player_dict)

        print(len(players_from_webpage_list))
    driver.quit()

    f = open('players.py', 'w')
    f.writelines('#!/usr/bin/env python\n\nplayers_list = ')
    f.writelines(json.dumps(players_from_webpage_list, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()

    with open('players.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['first_name', 'last_name', 'nationality', 'appearances', 'goals']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerows(players_from_webpage_list)


if __name__ == '__main__':
    main()
