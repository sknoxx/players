#! /usr/bin/env python

from selenium.webdriver.common.by import By


class WikiPageLocators(object):
    MAIN_PAGE_LINK = (By.LINK_TEXT, 'Main page')
    TOTAL_COLUMN_HEADER = (By.CSS_SELECTOR, 'th.headerSort:nth-child(7)')
    ROWS_IN_TABLE = (By.XPATH, '//*[@id="mw-content-text"]/div/table[2]/tbody/tr')
    NAME_CELL_IN_ROW = (By.TAG_NAME, 'th')
    CELL_IN_ROW = (By.TAG_NAME, 'td')