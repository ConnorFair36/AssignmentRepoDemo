import tkinter as tk
from tkinter import ttk
import time

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def popupmsg(name):
        popup = tk.Tk()
        popup.wm_title("REMINDER")
        message = f"It is {time.localtime()[3] if (time.localtime()[3] < 13) else (time.localtime()[3]-12)}:{time.localtime()[4]:02}, time to take " + name
        label = ttk.Label(popup, text = message, font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)
        #label.pack(side = "left", fill = "x", padx = (10))
        confirm = ttk.Button(popup, text="Confirm", command = popup.destroy)
        ignore = ttk.Button(popup, text = "Ignore", command = popup.destroy)
        conditions = ttk.Button(popup, text = "Conditions V", command = popup.destroy)
        confirm.pack(side = "right", fill = "x", padx = 10)
        ignore.pack(side = "left", fill = "x", padx = 10)
        #conditions.pack(side = "right", fill = "both", padx = 10)
        popup.mainloop()