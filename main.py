# Author: Jason Allen
# Date: 10 February 2022
#Assignment 6: Minimum Viable Product
"""Microservice: Text based UI Service that reads a number from a file and
returns a set of lucky lottery numbers based on which lottery game the user
selects: Powerball or Mega Millions

Powerball numbers are 6 numbers total. 5 are in range 1 to 69 with an additional
last number that must be 1 to 26.

Mega Millions numbers are 6 numbers total. 5 are in range 1 to 70 with the final
number in the range 1 to 25

Writes user response to a text file: lottoType.txt
"""
import time
# from numbers import random_number # testing line

def user_interface():

    while True:
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
            3-read and output to lottoType.txt file
            """
            # random_number() #testing line
            with open('lottoType.txt', 'w') as out:
                out.write("1")
            # time.sleep(2)
            with open('numbers.txt', 'r') as infile:
                num = infile.readline()
                num = num.strip()
                print("These are your lucky POWERBALL numbers", num)

        elif response == '2':
            # random_number()  #testing line
            with open('lottoType.txt', 'w') as out:
                out.write("2")
            # time.sleep(2)
            with open('numbers.txt', 'r') as infile:
                num = infile.readline()
                num = num.strip()
                print("These are your lucky MEGA MILLIONS numbers", num)

        elif response == '3':
            print("You have chosen to exit the program. Goodbye.")
            return
        else:
            print("Invalid entry")


def main():
    # random_number() #testing line
    user_interface()


if __name__ == "__main__":
    main()
