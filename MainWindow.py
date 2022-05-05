from tkinter import *

from TopFrame import TopFrame
from AdminFrame import AdminFrame
from TempFrame import TempFrame
from GraphFrame import GraphFrame
from GradientFrame import GradientFrame
import colorpalet as cp

#Create GUI window
window = Tk()

#Set start parameter for the GUI size and position
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
app_h = 775
app_w = 1400
posX = (screen_w / 2) - (app_w / 2)
posY = (screen_h / 2) - (app_h / 2)

#Settings for the GUI appearance
window.geometry(f'{app_w}x{app_h}+{int(posX)}+{int(posY)}')
gf = GradientFrame(window, colors=(cp.lightPink, cp.purple), width=app_w, height=app_h)
gf.place(x=0, y=0)
gf.pack()
window.title("Temperature-Master")
window.resizable(False, False)
window.overrideredirect(True)


#Configure of the top frame
topFrame = TopFrame(master=window, posx=25, posy=25, width=1350, height=50, bgcolor=cp.lightGrey)

#Create frame at side top
adminFrame = AdminFrame(master=window, posx=25, posy=100, width=400, height=200, bgcolor=cp.lightGrey)

#Create frame at side mid
dataFrame = TempFrame(master=window, posx=25, posy=325, width=400, height=200, bgcolor=cp.lightGrey)

#Create frame at side bottom
sidePanel03 = Frame(window, width=400, height=200, bg=cp.lightGrey)
sidePanel03.place(x=25, y=550)

#Create graph with data
graphFrame = GraphFrame(master=window, posx=450, posy=100, width=925, height=650, bgcolor=cp.lightGrey)

window.mainloop()
