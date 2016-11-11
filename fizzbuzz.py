# -*- coding: UTF-8 -*-
import Tkinter
import tkMessageBox
window = Tkinter.Tk()

greeting = Tkinter.Label(window,
                         text="Vnesite stevilko med 1 in 100:.")
greeting.pack()

entry_field = Tkinter.Entry(window)
entry_field.pack()

def check_number():
    stevilo = int(entry_field.get())
    for stevilo in range(1, stevilo + 1):
        if stevilo % 3 == 0 and stevilo % 5 == 0:
            alert_text = "fizzbuzz"
        elif stevilo % 5 == 0:
            alert_text = "buzz"
        elif stevilo % 3 ==  0:
            alert_text = "fizz"
        else:
            alert_text = stevilo

        tkMessageBox.showinfo("fizzbuzz",
                          alert_text)

check_button = Tkinter.Button(window,
                              text="Start",
                              command=check_number)
check_button.pack()


window.mainloop()