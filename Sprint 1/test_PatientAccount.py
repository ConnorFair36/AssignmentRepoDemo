import unittest
import json
from handle_accounts import PatientAccount

test_data = [
  {
    "id": 0,
    "name": "Liam Johnson",
    "password": "liamJ!2025",
    "phone": "5551010101",
    "email": "liam.johnson@example.com",
    "birthday": "03-12-1990",
    "sex": "M",
    "insurance provider": "Blue Cross Blue Shield"
  },
  {
    "id": 1,
    "name": "Emma Garcia",
    "password": "emmaG2025#",
    "phone": "5552020202",
    "email": "emma.garcia@example.com",
    "birthday": "07-22-1985",
    "sex": "F",
    "insurance provider": "Aetna"
  },
  {
    "id": 2,
    "name": "Noah Smith",
    "password": "noahSecure99",
    "phone": "5553030303",
    "email": "noah.smith@example.com",
    "birthday": "01-08-2000",
    "sex": "M",
    "insurance provider": "Cigna"
  },
  {
    "id": 3,
    "name": "Olivia Brown",
    "password": "OliBrown@123",
    "phone": "5554040404",
    "email": "olivia.brown@example.com",
    "birthday": "10-31-1993",
    "sex": "F",
    "insurance provider": "UnitedHealthcare"
  },
  {
    "id": 4,
    "name": "William Davis",
    "password": "wDavis_2025",
    "phone": "5555050505",
    "email": "william.davis@example.com",
    "birthday": "05-17-1988",
    "sex": "M",
    "insurance provider": "Kaiser Permanente"
  },
  {
    "id": 5,
    "name": "Sophia Martinez",
    "password": "SophiaM!88",
    "phone": "5556060606",
    "email": "sophia.martinez@example.com",
    "birthday": "09-25-1996",
    "sex": "F",
    "insurance provider": "Humana"
  },
  {
    "id": 6,
    "name": "James Wilson",
    "password": "James_W2024",
    "phone": "5557070707",
    "email": "james.wilson@example.com",
    "birthday": "11-14-1975",
    "sex": "M",
    "insurance provider": "Blue Cross Blue Shield"
  },
  {
    "id": 7,
    "name": "Isabella Moore",
    "password": "is@bellaM2025",
    "phone": "5558080808",
    "email": "isabella.moore@example.com",
    "birthday": "06-06-2002",
    "sex": "F",
    "insurance provider": "Aetna"
  },
  {
    "id": 8,
    "name": "Benjamin Taylor",
    "password": "BenTay#2025",
    "phone": "5559090909",
    "email": "benjamin.taylor@example.com",
    "birthday": "02-19-1991",
    "sex": "M",
    "insurance provider": "Cigna"
  },
  {
    "id": 9,
    "name": "Mia Anderson",
    "password": "miaA_secure!",
    "phone": "5550001111",
    "email": "mia.anderson@example.com",
    "birthday": "12-04-1983",
    "sex": "F",
    "insurance provider": "UnitedHealthcare"
  },
  {
    "id": 10,
    "name": "Logan Thomas",
    "password": "log@2024T",
    "phone": "5551112222",
    "email": "logan.thomas@example.com",
    "birthday": "08-13-1995",
    "sex": "M",
    "insurance provider": "Cigna"
  },
  {
    "id": 11,
    "name": "Charlotte Lee",
    "password": "charLee#88",
    "phone": "5552223333",
    "email": "charlotte.lee@example.com",
    "birthday": "04-03-1989",
    "sex": "F",
    "insurance provider": "Aetna"
  },
  {
    "id": 12,
    "name": "Ethan Hall",
    "password": "ethanH_123",
    "phone": "5553334444",
    "email": "ethan.hall@example.com",
    "birthday": "01-27-1982",
    "sex": "M",
    "insurance provider": "Humana"
  },
  {
    "id": 13,
    "name": "Amelia Clark",
    "password": "ameliaC!2023",
    "phone": "5554445555",
    "email": "amelia.clark@example.com",
    "birthday": "03-15-1997",
    "sex": "F",
    "insurance provider": "Kaiser Permanente"
  },
  {
    "id": 14,
    "name": "Lucas Rodriguez",
    "password": "lucasRod2025",
    "phone": "5555556666",
    "email": "lucas.rodriguez@example.com",
    "birthday": "06-21-1990",
    "sex": "M",
    "insurance provider": "UnitedHealthcare"
  },
  {
    "id": 15,
    "name": "Harper Lewis",
    "password": "harperL#2025",
    "phone": "5556667777",
    "email": "harper.lewis@example.com",
    "birthday": "02-02-2001",
    "sex": "F",
    "insurance provider": "Blue Cross Blue Shield"
  },
  {
    "id": 16,
    "name": "Alexander Walker",
    "password": "alexW!pass",
    "phone": "5557778888",
    "email": "alex.walker@example.com",
    "birthday": "07-05-1984",
    "sex": "M",
    "insurance provider": "Aetna"
  },
  {
    "id": 17,
    "name": "Evelyn Perez",
    "password": "eveP@123",
    "phone": "5558889999",
    "email": "evelyn.perez@example.com",
    "birthday": "11-29-1992",
    "sex": "F",
    "insurance provider": "Cigna"
  },
  {
    "id": 18,
    "name": "Daniel Adams",
    "password": "danA_secure",
    "phone": "5559990000",
    "email": "daniel.adams@example.com",
    "birthday": "09-18-1987",
    "sex": "M",
    "insurance provider": "Humana"
  },
  {
    "id": 19,
    "name": "Abigail Campbell",
    "password": "abbyC!pass",
    "phone": "5551231234",
    "email": "abigail.campbell@example.com",
    "birthday": "05-06-1999",
    "sex": "F",
    "insurance provider": "Kaiser Permanente"
  },
  {
    "id": 20,
    "name": "Matthew Mitchell",
    "password": "mattM!2025",
    "phone": "5552342345",
    "email": "matthew.mitchell@example.com",
    "birthday": "10-11-1981",
    "sex": "M",
    "insurance provider": "UnitedHealthcare"
  },
  {
    "id": 21,
    "name": "Emily Rivera",
    "password": "emilyR!secure",
    "phone": "5553453456",
    "email": "emily.rivera@example.com",
    "birthday": "06-09-2003",
    "sex": "F",
    "insurance provider": "Blue Cross Blue Shield"
  },
  {
    "id": 22,
    "name": "Jackson Murphy",
    "password": "jackM_pass",
    "phone": "5554564567",
    "email": "jackson.murphy@example.com",
    "birthday": "03-26-1994",
    "sex": "M",
    "insurance provider": "Aetna"
  },
  {
    "id": 23,
    "name": "Ella Bailey",
    "password": "ellaB@secure",
    "phone": "5555675678",
    "email": "ella.bailey@example.com",
    "birthday": "08-30-1998",
    "sex": "F",
    "insurance provider": "Cigna"
  },
  {
    "id": 24,
    "name": "David Scott",
    "password": "dscott2025!",
    "phone": "5556786789",
    "email": "david.scott@example.com",
    "birthday": "12-15-1986",
    "sex": "M",
    "insurance provider": "Humana"
  },
  {
    "id": 25,
    "name": "Scarlett Cooper",
    "password": "scarlettC!pass",
    "phone": "5557897890",
    "email": "scarlett.cooper@example.com",
    "birthday": "04-27-1990",
    "sex": "F",
    "insurance provider": "Kaiser Permanente"
  },
  {
    "id": 26,
    "name": "Joseph Reed",
    "password": "joeR#secure",
    "phone": "5558908901",
    "email": "joseph.reed@example.com",
    "birthday": "01-23-1980",
    "sex": "M",
    "insurance provider": "UnitedHealthcare"
  },
  {
    "id": 27,
    "name": "Victoria Price",
    "password": "vickiP_2025",
    "phone": "5559019012",
    "email": "victoria.price@example.com",
    "birthday": "07-12-1991",
    "sex": "F",
    "insurance provider": "Blue Cross Blue Shield"
  },
  {
    "id": 28,
    "name": "Andrew Jenkins",
    "password": "andyJ_secure",
    "phone": "5550120123",
    "email": "andrew.jenkins@example.com",
    "birthday": "05-30-1983",
    "sex": "M",
    "insurance provider": "Aetna"
  },
  {
    "id": 29,
    "name": "Aria Bennett",
    "password": "ariaB!pass",
    "phone": "5551239876",
    "email": "aria.bennett@example.com",
    "birthday": "09-03-1995",
    "sex": "F",
    "insurance provider": "Cigna"
  }
]

