# Author: Jason Allen
# Date: 14 January 2022
# Microservice: Pseudo Random Number Generator generates random number
# and writes numbers to a file

import random
import time


def random_number():
    """Generates a random integer between 0 - 9 and writes them to a file"""

    random_nums = random.randint(1, 20)

    # while True:
    #     time.sleep(1)

    with open('prng-service.txt', 'r') as infile:
        condition = infile.readline()
        condition = condition.strip()
        print(condition)
        if condition == 'run':
            with open('image-service.txt', 'w') as outfile:
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

