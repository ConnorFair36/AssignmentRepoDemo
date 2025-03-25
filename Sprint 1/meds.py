import json
from reminder import reminder

class medsManager():
    def __init__(self, name=""):
        self.reminder = reminder()
    def addMedication(self, name="", conditions="", severity=0, time1=[-1, -1], time2=[-1, -1], time3=[-1, -1]):
        if(severity < 0 or severity > 5):#returns false if medicaiton information is invalid
            return False
        if(time1[0] < -1 or time1[0] > 24 or time1[1] < -1 or time1[1] > 60):
            return False
        if(time2[0] < -1 or time2[0] > 24 or time2[1] < -1 or time2[1] > 60):
            return False
        if(time3[0] < -1 or time3[0] > 24 or time3[1] < -1 or time3[1] > 60):
            return False
        else:#returns true if medicaion is valid and added to list
            self.newMed = {
                "name" : name,
                "conditions" : conditions,
                "severity" : severity,
                "time1" :{
                    "hours" : time1[0],
                    "minutes" : time1[1]
                },
                "time2" :{
                    "hours" : time2[0],
                    "minutes" : time2[1]
                },
                "time3" :{
                    "hours" : time3[0],
                    "minutes" : time3[1]
                },
            }
            self.writeMedication()
            return True

    def getMedsList(self):
        medsArray = []
        try:
            with open("medsList.json", mode="r", encoding="utf-8") as f:
                try:
                    medsArray = json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
                
        except FileNotFoundError:
            print(f"File 'medsList.json' not found! Aborting")
            exit(1)
        f.close()
        return medsArray

    def writeMedication(self):
        self.medsArray = self.getMedsList()
        self.medsArray.append(self.newMed)
        try:
            with open("medsList.json", mode="w", encoding="utf-8") as self.medsList:
                json.dump(self.medsArray, self.medsList, indent = 4)
        except FileNotFoundError:
            print(f"File 'medsList.json' not found! Aborting")
            exit(1)
        self.medsList.close()

    def clear(self):
        try:
            with open("medsList.json", mode="w", encoding="utf-8") as self.medsList:
                pass
        except FileNotFoundError:
            print(f"File 'medsList.json' not found! Aborting")
            exit(1)
        self.medsList.close()

    def reminderCheck(self):
        for medication in self.medsArray:
            self.reminder.check(medication)

