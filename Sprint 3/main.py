from json import load, dump
#from sys import argv

from meds import medsManager
import reminder
import window
from patient import patient
import time

#this is all temp to test the meds file
TopherMaguire = patient("Topher", "Maguire", "349-298-2918", "United Healthcare", [9,11,2001])

TopherMaguire.clearMedsList()

TopherMaguire.addMedication("Test medication 1", "None", 3, [time.localtime()[3], time.localtime()[4]], [14, 14], [20,0])
TopherMaguire.addMedication("Test medication 2", "take with food", 0, [14, 19])
TopherMaguire.addMedication("Test medicaiton 3", "don't mix with alcohol (;", 5, [time.localtime()[3], time.localtime()[4]], [17, 24])

TopherMaguire.removeMedicaiton("Test medication 2")
# TopherMaguire.generateReport()

while(1):
     TopherMaguire.reminderCheck()