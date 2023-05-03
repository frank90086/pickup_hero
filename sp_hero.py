import numpy as np
import math

def sp():
    total_spend = 0
    fragments = 0
    sp_hero_level = 0
    step_full_hero = 50

    # constant
    bonus_full_hero = 80
    hero_spend = np.array([["0 (0_Fire)", 80], ["1 (1_Fire)", 160], ["2 (2_Fire)", 160], ["3 (3_Fire)", 240], ["4 (4_Fire)", 240], ["5 (5_Fire)", 320]], dtype=object)

    # probability
    prob_sp_full_hero = 0.03
    prob_sp_10x_hero = 0.0795
    prob_sp_5x_hero = 0.1998
    prob_other = 1 - prob_sp_full_hero - prob_sp_10x_hero - prob_sp_5x_hero

    probs = np.array([prob_sp_full_hero, prob_sp_10x_hero, prob_sp_5x_hero, prob_other])

    result = []
    while(fragments < np.sum(hero_spend[:, 1])):
        total_spend += 1
        step_full_hero -= 1

        # get full hero bonus
        if(step_full_hero == 0):
            pick_out = bonus_full_hero
        else:
            pick_out = np.random.choice([80, 10, 5, 0], p = probs)

        # reset if pick full hero
        if(pick_out == 80):
            step_full_hero = 50

        fragments += pick_out

        while(fragments >= np.sum(hero_spend[:sp_hero_level+1, 1]) and sp_hero_level < 6):
            result.append([hero_spend[sp_hero_level, 0], total_spend, fragments])
            sp_hero_level += 1

    return np.array(result, dtype=object)

def sp_specific_wrapper(arg):
    return sp_specific(*arg)

def sp_specific(current, current_fragments, target):
    total_spend = 0
    fragments = 0
    sp_hero_level = 0
    step_full_hero = 50

    # constant
    bonus_full_hero = 80
    hero_spend = np.array([["0 (0_Fire)", 80], ["1 (1_Fire)", 160], ["2 (2_Fire)", 160], ["3 (3_Fire)", 240], ["4 (4_Fire)", 240], ["5 (5_Fire)", 320]], dtype=object)

    # probability
    prob_sp_full_hero = 0.03
    prob_sp_10x_hero = 0.0795
    prob_sp_5x_hero = 0.1998
    prob_other = 1 - prob_sp_full_hero - prob_sp_10x_hero - prob_sp_5x_hero

    # setup
    sp_hero_level = current
    fragments = np.sum(hero_spend[:sp_hero_level+1, 1]) + current_fragments

    probs = np.array([prob_sp_full_hero, prob_sp_10x_hero, prob_sp_5x_hero, prob_other])

    result = []
    while(fragments < np.sum(hero_spend[:target + 1, 1])):
        total_spend += 1
        step_full_hero -= 1

        # get full hero bonus
        if(step_full_hero == 0):
            pick_out = bonus_full_hero
        else:
            pick_out = np.random.choice([80, 10, 5, 0], p = probs)

        # reset if pick full hero
        if(pick_out == 80):
            step_full_hero = 50

        fragments += pick_out

        while(fragments >= np.sum(hero_spend[:sp_hero_level+1, 1]) and sp_hero_level < 6):
            result.append([hero_spend[sp_hero_level, 0], total_spend, fragments])
            sp_hero_level += 1

    return np.array(result, dtype=object)