test_account = {"name": "John Cenna",
				"password": "DOOTDODODOOOO",
				"phone": "1234567890",
				"email": "andhisname@is.johncena",
				"birthday": "03-12-1990",
				"sex": "M",
				"insurance provider": "WWE"}

def empty_json_file():
	with open("allPatients.json", mode="w", encoding="utf-8") as f:
		json.dump([], f, indent=4)
		f.close()

def get_file_data():
	all_records = []
	try:
		with open("allPatients.json", mode="r", encoding="utf-8") as f:
			try:
				all_records = json.load(f)
			except json.decoder.JSONDecodeError:
				pass
	except FileNotFoundError:
		print(f"File 'allPatients.json' not found! Aborting")
		exit(1)
	f.close()
	return all_records

class TestPatientAccount(unittest.TestCase):
	def setUp(self):
		with open("allPatients.json", mode="w", encoding="utf-8") as f:
			json.dump(test_data, f, indent=4)
			f.close()
		self.PatientAccount = PatientAccount()

	# create account on empty .json
	def test_case_1(self):
		# NOTE: For any test cases that use an empty .json file, reset the PatientAccount object
		empty_json_file()
		self.PatientAccount = PatientAccount()

		self.PatientAccount.create_account(test_account["name"],
										   test_account["password"],
										   test_account["phone"],
										   test_account["email"],
										   test_account["birthday"],
										   test_account["sex"],
										   test_account["insurance provider"])
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertEqual(self.PatientAccount.account["id"],0)

	# create account on filled .json
	def test_case_2(self):
		self.PatientAccount.create_account(test_account["name"],
										   test_account["password"],
										   test_account["phone"],
										   test_account["email"],
										   test_account["birthday"],
										   test_account["sex"],
										   test_account["insurance provider"])
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertEqual(self.PatientAccount.account["id"], 30)

	# find account with valid name and password
	def test_case_3(self):
		self.assertTrue(self.PatientAccount.find_account(test_data[0]["name"],test_data[0]["password"]))
		self.assertEqual(self.PatientAccount.account, get_file_data()[0])

	# find account on empty .json
	def test_case_4(self):
		empty_json_file()
		self.PatientAccount = PatientAccount()
		self.assertFalse(self.PatientAccount.find_account(test_data[0]["name"], test_data[0]["password"]))
		self.assertFalse(self.PatientAccount.account)

	# find account invalid name
	def test_case_5(self):
		self.assertFalse(self.PatientAccount.find_account("INVALID NAME", test_data[0]["password"]))
		self.assertFalse(self.PatientAccount.account)

	# find account invalid password
	def test_case_6(self):
		self.assertFalse(self.PatientAccount.find_account(test_data[0]["name"], "INVALID PASSWORD"))
		self.assertFalse(self.PatientAccount.account)

	# find account invalid name and password
	def test_case_7(self):
		self.assertFalse(self.PatientAccount.find_account("INVALID NAME", "INVALID PASSWORD"))
		self.assertFalse(self.PatientAccount.account)

	# update account with no arguments given
	def test_case_8(self):
		self.PatientAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.PatientAccount.update_account()
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertEqual(self.PatientAccount.account, get_file_data()[0])
		self.assertEqual(self.PatientAccount.account, test_data[0])

	# update account some arguments
	def test_case_9(self):
		self.PatientAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.PatientAccount.update_account(name="NEW NAME", phone_number="0987654321",
										   insur_prov="NEW INSURANCE PROVIDER")
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertEqual(self.PatientAccount.account, get_file_data()[0])
		self.assertNotEqual(self.PatientAccount.account["name"], test_data[0]["name"])
		self.assertEqual(self.PatientAccount.account["password"], test_data[0]["password"])
		self.assertNotEqual(self.PatientAccount.account["phone"], test_data[0]["phone"])
		self.assertEqual(self.PatientAccount.account["email"], test_data[0]["email"])
		self.assertEqual(self.PatientAccount.account["birthday"], test_data[0]["birthday"])
		self.assertEqual(self.PatientAccount.account["sex"], test_data[0]["sex"])
		self.assertNotEqual(self.PatientAccount.account["insurance provider"], test_data[0]["insurance provider"])

	# update account all arguments
	def test_case_10(self):
		self.PatientAccount.find_account(test_data[0]["name"], test_data[0]["password"])
		self.PatientAccount.update_account("New Name", "NEWPASSWORD", "0987654321",
										   "new@em.ail", "DD-MM-YYYY", "ALL", "NEW PROVIDER")
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertEqual(self.PatientAccount.account, get_file_data()[0])
		self.assertNotEqual(self.PatientAccount.account["name"], test_data[0]["name"])
		self.assertNotEqual(self.PatientAccount.account["password"], test_data[0]["password"])
		self.assertNotEqual(self.PatientAccount.account["phone"], test_data[0]["phone"])
		self.assertNotEqual(self.PatientAccount.account["email"], test_data[0]["email"])
		self.assertNotEqual(self.PatientAccount.account["birthday"], test_data[0]["birthday"])
		self.assertNotEqual(self.PatientAccount.account["sex"], test_data[0]["sex"])
		self.assertNotEqual(self.PatientAccount.account["insurance provider"], test_data[0]["insurance provider"])

	# delete an account
	def test_case_11(self):
		self.PatientAccount.find_account(test_data[5]["name"], test_data[5]["password"])
		self.PatientAccount.delete_account()
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertFalse(self.PatientAccount.account)
		self.assertFalse(test_data[5] in get_file_data())

	# delete an empty account
	def test_case_12(self):
		self.PatientAccount.delete_account()
		self.assertEqual(self.PatientAccount.all_records, get_file_data())
		self.assertFalse(self.PatientAccount.account)

if __name__ == '__main__':
	unittest.main()
