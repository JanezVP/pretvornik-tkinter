# -*- coding: UTF-8 -*-
import Tkinter
import tkMessageBox


window = Tkinter.Tk()

greeting = Tkinter.Label(window,
                         text="Vnesite kilometre in jaz vam bom izracunal milje.")
greeting.pack()

entry_field = Tkinter.Entry(window)
entry_field.pack()



def check_number(): #spodaj preverimo stevilko
    kilometer = int(entry_field.get())
    milja = kilometer * 0.621371

    tkMessageBox.showinfo("Milje",
                          milja)

check_button = Tkinter.Button(window,
                              text="Pretvori",
                              command=check_number)
check_button.pack()


window.mainloop()