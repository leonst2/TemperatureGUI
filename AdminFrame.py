from tkinter import *
import numpy as np
import colorpalet as cp


triesData = np.loadtxt("loginData.txt", dtype="str", delimiter=";")
tries = int(triesData[2])


class AdminFrame(Frame):

    def __init__(self, master, posx, posy, width, height, bgcolor):

        super().__init__(master, height=height, width=width)

        def login(event):
            global tries
            checkUser = userEntry.get()
            checkPass = passwordEntry.get()
            if (checkUser != "") and (checkPass != ""):
                loginData = np.loadtxt("loginData.txt", dtype="str", delimiter=";")
                dataUser = loginData[0]
                dataPass = loginData[1]
                if (checkUser.encode("utf-8").hex() == dataUser) and (checkPass.encode("utf-8").hex() == dataPass):
                    userEntry.delete(0, "end")
                    passwordEntry.delete(0, "end")
                    loginButton.config(text="LOGOUT", bg=cp.purple, font=("Arial", 10))
                    loginButton.bind("<Button-1>", logout)
                    messageLabel.config(text="Logged in successfully", fg=cp.limegreen)
                    tries = 3
                else:
                    tries -= 1
                    messageLabel.config(text="ERROR: Username or password is not correct. Tries: " + str(tries))
            else:
                messageLabel.config(text="ERROR: Enter username and password")
            if tries <= 0:
                loginButton.config(state=DISABLED, bg=cp.lightGrey, fg=cp.purple)
                loginButton.unbind("<Button-1>")
                userEntry.unbind("<Button-1>")
                passwordEntry.unbind("<Button-1>")
                passwordEntry.unbind("Leave")
                loginButton.unbind("<Enter>")
                messageLabel.config(text="ERROR: No more tries")

        def logout(event):
            userEntry.delete(0, "end")
            passwordEntry.delete(0, "end")
            loginButton.config(text="LOGIN", bg=cp.purple, font=("Arial", 10))
            loginButton.bind("<Button-1>", login)
            messageLabel.config(text="Logged out successfully", fg=cp.limegreen)

        def hoverEnter(event, btn):
            btn.config(bg=cp.purple, fg=cp.lightGrey)

        def hoverLeave(event, btn):
            btn.config(bg=cp.lightGrey, fg=cp.purple)

        def hideError(event):
            messageLabel.config(text="", fg=cp.closeRed)

        adminPanel = Frame(master, width=width, height=height, bg=bgcolor)
        adminPanel.place(x=posx, y=posy)

        headerLabel = Label(adminPanel, text="Admin Login:")
        headerLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        headerLabel.config(font=("Arial", 18, "underline", "bold"))

        userLabel = Label(adminPanel, text="Username:")
        userLabel.place(relx=0.15, rely=0.4, anchor=CENTER)
        userLabel.config(font=("Arial", 10))

        userEntry = Entry(adminPanel, width=30, bd=0)
        userEntry.place(relx=0.6, rely=0.4, anchor=CENTER)
        userEntry.config(font=("Arial", 10))
        userEntry.bind("<Button-1>", hideError)

        passwordLabel = Label(adminPanel, text="Password:")
        passwordLabel.place(relx=0.15, rely=0.6, anchor=CENTER)
        passwordLabel.config(font=("Arial", 10))

        passwordEntry = Entry(adminPanel, width=30, bd=0, show="*")
        passwordEntry.place(relx=0.6, rely=0.6, anchor=CENTER)
        passwordEntry.config(font=("Arial", 10))
        passwordEntry.bind("<Button-1>", hideError)

        loginButton = Button(adminPanel, width=15, text="LOGIN", bg=cp.lightGrey, fg=cp.purple, activebackground=cp.purple, bd=0, relief=SUNKEN)
        loginButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        loginButton.config(font=("Arial", 10, "bold"))
        loginButton.bind("<Button-1>", login)
        loginButton.bind("<Enter>", lambda event, btn=loginButton: hoverEnter(event, btn))
        loginButton.bind("<Leave>", lambda event, btn=loginButton: hoverLeave(event, btn))

        messageLabel = Label(adminPanel)
        messageLabel.place(relx=0.5, rely=0.95, anchor=CENTER)
        messageLabel.config(font=("Charcoal", 8, "italic"), fg=cp.closeRed)
