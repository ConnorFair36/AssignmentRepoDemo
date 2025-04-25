import json
import time
from reminder import reminder

class medsManager():
    def __init__(self, name=""):
        # self.reminder = reminder()
        self.reminderArray = []
        self.listFileName = name + "Meds_List.json"
        self.reportFileName = name + "Report.json"
        
        try:#creates meds list file
            with open(self.listFileName, mode="a", encoding="utf-8") as f:
                pass
        except FileNotFoundError:
            print(f"File '{self.listFileName}' not found! Aborting")
            exit(1)
        f.close()

        try:#creates report file
            with open(self.reportFileName, mode="a", encoding="utf-8") as f:
                pass
        except FileNotFoundError:
            print(f"File '{self.reportFileName}' not found! Aborting")
            exit(1)
        f.close()

        self.medsArray = self.getMedsList()
        

    def addMedication(self, name="", conditions="None", severity=0, time1=[-1, -1], time2=[-1, -1], time3=[-1, -1]):
        if(severity < 0 or severity > 5):#returns false if medicaiton information is invalid
            return False
        if(time1[0] < -1 or time1[0] > 24 or time1[1] < -1 or time1[1] > 60):
            return False
        if(time2[0] < -1 or time2[0] > 24 or time2[1] < -1 or time2[1] > 60):
            return False
        if(time3[0] < -1 or time3[0] > 24 or time3[1] < -1 or time3[1] > 60):
            return False
        else:#returns true if medicaion is valid and added to list
            newMed = {
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
            self.medsArray = self.getMedsList()
            self.medsArray.append(newMed)
            self.writeMedication()
            return True

    def getMedsList(self):
        medsArray = []
        try:
            with open(self.listFileName, mode="r", encoding="utf-8") as f:
                try:
                    medsArray = json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
                
        except FileNotFoundError:
            print(f"File '{self.listFileName}' not found! Aborting")
            exit(1)
        f.close()
        return medsArray

    def writeMedication(self):
        #self.medsArray = self.getMedsList()
        try:
            with open(self.listFileName, mode="w", encoding="utf-8") as self.medsList:
                if(len(self.medsArray) > 0):
                    json.dump(self.medsArray, self.medsList, indent = 4)
                else:
                    pass
        except FileNotFoundError:
            print(f"File '{self.listFileName}' not found! Aborting")
            exit(1)
        self.medsList.close()

    def clear(self):
        try:
            with open(self.listFileName, mode="w", encoding="utf-8") as self.medsList:
                pass
        except FileNotFoundError:
            print(f"File '{self.listFileName}' not found! Aborting")
            exit(1)
        self.medsList.close()

    def removeMedication(self, name = ""):
        self.medsArray = self.getMedsList()
        # if(len(self.medsArray) > 0):
        toRemove = None
        for med in self.medsArray:
            if med["name"] == name:
                toRemove = med
                break
        try:
            if(toRemove != None): self.medsArray.remove(toRemove)
            self.writeMedication()
            # print(self.medsArray)
        except ValueError:
            print("ERROR: medication not found in list")
        
    def reminderCheck(self):
        self.medsArray = self.getMedsList()
        if(len(self.reminderArray) != len(self.medsArray)):#creates array large enough for all medications
            self.reminderArray = [None for i in range(len(self.medsArray))]
            for c in range(len(self.medsArray)):
                self.reminderArray[c] = reminder()#instantiates new reminder for each medication
        for c in range(len(self.medsArray)):
            self.reminderArray[c].check(self.medsArray[c], self.reportFileName)#checks each medication
    


    def printReport(self, report={"name":"", "time":time.gmtime(0)}):
        if(report["time"][3] < 13):
            time = f"{report['time'][3]}:{report['time'][4]:02} am"
        else:
            time = f"{report['time'][3]-12}:{report['time'][4]:02} pm"
        # print(f"{report['name']} taken at " + time + f" on {report['time'][1]}-{report['time'][2]}-{report['time'][0]}")
        return f"{report['name']} taken at " + time + f" on {report['time'][1]}-{report['time'][2]}-{report['time'][0]}\n"

    def generateReport(self, medName: str = None, time1: time.struct_time = None, time2: time.struct_time = None):
        reportString = ""
        try:
            with open(self.reportFileName, mode="r", encoding="utf-8") as f:
                try:
                    tempArray = json.load(f)
                    for report in tempArray:
                        if(medName != None):
                            if(report["name"] == medName):
                                reportString = reportString + self.printReport(report)
                        else:
                            reportString = reportString + self.printReport(report)
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            print(f"File '{self.reportFileName}' not found! Aborting")
            exit(1)
        f.close()
        return reportString
    
    def clearReport(self):
        try:
            with open(self.reportFileName, mode="w", encoding="utf-8") as f:
                pass
        except FileNotFoundError:
            print(f"File '{self.reportFileName}' not found! Aborting")
            exit(1)
        f.close()