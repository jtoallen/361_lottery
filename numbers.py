# Author: Jason Allen
# Date: 14 January 2022
# Microservice: Pseudo Random Number Generator generates random number
# and writes numbers to a file

import random
import time


def random_number():
    """Generates a random integer between 0 - 9 and writes them to a file"""

    random_nums = []
    # for i in range(6):
    #     random_nums.append(random.randint(1, 70))

    # while True:
    #     time.sleep(1)

    with open('lottoType.txt', 'r') as infile:
        condition = infile.readline()
        condition = condition.strip()
        print(condition)
        if condition == '1':
            #conditions for Powerball
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 69))
                random_nums.append(random.randint(1,26))
                print("Powerball", random_nums)
                outfile.write(str(random_nums))
        else:
            #conditions for Mega Millions
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 70))
                random_nums.append(random.randint(1,25))
                print("Mega Millions", random_nums)
                outfile.write(str(random_nums))
    # with open('prng-service.txt', 'w') as update_outfile:
    #     update_outfile.write("")

    # random_nums = [random.randint(0, 9)]
    # print(random_nums)
    #
    # with open('prng-service.txt', 'w') as outfile:
    #     for num in random_nums:
    #         outfile.write(str(num))

    # random_nums = []
    # for i in range(20):
    #     random_nums.append(random.randint(0, 9))
    # # print(random_nums)
    #
    # with open('prng-service.txt', 'w') as outfile:
    #     for num in random_nums:
    #         outfile.write(str(num) + ',')
    #         print(num)


def main():
    random_number()


if __name__ == "__main__":
    main()

