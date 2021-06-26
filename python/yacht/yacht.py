"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    min_value = min(dice)
    max_value = max(dice)
    dice_grouped = Counter(dice)
    max_value_grouped = max(set(dice_grouped.values()))

    if category == YACHT and max_value_grouped >= 5:
        return 50
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * dice_grouped.get(category, 0)
    elif category == FULL_HOUSE and set(dice_grouped.values()) == {2, 3}:
        return sum(dice)
    elif category == FOUR_OF_A_KIND and max_value_grouped >= 4:
        return 4 * [k for k, v in dice_grouped.items() if v == max_value_grouped][0]
    elif (
        category == LITTLE_STRAIGHT
        and len(dice_grouped) == 5
        and min_value == 1
        and max_value == 5
    ):
        return 30
    elif (
        category == BIG_STRAIGHT
        and len(dice_grouped) == 5
        and min_value == 2
        and max_value == 6
    ):
        return 30
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
