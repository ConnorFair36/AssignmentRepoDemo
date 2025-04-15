import tkinter as tk
from tkinter import ttk
import time

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)



class popupmsg():
    def __init__(self, med = {"name":"ERROR: NO INPUT", "conditions":"ERROR: NO INPUT"}, fileName = None):
        self.med = med
        self.fileName = fileName
        self.popup = tk.Tk()
        self.popup.wm_title("REMINDER")
        message = f"It is {time.localtime()[3] if (time.localtime()[3] < 13) else (time.localtime()[3]-12)}:{time.localtime()[4]:02}, time to take " + med["name"]
        label = ttk.Label(self.popup, text = message, font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)
        #label.pack(side = "left", fill = "x", padx = (10))
        confirm = ttk.Button(self.popup, text="Confirm", command = self.report)
        ignore = ttk.Button(self.popup, text = "Ignore", command = self.popup.destroy)
        conditions = ttk.Button(self.popup, text = "Conditions", command = lambda: self.conditionsPopup())

        label.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        confirm.grid(row=1, column=0, pady=10)
        ignore.grid(row=1, column=1, pady=10)
        conditions.grid(row=1, column=2)
        self.popup.call('wm', 'attributes', '.', '-topmost', '1')
        self.popup.mainloop()

    def report(self):
        try:
            with open(self.fileName, mode="a") as f:
                f.write(self.med["name"] + f" taken at {time.localtime()[3] if (time.localtime()[3] < 13) else (time.localtime()[3]-12)}:{time.localtime()[4]:02} on {time.localtime()[1]}/{time.localtime()[2]}/{time.localtime()[0]}\n")
                        
        except FileNotFoundError:
            print(f"File '{self.fileName}' not found! Aborting")
            exit(1)
        f.close()
        self.popup.destroy()
        
    def conditionsPopup(self):
        toplevel = tk.Toplevel()
        label = ttk.Label(toplevel, text=self.med["conditions"], font=LARGE_FONT, justify='center')
        label.pack(side="top", expand=False, padx=10, pady=10)