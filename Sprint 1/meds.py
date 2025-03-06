import json



# class meds:
#     def __init__(self, name="", conditions="", severity=0, time1=[-1, -1], time2=[-1, -1], time3=[-1, -1]):
#         #first element of time array is hours, second is minutes
#         #uses 24 hour time scale
#         #default -1 time means at time hasn't been set for a reminder
#         self.name = name
#         self.contidtions = conditions
#         self.severity = severity
#         self.time1 = time1
#         self.time2 = time2
#         self.time3 = time3

#     def valid(self):
#         if(self.severity < 0 or self.severity > 5):
#             return False
#         if(self.time1[0] < -1 or self.time1[0] > 24 or self.time1[1] < -1 or self.time1[1] > 60):
#             return False
#         if(self.time2[0] < -1 or self.time2[0] > 24 or self.time2[1] < -1 or self.time2[1] > 60):
#             return False
#         if(self.time3[0] < -1 or self.time3[0] > 24 or self.time3[1] < -1 or self.time3[1] > 60):
#             return False
#         else:
#             return True
            
class medsManager():
    def __init__(self):
        pass
    def addMedication(self, name="", conditions="", severity=0, time1={-1, -1}, time2={-1, -1}, time3={-1, -1}):
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
        #if self.newMed.valid():
        try:
            with open("medsList.json", mode="a", encoding="utf-8") as self.medsList:
                json.dump(self.newMed, self.medsList, indent = 4)
        except FileNotFoundError:
            print(f"File 'medsList.json' not found! Aborting")
            exit(1)
        
            #.dumps(self.newMed, indent = 4)
                