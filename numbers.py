# Author: Jason Allen
# Date: 10 February 2022
#Assignment 6: Minimum Viable Product
"""Microservice: Pseudo Random Number Generator generates random numbers
based on which lotto game the user selects. Writes numbers to a text file
numbers.txt
"""

import os
import random
import time
import contextlib



def random_number():
    """Generates random integers and writes them to a file"""

    random_nums = []

    # while True:
    #     time.sleep(1)
    #     random_nums = []

    # with contextlib.suppress(FileNotFoundError):
    #     os.remove('numbers.txt')
    #     print('file removed')


    with open('lottoType.txt', 'r') as infile:
        condition = infile.readline()
        condition = condition.strip()
        # print(condition)  #testing code
        # with contextlib.suppress(FileNotFoundError):
        #     os.remove('numbers.txt')
        #     print('file removed')


        if condition == '1':
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 69))
                random_nums.append(random.randint(1,26))
                # print("Powerball", random_nums)
                outfile.write(str(random_nums))
                # time.sleep(1)
                # with contextlib.suppress(FileNotFoundError):
                #     os.remove('lottoType.txt')
                #     print('file removed')

        elif condition == '2':
            #conditions for Mega Millions
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 70))
                random_nums.append(random.randint(1,25))
                # print("Mega Millions", random_nums)
                outfile.write(str(random_nums))

        elif condition == '3':
            #conditions for Powerball with hockey game score
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 70))
                # random_nums.append(random.randint(1,25))
                with open('hockeyscore.txt', 'r') as inscore:
                    score = inscore.readline()
                    score = int(score.strip())
                    # print(score)
                    random_nums.append(score)
                # print("Powerball", random_nums)
                with open('numbers.txt', 'w') as outfile:
                    outfile.write(str(random_nums))



def main():
    random_number()


if __name__ == "__main__":
    main()
