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

import random
import subprocess

cmd = 'python numbers.py'
new_pipe = subprocess.Popen(cmd, shell= True)


def user_interface():
    """user interface takes input reads response and outputs lotto numbers"""


    while True:
        response = input("Enter 1 to generate your lucky numbers for Texas Powerball\n"
                         "or\n"
        "Enter 2 to generate your lucky numbers for Texas Mega Millions\n"
                         "or\n"
        "Enter 3 to use the Toronto Maple Leafs game score as your powerball number for "
                         "Powerball\n"
                         "or\n"
        "Enter 4 to exit program: \n")

        if response == '1':
            """
            1-write '1' in  lottoType.txt "
            2-sleep for 5 seconds
            3-read and output to lottoType.txt file
            """
            new_pipe = subprocess.Popen(cmd, shell=True)

            with open('lottoType.txt', 'w') as out:
                out.write("1")

            with open('numbers.txt', 'r') as infile:
                num = infile.readline()
                num = num.strip()
                print("These are your lucky POWERBALL numbers", num)
                print("\n")

        elif response == '2':
            new_pipe = subprocess.Popen(cmd, shell=True)
            with open('lottoType.txt', 'w') as out:
                out.write("2")

            with open('numbers.txt', 'r') as infile:
                num = infile.readline()
                num = num.strip()
                print("These are your lucky MEGA MILLIONS numbers", num)
                print("\n")

        elif response == '3':
            subprocess.Popen(cmd, shell=True)
            random_nums = []
            with open('numbers.txt', 'w') as outfile:
                for i in range(5):
                    random_nums.append(random.randint(1, 70))
                with open('hockeyscore.txt', 'r') as inscore:
                    score = inscore.readline()
                    score = int(score.strip())
                    random_nums.append(score)

                with open('numbers.txt', 'w') as outfile:
                    outfile.write(str(random_nums))

                with open('numbers.txt', 'r') as infile:
                    num = infile.readline()
                    num = num.strip()
                    print("These are your lucky POWERBALL numbers with the "
                    "Toronto Maple Leafs game score as your powerball number", num)
                    print("\n")

        elif response == '4':
            with open('lottoType.txt', 'w') as out:
                out.write("4")
            print("You have chosen to exit the program. Goodbye.")
            return

        else:
            print("Invalid entry.  Please enter 1, 2, or 3 to generate "
                  "lottery numbers.  To Exit, enter 4 \n")
            response = input(
                "Enter 1 to generate your lucky numbers for Texas Powerball\n"
                "or\n"
                "Enter 2 to generate your lucky numbers for Texas Mega Millions\n"
                "or\n"
                "Enter 3 to use the Toronto Maple Leafs game score as your "
                "powerball number for Powerball\n"
                "or\n"
                "Enter 4 to exit program: \n")


def main():
    user_interface()


if __name__ == "__main__":
    main()

