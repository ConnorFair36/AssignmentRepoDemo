import unittest
import json
from handle_accounts import DoctorAccount

test_data = [
  {
    "id": 0,
    "name": "Emily Carter",
    "password": "emily123!",
    "phone": "5551234567",
    "email": "emily.carter@healthcare.org",
    "institution name": "Springfield Medical Center"
  },
  {
    "id": 1,
    "name": "James Thompson",
    "password": "secureJames99",
    "phone": "5552345678",
    "email": "james.thompson@medgroup.com",
    "institution name": "Greenwood Clinic"
  },
  {
    "id": 2,
    "name": "Sophia Nguyen",
    "password": "sophia@789",
    "phone": "5553456789",
    "email": "sophia.nguyen@wellness.org",
    "institution name": "Downtown Health Services"
  },
  {
    "id": 3,
    "name": "Daniel Lee",
    "password": "passDaniel2025",
    "phone": "5554567890",
    "email": "daniel.lee@familymed.com",
    "institution name": "Evergreen Family Medicine"
  },
  {
    "id": 4,
    "name": "Ava Martinez",
    "password": "avaSecure!23",
    "phone": "5555678901",
    "email": "ava.martinez@clinicnet.org",
    "institution name": "Riverside Health Partners"
  },
  {
    "id": 5,
    "name": "Michael Brown",
    "password": "michael_456",
    "phone": "5556789012",
    "email": "michael.brown@hospitalgroup.com",
    "institution name": "Oakwood General Hospital"
  },
  {
    "id": 6,
    "name": "Isabella Wilson",
    "password": "bellaPass2024",
    "phone": "5557890123",
    "email": "isabella.wilson@carefirst.net",
    "institution name": "Pine Hill Medical Center"
  },
  {
    "id": 7,
    "name": "Ethan Davis",
    "password": "ethanSecure!",
    "phone": "5558901234",
    "email": "ethan.davis@citymed.org",
    "institution name": "City Health Clinic"
  },
  {
    "id": 8,
    "name": "Mia Hernandez",
    "password": "mia_Health1",
    "phone": "5559012345",
    "email": "mia.hernandez@medaccess.com",
    "institution name": "Lakeside Wellness Center"
  },
  {
    "id": 9,
    "name": "Alexander Robinson",
    "password": "alexR_2025!",
    "phone": "5550123456",
    "email": "alex.robinson@healthnet.org",
    "institution name": "Northview Medical Institute"
  }
]

test_data2 = [
  { "1": [3, 4, 5] },
  { "2": [6, 7] },
  { "3": [8, 9, 10, 11] },
  { "4": [12, 13] },
  { "5": [14, 15, 16] },
  { "6": [17, 18, 19] },
  { "7": [20, 21] },
  { "8": [22, 23, 24, 25] },
  { "9": [26, 27, 28, 29] }
]


test_account = {"name": "Nota Doc",
				"password": "password123",
				"phone": "8888880000",
				"email": "unreal@notgoogle.con",
				"institution name": "not a hospital"}

def empty_json_file():
	with open("allDoctors.json", mode="w", encoding="utf-8") as f:
		json.dump([], f, indent=4)
		f.close()

def empty_docPat_file():
	with open("doctorPatients.json", mode="w", encoding="utf-8") as f:
		json.dump([], f, indent=4)
		f.close()

def get_file_data():
	all_records = []
	try:
		with open("allDoctors.json", mode="r", encoding="utf-8") as f:
			try:
				all_records = json.load(f)
			except json.decoder.JSONDecodeError:
				pass
	except FileNotFoundError:
		print(f"File 'allDoctors.json' not found! Aborting")
		exit(1)
	f.close()
	return all_records

def get_docPat_file():
	all_records = []
	try:
		with open("doctorPatients.json", mode="r", encoding="utf-8") as f:
			try:
				all_records = json.load(f)
			except json.decoder.JSONDecodeError:
				pass
	except FileNotFoundError:
		print(f"File 'doctorPatients.json' not found! Aborting")
		exit(1)
	f.close()
	return all_records

