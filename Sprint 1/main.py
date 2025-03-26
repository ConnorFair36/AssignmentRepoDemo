from json import load, dump
#from sys import argv

from meds import medsManager
import reminder
import window

#this is all temp to test the meds file
medsList = medsManager()

# medsList.clear()

# medsList.addMedication("Test medication 1", "", 3, [8, 0], [14, 14], [20,0])
# medsList.addMedication("Test medication 2", "take with food", 0, [18, 42])

while(1):
     medsList.reminderCheck()