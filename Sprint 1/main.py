from json import load, dump
#from sys import argv

from meds import medsManager
import reminder
import window
from patient import patient

#this is all temp to test the meds file
TopherMaguire = patient("Topher", "Maguire", "349-298-2918", "United Healthcare", [9,11,2001])

TopherMaguire.clearMedsList()

TopherMaguire.addMedication("Test medication 1", "", 3, [8, 0], [14, 14], [20,0])
TopherMaguire.addMedication("Test medication 2", "take with food", 0, [14, 19])
TopherMaguire.addMedication("Test medicaiton 3", "don't mix with alcohol (;", 5, [9, 36], [17, 24])

TopherMaguire.removeMedicaiton("Test medication 2")

# while(1):
#      TopherMaguire.reminderCheck()