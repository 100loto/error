# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class WaitHelper:

    def __init__(self, app):
        self.app = app

    def present_css(self, element, t):
        for i in range(t):
            try:
                if self.is_element_present(By.CSS_SELECTOR, element):
                    break
            except:
                pass
            time.sleep(1)
        else:
            pass

    def visible_css(self, element, t):
        wd = self.app.wd
        for i in range(t):
            try:
                if wd.find_element_by_css_selector(element).is_displayed():
                    break
            except:
                pass
            time.sleep(1)
        else:
            pass

    def is_element_present(self, how, what):
        wd = self.app.wd
        try:
            wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

