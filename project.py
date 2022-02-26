# Aaron Wheaton
# CS 361
# NHL Data Scraper
# This program is designed to produce the box scores for a user based off
# NHL team, chosen time frame, etc.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import requests
import PIL
import os
import sys

from tkinter import *


# # Main class
class Application:
    def __init__(self, master):  # Constructor
        frame = Frame(master)
        frame.pack()
        btn_one = Button(master, text='Exit', command=quit)
        btn_one.pack(side=BOTTOM)


root = Tk()
app = Application(root)
root.title('NHL Schedule Scraper')
root.minsize(300, 300)

z = tk.IntVar()

tk.Label(root,
         text="""Choose how you want to select a date range for NHL Games (Note: if you arent sure, 
        just pick your own dates with the calendar!):""",
         font=16,
         justify=tk.LEFT,
         padx=20).pack()

tk.Radiobutton(root,
               text="Import Dates of NHL Games (Note: if you select this option, you will require a text file with the dates!",
               padx=20,
               font=14,
               variable=z,
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="No thanks, I'll choose my own NHL Game Dates",
               padx=20,
               font=14,
               variable=z,
               value=2).pack(anchor=tk.W)

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

teams = [("Tampa Bay Lightning", 14),
         ("Florida Panthers", 13),
         ("Toronto Maple Leafs", 10),
         ("Boston Bruins", 6),
         ("Detroit Red Wings", 17)]

tk.Label(root,
         text="""Choose your favorite Atlantic Division NHL Team:""",
         font=14,
         justify=tk.LEFT,
         padx=20).pack()

for teams, val in teams:
    tk.Radiobutton(root,
                   text=teams,
                   padx=20,
                   font=14,
                   variable=v,
                   value=val).pack(anchor=tk.W)

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Schedule Selector')
label1.config(font=('helvetica', 13))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root,
                  text='Utilize our calendars to pick dates for NHL games!:')
label2.config(font=('helvetica', 13))
canvas1.create_window(200, 100, window=label2)

cal1 = Calendar(root, selectmode='day',
                year=2021, month=10,
                date_pattern='y-mm-dd',
                day=1)

cal1.pack(pady=20)
cal1.lift()

cal2 = Calendar(root, selectmode='day',
                year=2021, month=11,
                date_pattern='y-mm-dd',
                day=1)

cal2.pack(pady=20)


def getSchedule():
    teams = [("Tampa Bay Lightning", 14),
             ("Florida Panthers", 13),
             ("Toronto Maple Leafs", 10),
             ("Boston Bruins", 6),
             ("Detroit Red Wings", 17)]

    team_name = None
    x_check = v.get()
    for teams in teams:
        if teams[1] == x_check:
            team_name = teams[0]

    x1 = team_name

    if z.get() == 1:
        file2 = open("dates.txt", "r+")
        Lines = file2.readlines()
        x2 = Lines[0].strip()
        x3 = Lines[1].strip()

    else:
        x2 = cal1.get_date()
        x3 = cal2.get_date()

    api_url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId=" + str(
        x_check) + "&startDate=" + str(x2) + "&endDate=" + str(x3)
    response = requests.get(api_url)
    game_data = response.json()
    game_list = []
    for var in game_data['dates']:
        game_array = []
        game_array.append(var['date'])
        game_array.append(var['games'][0]['teams']['home']['team']['name'])
        game_array.append(var['games'][0]['teams']['home']['score'])
        game_array.append(var['games'][0]['teams']['away']['team']['name'])
        game_array.append(var['games'][0]['teams']['away']['score'])
        game_list.append(game_array)

    gameList(game_list)


def gameList(game_list):
    root = Tk()
    root.title("List of games between that time:")
    w = 600  # popup window width
    h = 600  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    for i in game_list:
        Label(root, text=" " + str(i)).pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()

    def exportGames():
        fullpath = os.path.join(os.path.dirname(sys.argv[0]), 'output.txt')
        file1 = open("output.txt", "w+")
        file1.truncate(0)
        for i in game_list:
            file1.write(str(i) + "\n")
        file1.close()
        root = Tk()
        root.title("File Exported!")
        w = 350  # popup window width
        h = 350  # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        label2 = tk.Label(root,
                          text='Games succesfully exported to output.txt!')
        label2.config(font=('helvetica', 10))
        label2.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()

    export_button = Button(root, text='Export to txt file', command=exportGames,
                           bg='brown', fg='white',
                           font=('helvetica', 9, 'bold'))
    export_button.pack()
    mainloop()


button1 = tk.Button(text='List the scheduled games', command=getSchedule,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
