# -*- coding: utf-8 -*-

import time
from selenium import webdriver

from fixture.game import GameHelper
from fixture.wait import WaitHelper


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.game = GameHelper(self)
        self.base_url = base_url
        self.wait = WaitHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def get_current_url(self):
        wd = self.wd
        time.sleep(2)
        return str(wd.current_url)

    def open_home_page(self):
        wd = self.wd
        current_url = self.get_current_url()
        if not self.base_url == current_url:
            time.sleep(1)
            wd.get(self.base_url)
            wd.maximize_window()

    def destroy(self):
        self.wd.quit()
