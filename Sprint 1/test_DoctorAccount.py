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

test_account = {"name": "Nota Doc",
				"password": "password123",
				"phone": "8888880000",
				"email": "unreal@notgoogle.con",
				"institution name": "not a hospital"}

def empty_json_file():
	with open("allDoctors.json", mode="w", encoding="utf-8") as f:
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

class TestDoctorAccount(unittest.TestCase):
	def setUp(self):
		with open("allDoctors.json", mode="w", encoding="utf-8") as f:
			json.dump(test_data, f, indent=4)
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


if __name__ == '__main__':
	unittest.main()