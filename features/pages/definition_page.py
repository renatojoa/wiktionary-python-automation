#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class DefinitionPage(BasePage):
    lblHeading = (By.ID, "firstHeading")
    #for testing
    listNoun = (By.XPATH, "//*[@id='mw-content-text']/div/ol")
    listNounSpan = (By.XPATH, "//*[@id='mw-content-text']/div/ol/li")
    #real
    listDefinition = (By.XPATH, "//*[@id='mw-content-text']//h3//following-sibling::ol")
    
    def navigate_page(self, url):
        self.open_url(url)

    def assertAddress(self, searchTxt):
        assert self.get_url() == ('https://en.wiktionary.org/wiki/' + searchTxt)

    def assertPage(self, searchTxt):
        assert self.get_title() == (searchTxt + ' - Wiktionary')

    def assertHeader(self, searchTxt):
        assert self.return_text(self.lblHeading) == searchTxt

    def onDefinitionPage(self, searchTxt):
        assert self.get_url() == ('https://en.wiktionary.org/wiki/' + searchTxt)
        assert self.get_title() == (searchTxt + ' - Wiktionary')
        assert self.return_text(self.lblHeading) == searchTxt

    def assertDefinition(self, expectedDefinition):
        myDefinitions = self.find_by_xpath(self.listDefinition)
        for li in myDefinitions:
            z = li.text
            if expectedDefinition in li.text:
                print(expectedDefinition)
                print(li.text)
                assert expectedDefinition in li.text
                break
        else :
            assert False
