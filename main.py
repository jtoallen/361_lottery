# Author: Jason Allen
# Date: 10 January 2022
# Microservice: Text based UI Service that reads a number from a file and
#returns a set of lucky lottery numbers

import time


def user_interface():

    # while True:
        response = input("Enter 1 to generate your lucky numbers for Texas Powerball\n"
                         "or\n"
        "Enter 2 to generate your lucky numbers for Texas Mega Millions\n"
                         "or\n"
        "Enter 3 to exit program: \n")
        # response = int(response)
        # print(response)

        if response == '1':
            """
            1-write '1' in  lottoType.txt "
            2-sleep for 5 seconds
            3-read and output image service txt file
            """
            with open('lottoType.txt', 'w') as out:
                out.write("1")
            # time.sleep(2)
            # with open('prng-service.txt', 'r') as infile:
            #     num = infile.readline()
            #     num = num.strip()
            #
            # with open('image-service.txt', 'w') as outfile:
            #     outfile.write(str(num))

        elif response == '2':
            with open('lottoType.txt', 'w') as out:
                out.write("2")
            # time.sleep(2)
            # with open('prng-service.txt', 'r') as infile:
            #     num = infile.readline()
            #     num = num.strip()
            #
            # with open('image-service.txt', 'w') as outfile:
            # #     outfile.write(str(num))
            # with open('image-service.txt', 'r') as infile:
            #     num = infile.readline()
            #     condition_stripped = num.strip()
            #     print(condition_stripped)
        elif response == '3':
            return
        else:
            print("Invalid entry")


def main():
    # random_number()
    user_interface()


if __name__ == "__main__":
    main()
