from tkinter import *
from main import *

root = Tk()

# Configuiring Tk window
root.geometry("650x170")
root.resizable(width=0, height=0)
root.title("Flipkart Reviews Fetcher")
root.configure(bg='white')

# Defining on-screen objects

webpg_label = Label(root, text="Webpage URL:", bg='white', font=('Ariel', 12))
num_revs_label = Label(root, text="Number of reviews to fetch:", bg='white', font=('Ariel', 10))

webpg_edittxt = Entry(root, width=70, borderwidth=3)
webpg_edittxt.insert(END, 'https://www.flipkart.com/')
num_revs_edittxt = Entry(root, width=70, borderwidth=3)
num_revs_edittxt.insert(END, 'Multiple of 10 is preferred')

status_label = Label(root, text="Status: Waiting", font=('Helvetica bold', 15), bg='white')


def get_revs():
    webpage = webpg_edittxt.get()
    num_revs = num_revs_edittxt.get()
    mainfn(webpage, num_revs)
    status_label.config(text="Status: Success", fg="green", font=('Helvetica bold', 26))


submit_butt = Button(root, text="Submit", command=get_revs)

# Placing everything on screen

webpg_label.grid(row=0, column=0)
num_revs_label.grid(row=1, column=0, padx=10)
webpg_edittxt.grid(row=0, column=1, pady=20, padx=10)
num_revs_edittxt.grid(row=1, column=1)
submit_butt.grid(row=2, column=0, ipadx=20, ipady=5, pady=20)
status_label.grid(row=2, column=1)

root.mainloop()
