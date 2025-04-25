from meds import medsManager
import os
import time

class patient():
    def __init__(self, first="", last="", phone="", insurance="", birthday=[00,00,0000]):
        self.info = {
            "name": {
                "first": first,
                "last": last
            },
            "phone": phone,
            "insurance": insurance,
            "birthday": {
                "mon": birthday[0],
                "day": birthday[1],
                "year": birthday[2]
            }
        }
        self.medsManager = medsManager(self.info["name"]["first"]+"_"+self.info["name"]["last"]+"_")

    def addMedication(self, name="", conditions="None", severity=0, time1=[-1, -1], time2=[-1, -1], time3=[-1, -1]):
        self.medsManager.addMedication(name, conditions, severity, time1, time2, time3)
    
    def clearMedsList(self):
        self.medsManager.clear()
    
    def deleteMedsFiles(self):
        """Removes the medication list and reoprt file that was created for the patient. Use with care."""
        if os.path.exists(self.medsManager.listFileName):
            os.remove(self.medsManager.listFileName)
        if os.path.exists(self.medsManager.reportFileName):
            os.remove(self.medsManager.reportFileName)
    
    def removeMedicaiton(self, name = ""):
        self.medsManager.removeMedication(name)

    def getMedsList(self):
        return self.medsManager.medsArray
    
    def findMed(self, name: str) -> dict:
        all_meds = self.getMedsList()
        all_names = [med["name"] for med in all_meds]
        try:
            index = all_names.index(name)
            return all_meds[index]
        except ValueError:
            return {}
    
    def reminderCheck(self):
        self.medsManager.reminderCheck()

    def generateReport(self, medName: str = None, time1: time.struct_time = None, time2: time.struct_time = None):
        self.medsManager.generateReport(medName, time1, time2)
    
    def clearReport(self):
        self.medsManager.clearReport()