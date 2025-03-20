from json import load, dump
#from sys import argv

from meds import medsManager

#this is all temp to test the meds file
medsList = medsManager()
medsList.clear()
medsList.addMedication("adderall", "take with food", 3, [8, 0], [12, 35], [20,0])
medsList.addMedication("xanax", "", 3, [7, 0])
while(1):
    medsList.reminderCheck()
