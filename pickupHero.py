import numpy as np
import math

def pickup():
    total_spend = 0
    pickup_hero_level = 0
    step_full_hero = 30
    step_half_hero = 30

    # constant
    bonus_full_hero = 60
    bonus_helf_hero = bonus_full_hero / 2
    hero_spend = [["1⭐️", 60], ["2⭐️", 60], ["3⭐️", 120], ["4⭐️", 180], ["5⭐️", 240], ["1🔥", 120], ["2🔥", 120], ["3🔥", 180], ["4🔥", 180], ["5🔥", 240]]
    print(hero_spend)

    # probability
    prob_pickup_full_hero = 0.03333
    prob_other_full_hero = round(0.05 - prob_pickup_full_hero, 5)
    prob_pickup_10x_hero = 0.1
    prob_other_10x_hero = round(0.15 - prob_pickup_10x_hero, 5)
    prob_pickup_5x_hero = 0.13333
    prob_other_5x_hero = round(0.20 - prob_pickup_5x_hero, 5)
    prob_other = 0.60

    probs = np.array([prob_pickup_full_hero, prob_other_full_hero, prob_pickup_10x_hero, prob_other_10x_hero, prob_pickup_5x_hero, prob_other_5x_hero, prob_other])
    print(probs)

    return [np.sum(probs)]