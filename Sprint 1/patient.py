from meds import medsManager

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

    def addMedication(self, name="", conditions="", severity=0, time1=[-1, -1], time2=[-1, -1], time3=[-1, -1]):
        self.medsManager(name, conditions, severity, time1, time2, time3)