import tkinter as tk
from tkinter import ttk
import time

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def conditionsPopup(med):
        toplevel = tk.Toplevel()
        label = ttk.Label(toplevel, text=med["conditions"], font=LARGE_FONT, justify='center')
        label.pack(side="top", expand=False, padx=10, pady=10)

def popupmsg(med = {"name":"ERROR: NO INPUT", "conditions":"ERROR: NO INPUT"}):
        popup = tk.Tk()
        popup.wm_title("REMINDER")
        message = f"It is {time.localtime()[3] if (time.localtime()[3] < 13) else (time.localtime()[3]-12)}:{time.localtime()[4]:02}, time to take " + med["name"]
        label = ttk.Label(popup, text = message, font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)
        #label.pack(side = "left", fill = "x", padx = (10))
        confirm = ttk.Button(popup, text="Confirm", command = popup.destroy)
        ignore = ttk.Button(popup, text = "Ignore", command = popup.destroy)
        conditions = ttk.Button(popup, text = "Conditions", command = lambda: conditionsPopup(med))

        label.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        confirm.grid(row=1, column=0, pady=10)
        ignore.grid(row=1, column=1, pady=10)
        conditions.grid(row=1, column=2)
        popup.mainloop()