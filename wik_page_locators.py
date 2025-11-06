#! /usr/bin/env python

from selenium.webdriver.common.by import By


class WikiPageLocators(object):
    MAIN_PAGE_LINK = (By.LINK_TEXT, 'Main page')
    LIST_OF_PLAYERS_LINK = (By.CSS_SELECTOR, 'a[href="#List_of_players"]')
    TOTAL_COLUMN_HEADER = (By.XPATH, "//th[contains(., 'Total')]")
    ROWS_IN_TABLE = (By.XPATH, '//*[@id="mw-content-text"]/div/table[2]/tbody/tr')
    NAME_CELL_IN_ROW = (By.TAG_NAME, 'th')
    CELL_IN_ROW = (By.TAG_NAME, 'td')