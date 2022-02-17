from tkinter import *
import random

def click():
    entered_text = text_entry.get() # gets input from text entry box
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry entry not found"
    output.insert(END, definition)


def close_window():

#main
window = Tk()
window.title("Random Number Generator for Texas Lottery")
window.config(background="black")

#Photo
lotto_photo = PhotoImage(file="texas_lottery_logo.gif")
Label (window, image=lotto_photo, bg="white").grid(row=0, column=0, sticky=E)

#create label
Label (window, text="Enter 1, 2, or 3 ", bg="black", fg="white",
       font="none 12 bold").grid(row=1, column=0, sticky=W)

#create a text entry box
text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=0, sticky=W)


#add a submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

#create a label
Label (window, text="These are your lucky lotto numbers:", bg="black", fg="white",
       font="none 12 bold").grid(row=4, column=0, sticky=W)

#create a text box
output = Text(window, width=75, height = 6, wrap= WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#dictionary
my_compdictionary = {
    'algorithm': 'step by step recipe', 'bug': 'error causing program to fail'
}

#create a label
Label (window, text="click to Exit", bg="black", fg="white",
       font="none 12 bold").grid(row=6, column=0, sticky=W)
Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

#run the main loop
window.mainloop()





# def main():
#     root()
#
#
# if __name__ == "__main__":
#     main()
#
