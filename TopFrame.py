from tkinter import *
import colorpalet as cp
import mysql.connector


class TopFrame(Frame):

    def __init__(self, master, posx, posy, width, height, bgcolor):
        super().__init__(master, height=height, width=width)

        def hoverEnter(event, btn):
            btn.config(bg=cp.closeRed, fg=cp.lightGrey)

        def hoverLeave(event, btn):
            btn.config(bg=cp.lightGrey, fg=cp.closeRed)

        def testDB():
            db = mysql.connector.connect(
                host="localhost",
                user="1inf1tempsens",
                password="awHqqS9SS0wtiqbW",
                database="1inf1tempsens"
            )
            curser = db.cursor()
            curser.execute("CREATE TABLE Test (test VARCHAR(50))")

        topPanel = Frame(master, width=width, height=height, bg=bgcolor)
        topPanel.place(x=posx, y=posy)

        closeButton = Button(topPanel, width=5,
                             bg=cp.lightGrey,
                             fg=cp.closeRed,
                             activebackground=cp.closeRed,
                             text="QUIT",
                             bd=0,
                             command=master.quit,
                             relief=SUNKEN)
        closeButton.place(relx=0.97, rely=0.5, anchor=CENTER)
        closeButton.config(font=("Arial", 12, "bold"))
        closeButton.bind("<Enter>", lambda event, btn=closeButton: hoverEnter(event, btn))
        closeButton.bind("<Leave>", lambda event, btn=closeButton: hoverLeave(event, btn))

        titleText = Label(topPanel, text="Temperature Overview")
        titleText.place(relx=0.5, rely=0.5, anchor=CENTER)
        titleText.config(font=("Arial", 22, "underline", "bold"))

        testBtn = Button(topPanel, width=5,
                         bg=cp.lightGrey,
                         fg=cp.closeRed,
                         activebackground=cp.closeRed,
                         text="TEST",
                         bd=0,
                         command=testDB,
                         relief=SUNKEN)
        testBtn.place(relx=0.2, rely=0.5, anchor=CENTER)
        testBtn.config(font=("Arial", 12, "bold"))