class TestDoctorAccount(unittest.TestCase):
	def setUp(self):
		with open("allDoctors.json", mode="w", encoding="utf-8") as f:
			json.dump(test_data, f, indent=4)
			f.close()
		with open("doctorPatients.json", mode="w", encoding="utf-8") as f:
			json.dump(test_data2, f, indent=4)
			f.close()
		self.DoctorAccount = DoctorAccount()

	# create account on empty .json
	def test_case_13(self):
		empty_json_file()
		self.DoctorAccount = DoctorAccount()

		self.DoctorAccount.create_account(test_account["name"],
										   test_account["password"],
										   test_account["phone"],
										   test_account["email"],
										   test_account["institution name"])
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertEqual(self.DoctorAccount.account["id"], 0)

	# create account on filled .json
	def test_case_14(self):
		self.DoctorAccount.create_account(test_account["name"],
										  test_account["password"],
										  test_account["phone"],
										  test_account["email"],
										  test_account["institution name"])
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertEqual(self.DoctorAccount.account["id"], 10)

	# find account valid name and password
	def test_case_15(self):
		self.assertTrue(self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"]))
		self.assertEqual(self.DoctorAccount.account, get_file_data()[0])

	# find account on empty .json
	def test_case_16(self):
		empty_json_file()
		self.DoctorAccount = DoctorAccount()
		self.assertFalse(self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"]))
		self.assertFalse(self.DoctorAccount.account)

	# find account invalid name
	def test_case_17(self):
		self.assertFalse(self.DoctorAccount.find_account("INVALID NAME", test_data[0]["password"]))
		self.assertFalse(self.DoctorAccount.account)

	# find account invalid password
	def test_case_18(self):
		self.assertFalse(self.DoctorAccount.find_account(test_data[0]["name"], "INVALID PASSWORD"))
		self.assertFalse(self.DoctorAccount.account)

	# find account invalid name and password
	def test_case_19(self):
		self.assertFalse(self.DoctorAccount.find_account("INVALID NAME", "INVALID PASSWORD"))
		self.assertFalse(self.DoctorAccount.account)

	# update account no arguments given
	def test_case_20(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.update_account()
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertEqual(self.DoctorAccount.account, get_file_data()[0])
		self.assertEqual(self.DoctorAccount.account, test_data[0])

	# update account some arguments giver
	def test_case_21(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.update_account(name="NEW NAME", phone_number="0987654321",
										   institution_name="NEW INSTITUTION")
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertEqual(self.DoctorAccount.account, get_file_data()[0])
		self.assertNotEqual(self.DoctorAccount.account["name"], test_data[0]["name"])
		self.assertEqual(self.DoctorAccount.account["password"], test_data[0]["password"])
		self.assertNotEqual(self.DoctorAccount.account["phone"], test_data[0]["phone"])
		self.assertEqual(self.DoctorAccount.account["email"], test_data[0]["email"])
		self.assertNotEqual(self.DoctorAccount.account["institution name"], test_data[0]["institution name"])

	# update account all arguments
	def test_case_22(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.update_account("New Name", "NEWPASSWORD", "0987654321",
										   "new@em.ail", "NEW INSTITUTION")
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertEqual(self.DoctorAccount.account, get_file_data()[0])
		self.assertNotEqual(self.DoctorAccount.account["name"], test_data[0]["name"])
		self.assertNotEqual(self.DoctorAccount.account["password"], test_data[0]["password"])
		self.assertNotEqual(self.DoctorAccount.account["phone"], test_data[0]["phone"])
		self.assertNotEqual(self.DoctorAccount.account["email"], test_data[0]["email"])
		self.assertNotEqual(self.DoctorAccount.account["institution name"], test_data[0]["institution name"])

	# delete an account
	def test_case_23(self):
		self.DoctorAccount.find_account(test_data[5]["name"], test_data[5]["password"])
		self.DoctorAccount.delete_account()
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertFalse(self.DoctorAccount.account)
		self.assertFalse(test_data[5] in get_file_data())

	# delete an empty account
	def test_case_24(self):
		self.DoctorAccount.delete_account()
		self.assertEqual(self.DoctorAccount.all_records, get_file_data())
		self.assertFalse(self.DoctorAccount.account)

	# add patient to list empty .json and no list
	def test_case_25(self):
		empty_docPat_file()
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.assertTrue(self.DoctorAccount.add_patient("James Wilson"))
		self.assertEqual(self.DoctorAccount.patient_list, get_docPat_file()[0]["0"])

	# add patient to list filled .json and this doctor has no patient list
	def test_case_26(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.assertTrue(self.DoctorAccount.add_patient("James Wilson"))
		self.assertEqual(self.DoctorAccount.patient_list, get_docPat_file()[-1]["0"])

	# add patient to list filled .json, Doc already has some other patients
	def test_case_27(self):
		self.DoctorAccount.find_account(test_data[1]["name"], test_data[1]["password"])
		self.assertTrue(self.DoctorAccount.add_patient("James Wilson"))
		self.assertEqual(self.DoctorAccount.patient_list, get_docPat_file()[0]["1"])

	# add patient to list filled .json, Doc already has some other patients, including this patient
	def test_case_28(self):
		self.DoctorAccount.find_account(test_data[1]["name"], test_data[1]["password"])
		self.assertTrue(self.DoctorAccount.add_patient("Olivia Brown"))
		self.assertEqual(self.DoctorAccount.patient_list, get_docPat_file()[0]["1"])
		self.assertEqual(len(self.DoctorAccount.patient_list), 3)

	# remove patient where no doctors have patients
	def test_case_29(self):
		empty_docPat_file()
		self.DoctorAccount = DoctorAccount()
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.remove_patient(6)
		self.assertEqual(self.DoctorAccount.patient_list, [])
		self.assertEqual(get_docPat_file(), [])

	# remove patient where the current doctor has no patients
	def test_case_30(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.remove_patient(6)
		self.assertEqual(self.DoctorAccount.patient_list, [])
		self.assertEqual(get_docPat_file(), test_data2)

	# remove patient where the patient is the only one in the list
	def test_case_31(self):
		self.DoctorAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.DoctorAccount.add_patient("Noah Smith")
		self.assertEqual(self.DoctorAccount.patient_list, [2])
		self.assertNotEqual(get_docPat_file(), test_data2)
		self.DoctorAccount.remove_patient(2)
		self.assertEqual(self.DoctorAccount.patient_list, [])
		self.assertEqual(get_docPat_file(), test_data2)

	# remove patient where the patient is one of the patients in the list
	def test_case_32(self):
		self.DoctorAccount.find_account(test_data[1]["name"], test_data[1]["password"])
		self.DoctorAccount.remove_patient(4)
		self.assertEqual(self.DoctorAccount.patient_list, [3, 5])
		self.assertNotEqual(get_docPat_file()[0]["1"], test_data2[0]["1"])

	# remove patient where the patient is not in the list
	def test_case_33(self):
		self.DoctorAccount.find_account(test_data[1]["name"], test_data[1]["password"])
		self.DoctorAccount.remove_patient(2)
		self.assertEqual(self.DoctorAccount.patient_list, test_data2[0]["1"])
		self.assertEqual(get_docPat_file()[0]["1"], test_data2[0]["1"])

if __name__ == '__main__':
	unittest.main()