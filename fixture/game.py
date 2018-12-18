# -*- coding: utf-8 -*-
import random
import time


class GameHelper:

    def __init__(self, app):
        self.app = app

    def enter_in_game(self, id_game):
        wd = self.app.wd
        time.sleep(1)
        element = id_game
        self.app.wait.present_css(element, t=60)
        wd.find_element_by_css_selector(element).click()
        pass

    def open_game_page(self, id_game):
        wd = self.app.wd
        self.app.wait.visible_css(element=id_game, t=60)
        wd.find_element_by_css_selector(id_game).click()

    def fill_num_area(self, r=36, n=11):
        wd = self.app.wd
        comb = list(range(1, r))
        random.shuffle(comb)
        for i in range(n):
            num = "//div/b[" + "".join(str(comb.pop())) + "]"
            wd.find_element_by_xpath(num).click()
            time.sleep(0.1)

    def fill_num_second_area(self, ):
        wd = self.app.wd
        buttons = wd.find_elements_by_css_selector("div.extra_zone.cleared > b.game_number")
        for i in range(4):
            buttons[i].click()

    def limit_sum(self):
        wd = self.app.wd
        time.sleep(1)
        text = wd.find_element_by_css_selector("tr.sum td.value ins").text
        mod_text = text.replace(" ", "")
        bill = int(mod_text)
        return bill
