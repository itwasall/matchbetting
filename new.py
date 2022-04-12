#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from free_bet_calc import calc_bet

def bet_lose(stake, odds, is_free:bool=True):
    if is_free:
        return 0
    return stake

def bet_win(stake, odds, is_free:bool=True):
    if is_free:
        # Stake not returned
        return stake * (odds - 1)
    return stake * odds

def bet_profit(is_win: bool, outcome_amount, stake):
    if is_win:
        return outcome_amount - stake
    return -stake

def lay_liability(stake, odds):
    return stake * (odds - 1)

def lay_win(stake, odds):
    return stake

def lay_profit(is_win: bool, outcome_amount, stake):
    if is_win:
        return outcome_amount - stake
    return -outcome_amount

def each_way_back_bet(stake, odds, place_ratio):
    back_bet = {
        'E/W Stake': stake,
        'Total Stake': stake * 2,
        'Odds': odds,
        'Place Odds': round(odds * place_ratio, 2),
        'First Place Win': bet_win(stake, odds*(1-place_ratio), False) + bet_win(stake, odds*place_ratio, False),
        'Other Place Win': bet_win(stake, odds*place_ratio, False)
    }
    return back_bet

def each_way_lay_bet(win_stake, win_odds, place_stake, place_odds):
    lay_liability = {
        'Win': round(win_stake * win_odds, 2),
        'Place': round(place_stake * (place_odds - 1), 2),
        'Total': round((win_stake * (win_odds - 1)) + (place_stake * (place_odds - 1)),2)
    }
    lay_bet = {
        'Lay Win Stake': win_stake,
        'Lay Win Odds': win_odds,
        'Lay Place Stake': place_stake,
        'Lay Place Odds': place_odds,
        'Liability': lay_liability,
        'Lay Win Win': round(win_stake, 2),
        'Lay Place Win': round(place_stake, 2)
    }
    return lay_bet

back_bet = each_way_back_bet(10, 12, 0.2)
lay_bet = each_way_lay_bet(8.43, 14.5, 8.1, 4)

print(lay_bet)
def each_way_profit_calc(back_bet, lay_bet):
    back_ew_stake = back_bet['E/W Stake']
    back_first = back_bet['First Place Win']
    back_place = back_bet['Other Place Win']
    lay_first_liability = lay_bet['Liability']['Win']
    lay_place_liability = lay_bet['Liability']['Place']
    lay_first_win = lay_bet['Lay Win Win']
    lay_place_win = lay_bet['Lay Place Win']

    first_place = round(back_first + back_place - lay_first_liability - lay_place_liability, 2)
    normal_place = round(back_place + lay_first_win - back_ew_stake - lay_place_liability, 2)
    extra_place = round(back_place + lay_first_win + lay_place_win - back_ew_stake, 2)
    no_place = round(lay_first_win + lay_place_win - back_ew_stake * 2, 2)

    print(f"If 1st: {first_place}\nIf Regular Place: {normal_place}\nIf Extra Place: {extra_place}\nIf No Place: {no_place}")


each_way_profit_calc(back_bet, lay_bet)
