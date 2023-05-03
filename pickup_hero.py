import numpy as np
import math

def pickup():
    total_spend = 0
    fragments = 0
    pickup_hero_level = 0
    step_full_hero = 30
    step_half_hero = 30

    # constant
    bonus_full_hero = 60
    bonus_helf_hero = bonus_full_hero / 2
    hero_spend = np.array([["0 (1_Start)", 60], ["1 (2_Start)", 60], ["2 (3_Start)", 120], ["3 (4_Start)", 180], ["4 (5_Start)", 240], ["5 (1_Fire)", 120], ["6 (2_Fire)", 120], ["7 (3_Fire)", 180], ["8 (4_Fire)", 180], ["9 (5_Fire)", 240]], dtype=object)

    # probability
    prob_pickup_full_hero = 0.03333
    prob_other_full_hero = round(0.05 - prob_pickup_full_hero, 5)
    prob_pickup_10x_hero = 0.1
    prob_other_10x_hero = round(0.15 - prob_pickup_10x_hero, 5)
    prob_pickup_5x_hero = 0.13333
    prob_other_5x_hero = round(0.20 - prob_pickup_5x_hero, 5)
    prob_other = 0.60

    probs = np.array([prob_pickup_full_hero, prob_other_full_hero, prob_pickup_10x_hero, prob_other_10x_hero, prob_pickup_5x_hero, prob_other_5x_hero, prob_other])

    result = []
    while(fragments < np.sum(hero_spend[:, 1])):
        total_spend += 1
        step_full_hero -= 1
        step_half_hero -= 1

        # get full hero bonus
        if(step_full_hero == 0):
            pick_out = bonus_full_hero
        else:
            pick_out = np.random.choice([60, 0, 10, 0, 5, 0, 0], p = probs)

        # reset if pick full hero
        if(pick_out == 60):
            step_full_hero = 30

        # get half hero bonus and reset
        if(step_half_hero == 0):
            fragments += bonus_helf_hero
            step_half_hero = 30

        fragments += pick_out

        while(fragments >= np.sum(hero_spend[:pickup_hero_level+1, 1]) and pickup_hero_level < 10):
            result.append([hero_spend[pickup_hero_level, 0], total_spend, fragments])
            pickup_hero_level += 1

    return np.array(result, dtype=object)