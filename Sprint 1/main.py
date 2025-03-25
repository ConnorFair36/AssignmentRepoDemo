from json import load, dump
#from sys import argv

from meds import medsManager
import window

#this is all temp to test the meds file
medsList = medsManager()

med={"name" : "test", "conditions":"test test test test test\ntest test test"}
window.popupmsg(med)
# medsList.clear()
# medsList.addMedication("adderall", "take with food", 3, [8, 0], [14, 14], [20,0])
# medsList.addMedication("xanax", "", 3, [7, 0])
# while(1):
#     medsList.reminderCheck()