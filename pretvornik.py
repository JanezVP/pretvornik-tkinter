# -*- coding: UTF-8 -*-
import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window,
                         text="Pretvornik za kilometre in milje.")
greeting.pack()

entry_field = Tkinter.Entry(window)
entry_field.pack()

def check_kilometre():
    kilometer = int(entry_field.get())
    milja = kilometer * 0.621371

    tkMessageBox.showinfo("Milje",
                          milja)

check_button = Tkinter.Button(window,
                              text="Pretvori kilometre v milje",
                              command=check_kilometre)
check_button.pack()

def check_milje():
    milja = int(entry_field.get())
    kilometer = milja / 0.62137

    tkMessageBox.showinfo("Kilometer",
                          kilometer)

check_button = Tkinter.Button(window,
                              text="Pretvori milje v kilometre",
                              command=check_milje)
check_button.pack()


window.mainloop()