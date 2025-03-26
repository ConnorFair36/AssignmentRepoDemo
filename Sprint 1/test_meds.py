from meds import medsManager
import unittest

class MedsManagerTest(unittest.TestCase):
    # creates a new, empty medsManager and empty medsList.json before each test case
    def setUp(self):
        self.medsManager = medsManager()
        self.medsManager.clear()

    # places a single medication into the meds list
    def test_case_1(self):
        self.medsManager.addMedication("adderall", "take with food", 3, [8,0], [14, 14], [20, 0])
        current_meds = self.medsManager.getMedsList()
        self.assertEqual(current_meds[0], {'name': 'adderall', 'conditions': 'take with food', 'severity': 3, 'time1': {'hours': 8, 'minutes': 0}, 'time2': {'hours': 14, 'minutes': 14}, 'time3': {'hours': 20, 'minutes': 0}},
                         "Data of the .json file is different from the expected input")

    # places another medication into the .json file
    def test_case_2(self):
        # precondition: .json has 1 entry
        self.medsManager.addMedication("adderall", "take with food", 3, [8, 0], [14, 14], [20, 0])

        self.medsManager.addMedication("xanax", "", 3, [7, 0])
        current_meds = self.medsManager.getMedsList()
        self.assertEqual(current_meds[1], {"name": "xanax", "conditions": "","severity": 3,"time1": {"hours": 7,"minutes": 0},"time2": {"hours": -1,"minutes": -1},"time3": {"hours": -1,"minutes": -1}},
                         "Data of 2nd entry in the .json file is different from the expected input")

    # places a medication without a time 3
    def test_case_3(self):
        self.medsManager.addMedication("adderall", "take with food", 3, [8, 0], [14, 14])
        current_meds = self.medsManager.getMedsList()
        self.assertEqual(current_meds[0], {'name': 'adderall', 'conditions': 'take with food', 'severity': 3,
                                           'time1': {'hours': 8, 'minutes': 0}, 'time2': {'hours': 14, 'minutes': 14},
                                           'time3': {'hours': -1, 'minutes': -1}},
                         "Data of the .json file is different from the expected input")

    # places a medication without a time 3 or time 2
    def test_case_4(self):
        self.medsManager.addMedication("adderall", "take with food", 3, [8, 0])
        current_meds = self.medsManager.getMedsList()
        self.assertEqual(current_meds[0], {'name': 'adderall', 'conditions': 'take with food', 'severity': 3,
                                           'time1': {'hours': 8, 'minutes': 0}, 'time2': {'hours': -1, 'minutes': -1},
                                           'time3': {'hours': -1, 'minutes': -1}},
                         "Data of the .json file is different from the expected input")

    # TODO add test cases 5 & 6 from the google doc


if __name__ == '__main__':
    unittest.main()

    # {'name': 'adderall', 'conditions': 'take with food', 'severity': 3, 'time1': {'hours': 8, 'minutes': 0}, 'time2': {'hours': 14, 'minutes': 14}, 'time3': {'hours': 20, 'minutes': 0}}

