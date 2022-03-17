# Author: Jason Allen
# Date: 10 February 2022
#Portfolio Project: Lottery Number Generator
"""Microservice: Text based UI Service that reads a number from a file and
returns a set of lucky lottery numbers based on which lottery game the user
selects: Powerball or Mega Millions

Powerball numbers are 6 numbers total. 5 are in range 1 to 69 with an additional
last number that must be 1 to 26.

Mega Millions numbers are 6 numbers total. 5 are in range 1 to 70 with the final
number in the range 1 to 25

Writes user response to a text file
"""

import random
import subprocess
import csv

cmd = 'python numbers.py'
new_pipe = subprocess.Popen(cmd, shell= True)

def true_loop_condition():
    return True

def false_loop_condition():
    return False


def generate_powerball_nums():
    """generates powerball random numbers"""

    new_pipe = subprocess.Popen(cmd, shell=True)
    with open('lottoType.txt', 'w') as out:
        out.write("1")

    with open('numbers.txt', 'r') as infile:
        num = infile.readline()
        num = num.strip()
        print("These are your lucky POWERBALL numbers", num)
        print("\n")


def generate_mega_millions_nums():
    """generates set of random mega millions numbers"""
    new_pipe = subprocess.Popen(cmd, shell=True)
    with open('lottoType.txt', 'w') as out:
        out.write("2")

    with open('numbers.txt', 'r') as infile:
        num = infile.readline()
        num = num.strip()
        print("These are your lucky MEGA MILLIONS numbers", num)
        print("\n")


def hockey_score_csv_reader():
    with open('/Users/jason/cs361/Aaron_Project/output.txt') as fin, \
            open('output.csv', 'wb') as fout:
        csvin = csv.reader(fin)
        csvout = csv.writer(fout, delimiter='\t')
        for row in csvin:
            if row[1].strip(" ' ") == 'Toronto Maple Leafs':
                score = row[2].strip("[]")
                score = score.strip()
                with open('hockeyscore.txt', 'w') as inscore:
                    inscore.write(score)
            elif row[3].strip(" ' ") == 'Toronto Maple Leafs':
                score = row[4].strip("[]")
                score = score.strip()
                with open('hockeyscore.txt', 'w') as inscore:
                    inscore.write(score)


def generate_hockey_score_powerball_nums():
    """generates random set of powerball nums with hockey score as powerball num"""
    subprocess.Popen(cmd, shell=True)
    random_nums = []
    hockey_score_csv_reader()
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
                  "Toronto Maple Leafs game score as your powerball number",
                  num)
            print("\n")


def exit_program():
    """stops main program and exits"""
    with open('lottoType.txt', 'w') as out:
        out.write("4")
    print("You have chosen to EXIT the program. Goodbye.\n")
    return false_loop_condition()


def invalid_entry():
    print("INVALID ENTRY.\n")


def welcome_message():
    print("Welcome. Today is your lucky day. You have found a program that"
          " will help you generate a set of lottery numbers that you actually "
          "like. You have 3 options to choose from today: "
          " generate Texas Powerball numbers; Texas Mega Millions numbers; or"
          " for the Toronto Maple Leafs hockey fans, you can"
          " use the Leafs hockey score as your Texas Powerball number. "
          " Please create as many lists as you want, because your old lists will"
          " still be visible. Now, let's get your lucky numbers. \n")


def user_interface():
    """user interface takes input reads response and outputs lotto numbers"""

    welcome_message()
    while true_loop_condition():
        response = input("Enter 1 to generate your lucky numbers for Texas Powerball\n"
                         "or\n"
        "Enter 2 to generate your lucky numbers for Texas Mega Millions\n"
                         "or\n"
        "Enter 3 to use the Toronto Maple Leafs game score as your powerball number for "
                         "Powerball\n"
                         "or\n"
        "Enter 4 to exit program: \n")

        if response == '1':
            generate_powerball_nums()
        elif response == '2':
            generate_mega_millions_nums()
        elif response == '3':
            generate_hockey_score_powerball_nums()
        elif response == '4':
            exit_program()
            return false_loop_condition()
        else:
            invalid_entry()
            user_interface()


def main():
    user_interface()


if __name__ == "__main__":
    main()

