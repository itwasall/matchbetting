#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cli_ui import info, reset, bold, blue, yellow, red
from math import log2 

def calc_bet(back_bet_amt, back_bet_odds, lay_bet_amt, lay_bet_odds, is_free_bet: bool = True):
    if is_free_bet:
        BET_LOSE = 0
        BET_WIN = float((back_bet_amt * back_bet_odds) - back_bet_amt)
    else:
        BET_LOSE = back_bet_amt
        BET_WIN = float(back_bet_amt * back_bet_odds)
    LAY_LIABILITY = "{0:.2f}".format(lay_bet_amt * (lay_bet_odds - 1))
    LAY_WIN = lay_bet_amt
    EVENT_WIN = "{0:.2f}".format(BET_WIN - float(LAY_LIABILITY))
    EVENT_LOSE = "{0:.2f}".format(LAY_WIN - BET_LOSE)

    print(f"BACK BET: {back_bet_amt}@{back_bet_odds}\nLAY BET: {lay_bet_amt}@{lay_bet_odds} ({LAY_LIABILITY} liability)")
    if is_free_bet:
        info(blue, bold, "FREE BET")
    if float(EVENT_WIN) > 0:
        info("If event win:", bold, yellow, f"£{EVENT_WIN}")
    else:
        info("If event win:", bold, red, f"£{EVENT_WIN}")
    if float(EVENT_LOSE) > 0:
        info("If event lose:", bold, yellow, f"£{EVENT_LOSE}")
    else:
        info("If event lose:", bold, red, f"£{EVENT_LOSE}")
    info("PROFIT DIFFERENCE:", "{0:.2f}".format(float(EVENT_WIN) - float(EVENT_LOSE)))

# calc_bet(5, 10, 4.97, 11.5)
calc_bet(5, 10, 4.47, 11.5)
calc_bet(5, 10, 3.97, 11.5)
calc_bet(5, 10, 3.91, 11.5)
# calc_bet(5, 10, 2.97, 11.5)

def lay_stake_calculator(back_stake, back_odds, lay_odds, is_free_bet: bool = True):
    if is_free_bet:
        BACK_WIN = (back_stake * back_odds) - back_stake
        BACK_LOSE = 0
    else:
        BACK_WIN = back_stake * back_odds
        BACK_LOSE = back_stake
    BACK_LAY_ODDS_RATIO = back_odds / lay_odds
    LAY_STAKE = (BACK_LAY_ODDS_RATIO / log2(BACK_LAY_ODDS_RATIO)) * back_stake
    print(BACK_WIN, BACK_LOSE, LAY_STAKE)
    return LAY_STAKE


lay_stake_calculator(5, 10, 11.5)
calc_bet(5, 5.5, lay_stake_calculator(5, 5.5, 6), 6)
calc_bet(5, 1.8, lay_stake_calculator(5, 1.8, 2.4), 2.4)
# When [back_odds/lay_odds] are @ 90%, the lay stake calculated gives the least variance in winnings when back odds are 10 and lay odds are 11.5