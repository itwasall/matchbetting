#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cli_ui import info, reset, bold, blue, yellow, red

def calc_bet(bf, bfo, l, lo):
    BET_LOSE = 0
    BET_WIN = (bf * bfo) - bf
    LAY_LIABILITY = l * (lo - 1)
    LAY_LOSE = LAY_LIABILITY * -1
    LAY_WIN = l
    
    EVENT_WIN = "{0:.2f}".format(BET_WIN - LAY_LIABILITY)
    EVENT_LOSE = "{0:.2f}".format(LAY_WIN - BET_LOSE)
    print(EVENT_WIN, EVENT_LOSE)

    if float(EVENT_WIN) > 0:
        info("If event win:", bold, yellow, f"£{EVENT_WIN}")
    else:
        info("If event win:", bold, red, f"£{EVENT_WIN}")
    if float(EVENT_LOSE) > 0:
        info("If event lose:", bold, yellow, f"£{EVENT_LOSE}")
    else:
        info("If event lose:", bold, red, f"£{EVENT_LOSE}")

calc_bet(5, 10, 4.97, 9.8)
