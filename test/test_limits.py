# -*- coding: utf-8 -*-
# Created by NKruglov


def test_big_play(app):
    id_game = "div.bg_5x36plus"
    app.open_home_page()
    app.game.enter_in_game(id_game)
    app.game.fill_num_area()
    app.game.fill_num_second_area()
    limit_sum = app.game.limit_sum()
    assert 147840 == limit_sum
    pass
