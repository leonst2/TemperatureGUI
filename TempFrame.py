from tkinter import *
import colorpalet as cp


class TempFrame(Frame):

    def __init__(self, master, posx, posy, width, height, bgcolor):

        super().__init__(master, height=height, width=width)

        dataPanel = Frame(master, width=width, height=height, bg=bgcolor)
        dataPanel.place(x=posx, y=posy)

        headerLabel = Label(dataPanel, text="Recent Data:")
        headerLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        headerLabel.config(font=("Arial", 18, "underline", "bold"))

        maxLabel = Label(dataPanel, text="Maximum temperature:")
        maxLabel.place(relx=0.4, rely=0.4, anchor=CENTER)
        maxLabel.config(font=("Arial", 10))
        maxBg = Frame(dataPanel, height=18, width=80, bg=cp.white)
        maxBg.place(relx=0.7, rely=0.4, anchor=CENTER)

        minLabel = Label(dataPanel, text="Minimum temperature:")
        minLabel.place(relx=0.4, rely=0.6, anchor=CENTER)
        minLabel.config(font=("Arial", 10))
        minBg = Frame(dataPanel, height=18, width=80, bg=cp.white)
        minBg.place(relx=0.7, rely=0.6, anchor=CENTER)

        avgLabel = Label(dataPanel, text="Average temperature:")
        avgLabel.place(relx=0.4, rely=0.8, anchor=CENTER)
        avgLabel.config(font=("Arial", 10))
        avgBg = Frame(dataPanel, height=18, width=80, bg=cp.white)
        avgBg.place(relx=0.7, rely=0.8, anchor=CENTER)

        infoLabel = Label(dataPanel, text="These data were collected the last 24h")
        infoLabel.place(relx=0.5, rely=0.95, anchor=CENTER)
        infoLabel.config(font=("Charcoal", 8, "italic"), fg=cp.darkGrey)
