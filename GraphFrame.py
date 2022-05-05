from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import numpy as np
import mplcursors
import colorpalet as cp
from matplotlib.widgets import MultiCursor


#Test data for chart
tempData01 = {'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                       '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
              'Temperature01': [0.0, 1.0, 1.5, 2.0, 2.0, 4.0, 6.5, 9.0, 11.0, 14.0, 15.5, 17.0, 19.5,
                                24.0, 25.5, 27.0, 27.5, 25.0, 22.0, 18.0, 8.0, 6.0, 4.0, 2.0]
              }
tempInsert01 = DataFrame(tempData01, columns=['Time', 'Temperature01'])
print(tempInsert01)

tempData02 = {'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                       '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
              'Temperature02': [2.0, 3.0, 3.5, 4.0, 5.0, 6.0, 8.5, 11.0, 13.0, 16.0, 17.5, 19.0, 21.5,
                                26.0, 27.5, 29.0, 29.5, 0.0, 24.0, 20.0, 10.0, 8.0, 6.0, 4.0]
              }
tempInsert02 = DataFrame(tempData02,  columns=['Time', 'Temperature02'])
print(tempInsert02)


class GraphFrame(FigureCanvasTkAgg):

    def __init__(self, master, posx, posy, width, height, bgcolor):

        def clearGraph(event):
            ax1.clear()
            line.draw()
            cursor.remove()

        def refreshGraph(event):
            ax1.clear()
            df2 = tempInsert02[["Time", "Temperature02"]].groupby("Time").sum()
            df2.plot(kind="line", legend=True, ax=ax1, color=cp.neonBlue, marker="o", fontsize=10)
            line.draw()
            cursor.remove()
            cursor2 = mplcursors.cursor(ax1, hover=True)
            cursor2.connect("add", lambda sel: sel.annotation.set_text('Time: {}h, Temperature: {}°'.format(int(sel.target[0]), int(sel.target[1]))))

        def saveGraph(event):
            cursor.visible = False
            figure.savefig("figure.jpg")

        def addCursor(event):
            cursor.visible = True
            cursorButton.config(text="Remove cursor")
            cursorButton.bind("<Button-1>", removeCursor)

        def removeCursor(event):
            cursor.visible = False
            cursorButton.config(text="Add cursor")
            cursorButton.bind("<Button-1>", addCursor)

        def hoverEnter(event, btn):
            btn.config(bg=cp.purple, fg=cp.lightGrey)

        def hoverLeave(event, btn):
            btn.config(bg=cp.lightGrey, fg=cp.purple)

        # Create graph with temperature data
        figure = plt.Figure(figsize=(6, 6), dpi=100)
        ax1 = figure.add_subplot(111)
        line = FigureCanvasTkAgg(figure, master)
        line.get_tk_widget().place_configure(width=width, height=height-50, x=posx, y=posy)
        df1 = tempInsert01[["Time", "Temperature01"]].groupby("Time").sum()
        df1.plot(kind="line", legend=True, ax=ax1, color="r", marker="o", fontsize=10)

        cursor = mplcursors.cursor(ax1, hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text('Time: {}h, Temperature: {}°'.format(int(sel.target[0]), int(sel.target[1]))))

        toolBar = Frame(master, width=width, height=50, bg=bgcolor)
        toolBar.place(x=posx, y=posy + height - 50)

        clearButton = Button(toolBar, width=15, text="Clear", bg=cp.lightGrey, fg=cp.purple, activebackground=cp.purple, bd=0, relief=SUNKEN)
        clearButton.place(relx=0.2, rely=0.5, anchor=CENTER)
        clearButton.config(font=("Arial", 10, "bold"))
        clearButton.bind("<Enter>", lambda event, btn=clearButton: hoverEnter(event, btn))
        clearButton.bind("<Leave>", lambda event, btn=clearButton: hoverLeave(event, btn))
        clearButton.bind("<Button-1>", clearGraph)

        refreshButton = Button(toolBar, width=15, text="Refresh", bg=cp.lightGrey, fg=cp.purple, activebackground=cp.purple, bd=0, relief=SUNKEN)
        refreshButton.place(relx=0.4, rely=0.5, anchor=CENTER)
        refreshButton.config(font=("Arial", 10, "bold"))
        refreshButton.bind("<Enter>", lambda event, btn=refreshButton: hoverEnter(event, btn))
        refreshButton.bind("<Leave>", lambda event, btn=refreshButton: hoverLeave(event, btn))
        refreshButton.bind("<Button-1>", refreshGraph)

        saveButton = Button(toolBar, width=15, text="Save graph", bg=cp.lightGrey, fg=cp.purple, activebackground=cp.purple, bd=0, relief=SUNKEN)
        saveButton.place(relx=0.6, rely=0.5, anchor=CENTER)
        saveButton.config(font=("Arial", 10, "bold"))
        saveButton.bind("<Enter>", lambda event, btn=saveButton: hoverEnter(event, btn))
        saveButton.bind("<Leave>", lambda event, btn=saveButton: hoverLeave(event, btn))
        saveButton.bind("<Button-1>", saveGraph)

        cursorButton = Button(toolBar, width=15, text="Remove cursor", bg=cp.lightGrey, fg=cp.purple, activebackground=cp.purple, bd=0, relief=SUNKEN)
        cursorButton.place(relx=0.8, rely=0.5, anchor=CENTER)
        cursorButton.config(font=("Arial", 10, "bold"))
        cursorButton.bind("<Enter>", lambda event, btn=cursorButton: hoverEnter(event, btn))
        cursorButton.bind("<Leave>", lambda event, btn=cursorButton: hoverLeave(event, btn))
        cursorButton.bind("<Button-1>", removeCursor)
