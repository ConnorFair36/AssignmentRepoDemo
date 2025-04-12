import time
import window

class reminder():
    def __init__(self):
        self.reminderSent = False
    def check(self, med = {
                        "name" : "",
                        "conditions" : "None",
                        "severity" : 0,
                        "time1" :{
                            "hours" : -1,
                            "minutes" : -1
                        },
                        "time2" :{
                            "hours" : -1,
                            "minutes" : -1
                        },
                        "time3" :{
                            "hours" : -1,
                            "minutes" : -1
                        },
                       }
                  , fileName = ""
                ):
        self.med = med.copy()
        self.fileName = fileName
        hour = time.localtime()[3]
        minute = time.localtime()[4]
        if(self.med["time1"]["hours"] == hour and self.med["time1"]["minutes"] == minute):
            self.sendReminder(minute)
        elif(self.med["time2"]["hours"] == hour and self.med["time2"]["minutes"] == minute):
            self.sendReminder(minute)
        elif(self.med["time3"]["hours"] == hour and self.med["time3"]["minutes"] == minute):
            self.sendReminder(minute)

    def sendReminder(self, minute):
        if(self.reminderSent == False):
            window.popupmsg(self.med, self.fileName)
            self.reminderSent = True
        elif(time.localtime()[4] > minute):
            self.reminderSent = False
        #add code to log a confirmation