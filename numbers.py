# Author: Jason Allen
# Date: 18 March 2022
#Random Number Generator
"""Microservice: Pseudo Random Number Generator generates random numbers
based on which lotto game the user selects. Writes numbers to a text file
"""

import os
import random


def powerball_random_nums(random_nums):
    with open('numbers.txt', 'w') as outfile:
        for i in range(5):
            random_nums.append(random.randint(1, 69))
        random_nums.append(random.randint(1, 26))
        outfile.write(str(random_nums))


def mega_millions_random_nums(random_nums):
    with open('numbers.txt', 'w') as outfile:
        for i in range(5):
            random_nums.append(random.randint(1, 70))
        random_nums.append(random.randint(1, 25))
        outfile.write(str(random_nums))


def hockey_score_random_nums(random_nums):
    with open('numbers.txt', 'w') as outfile:
        for i in range(5):
            random_nums.append(random.randint(1, 70))
        with open('hockeyscore.txt', 'r') as inscore:
            score = inscore.readline()
            score = int(score.strip())
            random_nums.append(score)
        with open('numbers.txt', 'w') as hockey_out:
            hockey_out.write(str(random_nums))


def random_number():
    """Generates random integers and writes them to a file"""
    random_nums = []

    with open('lottoType.txt', 'r') as infile:
        condition = infile.readline()
        condition = condition.strip()
        if condition == '1':
            powerball_random_nums(random_nums)
        elif condition == '2':
            mega_millions_random_nums(random_nums)
        elif condition == '3':
            hockey_score_random_nums(random_nums)


def main():
    random_number()


if __name__ == "__main__":
    main()
