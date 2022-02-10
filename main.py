# Author: Jason Allen
# Date: 10 January 2022
# Microservice: Text based UI Service that reads a number from a file and
#returns a set of lucky lottery numbers

import time


def user_interface():

    while True:
        response = input("Please enter 2 to generate your lucky numbers or"
                         " 2 to exit program: \n")
        # response = int(response)
        # print(response)

        if response == '1':
            """
            1-write "run in image service "
            2-sleep for 5 seconds
            3-read and output image service txt file
            """
            with open('prng-service.txt', 'w') as out:
                out.write("run")
            # time.sleep(2)
            # with open('prng-service.txt', 'r') as infile:
            #     num = infile.readline()
            #     num = num.strip()
            #
            # with open('image-service.txt', 'w') as outfile:
            #     outfile.write(str(num))

            with open('image-service.txt', 'r') as infile:
                num = infile.readline()
                condition_stripped = num.strip()
                print(condition_stripped)
        elif response == '2':
            return
        else:
            print("Invalid entry")


def main():
    # random_number()
    user_interface()


if __name__ == "__main__":
    main()
