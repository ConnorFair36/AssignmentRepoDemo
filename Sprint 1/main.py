from json import load, dump
#from sys import argv

from meds import medsManager

#this is all temp to test the meds file
medsList = medsManager()
#medsList.clear()
medsList.addMedication("adderall", "take with food", 3, [8, 0], [20, 0], [14,0])
medsList.addMedication("xanax", "", 3, [7, 0], [12, 0], [-1,-1])
#medsList.clear()