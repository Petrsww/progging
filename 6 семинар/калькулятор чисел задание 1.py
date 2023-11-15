from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def show_message():
    label["text"] = eval(entry.get())
root = Tk()
root.title("калькулятор")
root.geometry("200x100")

entry = ttk.Entry()
entry.pack()

btn = ttk.Button(text="Посчитать", command=show_message)
btn.pack()


label = ttk.Label()
label.pack()

root.mainloop()
