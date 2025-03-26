from reminder import reminder
import unittest
import time

class TestReminder(unittest.TestCase):
    def setUp(self):
        self.reminder = reminder()
        self.local_time = time.localtime()[3:5]

    # tests if check() sends a pop-up window at the current time
    def test_case7(self):
        test_med = {"name" : "test",
                        "conditions" : "many O_O",
                        "severity" : 0,
                        "time1" :{
                            "hours" : self.local_time[0],
                            "minutes" : self.local_time[1],
                        }}
        self.reminder.check(test_med)
        self.assertTrue(self.reminder.reminderSent)

    # test to ensure that a time not equal to the current time will not trigger a pop-up
    def test_case8(self):
        test_med = {"name": "test",
                    "conditions": "many O_O",
                    "severity": 0,
                    "time1": {
                        "hours": (self.local_time[0] + 1) % 24,
                        "minutes": (self.local_time[1] + 1) % 60
                    },
                    "time2": {
                        "hours": -1,
                        "minutes": -1
                    },
                    "time3": {
                        "hours": -1,
                        "minutes": -1
                    }}
        self.reminder.check(test_med)
        self.assertFalse(self.reminder.reminderSent)


    def test_case9(self):
        test_med = {"name": "test",
                    "conditions": "many O_O",
                    "severity": 0,
                    "time1": {
                        "hours": self.local_time[0],
                        "minutes": self.local_time[1],
                    }}
        test_med2 = {"name": "test2",
                    "conditions": "too many O_O",
                    "severity": 3,
                    "time1": {
                        "hours": self.local_time[0],
                        "minutes": self.local_time[1],
                    }}
        test_med3 = {"name": "test3",
                    "conditions": "many O_O",
                    "severity": 5,
                    "time1": {
                        "hours": self.local_time[0],
                        "minutes": self.local_time[1],
                    }}
        # I am setting reminderSent to false each time because the class doesn't automaticly reset it yet
        self.reminder.check(test_med)
        self.assertTrue(self.reminder.reminderSent)
        self.reminder.reminderSent = False
        self.reminder.check(test_med2)
        self.assertTrue(self.reminder.reminderSent)
        self.reminder.reminderSent = False
        self.reminder.check(test_med3)
        self.assertTrue(self.reminder.reminderSent)

if __name__ == '__main__':
    unittest.main()

