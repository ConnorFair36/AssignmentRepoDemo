from json import load, dump
import time

from patient import patient

#this is all temp to test the meds file
CatherineSmith = patient("Catherine", "Smith", "349-298-2918", "United Healthcare", [9,11,2001])

CatherineSmith.addMedication(name = "Test medication 1", time1=[8,30], time2=[14, 14], time3=[20,0])
CatherineSmith.addMedication("Test medication 2", "don't mix with alcohol (;", 0, [12, 45])

CatherineSmith.removeMedicaiton("Test medication 1")

CatherineSmith.addMedication("Test medicaiton 3", "take with food", 5, [time.localtime()[3], time.localtime()[4]], [17, 24])

while(1):
     CatherineSmith.reminderCheck()