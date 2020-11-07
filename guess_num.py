#!/usr/bin/env python
# coding=utf-8

import random
import itertools

filter_nums = []
filter_combinations = []

def update_filter_nums(num):
    if num not in filter_nums:
        filter_nums.append(num)

def update_filter_combinations(combination):
    if combination not in filter_combinations:
        filter_combinations.append(combination)

def get_input():
    print("input number: ", end='')
    user_input = input()
    if len(user_input) != 3 or '0' in user_input:
        print("Illegal input!")
        exit(0)
    return [int(user_input[0]), int(user_input[1]), int(user_input[2])]

def matches(user_input, distinct_values):
    return user_input == distinct_values

def other_numbers(distinct_values, range_begin=1, range_end=10):
    nums = []
    for i in range(range_begin, range_end):
        if i not in distinct_values and i not in filter_nums:
            nums.append(i)
    return nums

def permutation(distinct_values, count=3):
    p = []
    for t in itertools.permutations(distinct_values, count):
        if list(t) not in filter_combinations:
            p.append(list(t))
    # print("permutation: ", p)
    return p

def num_match_case(distinct_values, num):
    other_nums = itertools.combinations(other_numbers(distinct_values), 3 - num)
    nums = itertools.combinations(distinct_values, num)
    cases = []
    for on in other_nums:
        for n in nums:
            for case in permutation(list(n) + list(on)):
                if case not in filter_combinations:
                    cases.append(list(case))
    return cases

def both_zero_case(distinct_values):
    ons = other_numbers(distinct_values)
    return permutation(ons)

def guess(user_input, distinct_values, count):
    # print("filter nums: ", filter_nums)
    # print("filter combinations: ", filter_combinations)
    print("Computer guess: {}".format(distinct_values))
    if matches(user_input, distinct_values):
        print("The number computer guesses matches user input's!")
        print("Guess count: %d" % (count))
        exit(0)
    nA, nB = 0, 0
    for loc, num in enumerate(distinct_values):
        for uloc, unum in enumerate(user_input):
            if num == unum and loc == uloc:
                # according to the question, we shouldn't record the loc
                # otherwise we cheat
                nA += 1
                break
            if num == unum:
                nB += 1
                break
    print("nA: %d, nB: %d, count: %d" % (nA, nB, count))

    update_filter_combinations(distinct_values)

    if nA == 0 and nB == 0:
        for num in distinct_values:
            update_filter_nums(num)
        for new_distinct_values in both_zero_case(distinct_values):
            count += 1
            guess(user_input, new_distinct_values, count)
    elif nA == 2: # in this case, nB must be equal to zero
        for num in (other_numbers(distinct_values)):
            new_distinct_values = [num, distinct_values[1], distinct_values[2]]
            if new_distinct_values not in filter_combinations:
                count += 1
                guess(user_input, new_distinct_values, count)
        for num in (other_numbers(distinct_values)):
            new_distinct_values = [distinct_values[0], num, distinct_values[2]]
            if new_distinct_values not in filter_combinations:
                count += 1
                guess(user_input, new_distinct_values, count)
        for num in (other_numbers(distinct_values)):
            new_distinct_values = [distinct_values[0], distinct_values[1], num]
            if new_distinct_values not in filter_combinations:
                count += 1
                guess(user_input, new_distinct_values, count)
        # update_filter_nums(num)
    elif nA + nB == 3:
        for new_distinct_values in permutation(distinct_values):
            count += 1
            guess(user_input, new_distinct_values, count)
    elif nA + nB == 2:
        for new_distinct_values in (num_match_case(distinct_values, 2)):
            count += 1
            guess(user_input, new_distinct_values, count)
    elif nA + nB == 1:
        for new_distinct_values in (num_match_case(distinct_values, 1)):
            count += 1
            guess(user_input, new_distinct_values, count)

if __name__ == "__main__":
    user_input = get_input()
    distinct_values = random.sample(range(1, 10), 3)
    guess(user_input, distinct_values, 1)
